"""
Setup a bone simple webserver, listen to POST's from a device like a
GW1000 or in my case, HP3501, decode results.
"""

import asyncio
from aiohttp import web
import logging
import math
import time

from .sensor_map import (
    EcoWittSensorTypes,
    MAP_NAME as MAP_NAME,
    MAP_SYSTEM as MAP_SYSTEM,
    MAP_STYPE as MAP_STYPE,
    SENSOR_MAP as SENSOR_MAP
)

ECOWITT_LISTEN_PORT = 4199
WINDCHILL_OLD = 0
WINDCHILL_NEW = 1
WINDCHILL_HYBRID = 2


class EcoWittSensor:
    """An internal sensor to the ecowitt."""
    def __init__(self, sensor_name, key, system, stype):
        """Initialize."""
        self.name = sensor_name
        self.key = key
        self.value = None
        self.system = system
        self.stype = stype
        self.lastupd = 0
        self.lastupd_m = 0

    def get_value(self):
        """Get the sensor value."""
        return self.value

    def set_value(self, value):
        """Set the sensor value."""
        self.value = value

    def get_system(self):
        """Get the system."""
        return self.system

    def get_stype(self):
        """Get the sensor type."""
        return self.stype

    def get_name(self):
        """Get the sensor name."""
        return self.name

    def get_key(self):
        """Get the sensor key."""
        return self.key

    def set_lastupd(self, value):
        """Set the last update time on this sensor."""
        self.lastupd = value

    def get_lastupd(self):
        """Get the last update time of this sensor."""
        return self.lastupd

    def set_lastupd_m(self, value):
        """Set the last update monotonic time on this sensor."""
        self.lastupd_m = value

    def get_lastupd_m(self):
        """Get the last update monotonic time of this sensor."""
        return self.lastupd_m


class EcoWittListener:
    def __init__(self, port=ECOWITT_LISTEN_PORT):
        # API Constants
        self.port = port

        # internal states
        self.server = None
        self.runner = None
        self.site = None
        self.r_listeners = []
        self.last_values = {}
        self.data_valid = False
        self.log = logging.getLogger(__name__)
        self.lastupd = 0
        self.windchill_type = WINDCHILL_HYBRID
        self.new_sensor_cb = None

        # storage
        self._station_type = "Unknown"
        self._station_freq = "Unknown"
        self._station_model = "Unknown"
        self._mac_addr = None

        self.data_ready = False
        self.sensors = []
        self.known_sensor_keys = []

    def int_new_sensor_cb(self):
        """Internal new sensor callback

        binds to self.new_sensor_cb
        """
        if self.new_sensor_cb is None:
            return
        self.new_sensor_cb()

    def set_windchill(self, wind):
        """Set a windchill mode, [012]."""
        if wind < 0 or wind > 2:
            return
        self.windchill_type = wind

    def register_listener(self, function):
        self.r_listeners.append(function)

    def get_dew_point_c(self, t_air_c, rel_humidity):
        """Compute the dew point in degrees Celsius
        FROM https://gist.github.com/sourceperl/45587ea99ff123745428
        :param t_air_c: current ambient temperature in degrees Celsius
        :type t_air_c: float
        :param rel_humidity: relative humidity in %
        :type rel_humidity: float
        :return: the dew point in degrees Celsius
        :rtype: float
        """
        A = 17.27
        B = 237.7
        alpha = ((A * t_air_c) / (B + t_air_c)) + math.log(rel_humidity / 100.0)
        return round((B * alpha) / (A - alpha), 2)

    def _ftoc(self, f):
        """ Convert f to c."""
        F = float(f)
        c = round((F - 32.0) * 5.0 / 9.0, 2)
        return(c)

    def _wind_chill(self, f, mph):
        """ New formula discards wind < 3.0 and temp > 50"""
        old = round((91.4 - (0.474677 - 0.020425 * mph + 0.303107
                             * math.sqrt(mph)) * (91.4 - f)), 2)
        new = round((35.74 + (0.6215 * f) - 35.75 * (mph ** 0.16)
                     + 0.4275 * f * (mph ** 0.16)), 2)

        # don't return a windchill higher than the temp.
        if (old > f):
            old = f
        if (new > f):
            new = f

        if self.windchill_type == WINDCHILL_NEW:
            if (f > 50.0 or mph < 3.0):
                return f
            else:
                return new
        if self.windchill_type == WINDCHILL_OLD:
            return old
        if self.windchill_type == WINDCHILL_HYBRID:
            if (f > 50.0 or mph < 3.0):
                return old
            else:
                return new
        return f

    def convert_units(self, data):
        """ Convert imperial to metric """
        # math stolen from:
        # https://github.com/iz0qwm/ecowitt_http_gateway/blob/master/index.php
        mph_kmh = 1.60934
        # mph_kts = 0.868976
        mph_ms = 0.44707
        in_hpa = 33.86
        in_mm = 25.4
        km_mi = 0.6213712

        # basic conversions
        if "humidityin" in data:
            data["humidityin"] = int(data["humidityin"])
        if "humidity" in data:
            data["humidity"] = int(data["humidity"])
        if "winddir" in data:
            data["winddir"] = int(data["winddir"])
        if "winddir_avg10m" in data:
            data["winddir_avg10m"] = int(data["winddir_avg10m"])
        if "uv" in data:
            data["uv"] = int(data["uv"])
        if "solarradiation" in data:
            data["solarradiation"] = float(data["solarradiation"])

        # lightning
        if "lightning_time" in data:
            if (data["lightning_time"] is not None and
                data["lightning_time"] != ''):
                data["lightning_time"] = int(data["lightning_time"])
        if "lightning_num" in data:
            data["lightning_num"] = int(data["lightning_num"])
        if "lightning" in data:
            if (data["lightning"] is not None and
                    data["lightning"] != ''):
                data["lightning"] = int(data["lightning"])
                data["lightning_mi"] = int(round(data["lightning"] * km_mi))

        # temperatures
        if "tempf" in data:
            data["tempf"] = float(data["tempf"])
            data["tempc"] = self._ftoc(data["tempf"])
        if "tempinf" in data:
            data["tempinf"] = float(data["tempinf"])
            data["tempinc"] = self._ftoc(data["tempinf"])
        # (WH45)
        if "tf_co2" in data:
            data["tf_co2"] = float(data["tf_co2"])
            data["tf_co2c"] = self._ftoc(data["tf_co2"])
        # WN34 Soil Temperature Sensor
        for j in range(1, 9):
            wnf = f"tf_ch{j}"
            wnc = f"tf_ch{j}c"
            if wnf in data:
                data[wnf] = float(data[wnf])
                data[wnc] = self._ftoc(data[wnf])

        # numbered WH31 temp/humid
        for j in range(1, 9):
            tmpf = f"temp{j}f"
            tmpc = f"temp{j}c"
            hm = f"humidity{j}"
            if tmpf in data:
                data[tmpf] = float(data[tmpf])
                data[tmpc] = self._ftoc(data[tmpf])
            if hm in data:
                data[hm] = int(data[hm])

        # speeds
        if "windspeedmph" in data:
            data["windspeedmph"] = float(data["windspeedmph"])
            data["windspeedkmh"] = round(data["windspeedmph"] * mph_kmh, 2)
            data["windspeedms"] = round(data["windspeedmph"] * mph_ms, 2)
        if "windgustmph" in data:
            data["windgustmph"] = float(data["windgustmph"])
            data["windgustkmh"] = round(data["windgustmph"] * mph_kmh, 2)
            data["windgustms"] = round(data["windgustmph"] * mph_ms, 2)
        # I assume this is MPH?
        if "maxdailygust" in data:
            data["maxdailygust"] = float(data["maxdailygust"])
            data["maxdailygustkmh"] = round(data["maxdailygust"] * mph_kmh, 2)
            data["maxdailygustms"] = round(data["maxdailygust"] * mph_ms, 2)
        if "windspdmph_avg10m" in data:
            data["windspdmph_avg10m"] = float(data["windspdmph_avg10m"])
            data["windspdkmh_avg10m"] = round(float(data["windspdmph_avg10m"]
                                                    * mph_kmh), 2)
            data["windspdms_avg10m"] = round(float(data["windspdmph_avg10m"]
                                                   * mph_ms), 2)

        # distances
        if "rainratein" in data:
            data["rainratein"] = float(data["rainratein"])
            data["rainratemm"] = round(data["rainratein"] * in_mm, 2)
        if "eventrainin" in data:
            data["eventrainin"] = float(data["eventrainin"])
            data["eventrainmm"] = round(data["eventrainin"] * in_mm, 2)
        if "hourlyrainin" in data:
            data["hourlyrainin"] = float(data["hourlyrainin"])
            data["hourlyrainmm"] = round(data["hourlyrainin"] * in_mm, 2)
        if "dailyrainin" in data:
            data["dailyrainin"] = float(data["dailyrainin"])
            data["dailyrainmm"] = round(data["dailyrainin"] * in_mm, 2)
        if "weeklyrainin" in data:
            data["weeklyrainin"] = float(data["weeklyrainin"])
            data["weeklyrainmm"] = round(data["weeklyrainin"] * in_mm, 2)
        if "monthlyrainin" in data:
            data["monthlyrainin"] = float(data["monthlyrainin"])
            data["monthlyrainmm"] = round(data["monthlyrainin"] * in_mm, 2)
        if "yearlyrainin" in data:
            data["yearlyrainin"] = float(data["yearlyrainin"])
            data["yearlyrainmm"] = round(data["yearlyrainin"] * in_mm, 2)
        if "totalrainin" in data:
            data["totalrainin"] = float(data["totalrainin"])
            data["totalrainmm"] = round(data["totalrainin"] * in_mm, 2)

        # Pressure
        if "baromrelin" in data:
            data["baromrelin"] = float(data["baromrelin"])
            data["baromrelhpa"] = round(data["baromrelin"] * in_hpa, 2)
        if "baromabsin" in data:
            data["baromabsin"] = float(data["baromabsin"])
            data["baromabshpa"] = round(data["baromabsin"] * in_hpa, 2)

        # Calculated values for fun!
        if "tempf" in data and "windspeedmph" in data:
            data["windchillf"] = self._wind_chill(data["tempf"],
                                                  data["windspeedmph"])
            data["windchillc"] = self._ftoc(data["windchillf"])
        for j in ['', 'in', '1', '2', '3', '4', '5', '6', '7', '8']:
            if "temp" + j + "c" in data and "humidity" + j in data:
                data["dewpoint" + j + "c"] = self.get_dew_point_c(data["temp" + j + "c"],
                                                                  data["humidity" + j])
                data["dewpoint" + j + "f"] = round((data["dewpoint" + j + "c"] * 9.0 / 5.0) + 32.0, 2)

        # Soil moisture (WH51)
        for j in range(1, 9):
            sm = f"soilmoisture{j}"
            if sm in data:
                data[sm] = int(data[sm])

        # PM 2.5 sensor (WH41)
        for j in range(1, 5):
            pm = f"pm25_ch{j}"
            pma = f"pm25_avg_24h_ch{j}"
            if pm in data:
                data[pm] = float(data[pm])
            if pma in data:
                data[pma] = float(data[pma])

        # Leak sensor (WH55)
        for j in range(1, 5):
            lk = f"leak_ch{j}"
            if lk in data:
                data[lk] = int(data[lk])

        # CO2 indoor air quality (WH45) (note temp is in temps above)
        pm_floats = [
            "pm25",
            "pm25_24h",
            "pm10",
            "pm10_24",
        ]
        for prefix in pm_floats:
            sm = f"{prefix}_co2"
            if sm in data:
                data[sm] = float(data[sm])
        if "co2" in data:
            data["co2"] = int(data["co2"])
        if "co2_24h" in data:
            data["co2_24h"] = int(data["co2_24h"])
        if "humi_co2" in data:
            data["humi_co2"] = int(data["humi_co2"])

        # Batteries
        bat_names = [
            "wh25",
            "wh26",
            "wh40",
            "wh57",
            "wh65",
            "wh68",
            "wh80",
            "co2_",
        ]
        bat_range_names = [
            "soil",
            "",  # for just 'batt'
            "pm25",
            "leak",
            "tf_",  # WN34 voltage type
        ]

        for prefix in bat_names:
            sm = f"{prefix}batt"
            if sm in data:
                data[sm] = float(data[sm])

        for r_prefix in bat_range_names:
            for j in range(1, 9):
                sm = f"{r_prefix}batt{j}"
                if sm in data:
                    data[sm] = float(data[sm])

        return(data)

    def find_sensor(self, key):
        for sensor in self.sensors:
            if sensor.get_key() == key:
                return sensor
        return None

    def parse_ws_data(self, weather_data):
        for sensor in weather_data.keys():
            sensor_dev = self.find_sensor(sensor)
            if sensor_dev is None:
                # we have a new sensor
                if sensor not in SENSOR_MAP:
                    self.log.warning("Unhandled sensor type %s value %s, "
                                     + "file a PR.", sensor, weather_data[sensor])
                    continue
                sensor_dev = EcoWittSensor(SENSOR_MAP[sensor][MAP_NAME],
                                           sensor,
                                           SENSOR_MAP[sensor][MAP_SYSTEM],
                                           SENSOR_MAP[sensor][MAP_STYPE].name)
                self.sensors.append(sensor_dev)
                self.int_new_sensor_cb()

            sensor_dev.set_value(weather_data[sensor])
            sensor_dev.set_lastupd(time.time())
            sensor_dev.set_lastupd_m(time.monotonic())

    async def handler(self, request: web.BaseRequest):
        if (request.method == 'POST'):
            data = await request.post()
            # data is not a dict, it's a MultiDict
            data_copy = {}
            for k in data.keys():
                data_copy[k] = data[k]
            weather_data = self.convert_units(data_copy)
            self.last_values = weather_data.copy()
            self.data_valid = True
            self.lastupd = time.time()
            self.parse_ws_data(weather_data)
            for rl in self.r_listeners:
                try:
                    await rl(weather_data)
                except:
                    pass

        return web.Response(text="OK")

    async def wait_for_valid_data(self):
        """ Wait for valid data, then return true. """
        while not self.data_valid:
            await asyncio.sleep(1)
        return self.data_valid

    async def listen(self):
        """ Listen and process."""

        self.server = web.Server(self.handler)
        self.runner = web.ServerRunner(self.server)
        await self.runner.setup()
        self.site = web.TCPSite(self.runner, port=self.port)
        await self.site.start()

        while True:
            await asyncio.sleep(10000)

    async def stop(self):
        await self.site.stop()

    async def start(self):
        loop = asyncio.get_event_loop()
        try:
            task = loop.create_task(self.listen())
            await task
        except Exception as e:
            self.log.error("Exiting listener {0}".format(str(e)))
        finally:
            loop.close()

    # Accessor functions
    def list_sensor_keys(self):
        """List all available sensors by key."""
        sensor_list = []
        for sensor in self.sensors:
            sensor_list.append(sensor.get_key())
        return sensor_list

    def list_sensor_keys_by_type(self, stype):
        """List all available sensors of a given type."""
        sensor_list = []
        for sensor in self.sensors:
            if sensor.get_stype() == stype:
                sensor_list.append(sensor.get_key())
        return sensor_list

    def get_sensor_value_by_key(self, key):
        """Find the sensor named key and return its value."""
        dev = self.find_sensor(key)
        if dev is None:
            return None
        return dev.get_value()
