import asyncio
from aiohttp import web
import logging
import math
import time

"""
Setup a bone simple webserver, listen to POST's from a device like a
GW1000 or in my case, HP3501, decode results.
"""


ECOWITT_LISTEN_PORT = 4199
WINDCHILL_OLD = 0
WINDCHILL_NEW = 1
WINDCHILL_HYBRID = 2


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
        alpha = ((A * t_air_c) / (B + t_air_c)) + math.log(rel_humidity/100.0)
        return round((B * alpha) / (A - alpha), 2)

    def _ftoc(self, f):
        """ Convert f to c."""
        F = float(f)
        c = round((F - 32.0) * 5.0 / 9.0, 2)
        return(c)

    def _wind_chill(self, f, mph):
        """ New formula discards wind < 3.0 and temp > 50"""
        new = round((91.4 - (0.474677 - 0.020425 * mph + 0.303107
                             * math.sqrt(mph)) * (91.4 - f)), 2)
        old = round((35.74 + (0.6215 * f) - 35.75 * (mph ** 0.16)
                     + 0.4275 * f * (mph ** 0.16)), 2)

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

        # basic conversions
        if "humidityin" in data:
            data["humidityin"] = int(data["humidityin"])
        if "humidity" in data:
            data["humidity"] = int(data["humidity"])
        if "winddir" in data:
            data["winddir"] = int(data["winddir"])
        if "uv" in data:
            data["uv"] = int(data["uv"])
        if "solarradiation" in data:
            data["solarradiation"] = float(data["solarradiation"])

        # temperatures
        if "tempf" in data:
            data["tempf"] = float(data["tempf"])
            data["tempc"] = self._ftoc(data["tempf"])
        if "tempinf" in data:
            data["tempinf"] = float(data["tempinf"])
            data["tempinc"] = self._ftoc(data["tempinf"])
        if "temp1f" in data:
            data["temp1f"] = float(data["temp1f"])
            data["temp1c"] = self._ftoc_(data["temp1f"])
        if "temp2f" in data:
            data["temp2f"] = float(data["temp2f"])
            data["temp2c"] = self._ftoc(data["temp2f"])
        if "temp3f" in data:
            data["temp3f"] = float(data["temp3f"])
            data["temp3c"] = self._ftoc(data["temp3f"])

        # speeds
        if "windspeedmph" in data:
            data["windspeedmph"] = float(data["windspeedmph"])
            data["windspeedkmh"] = round(data["windspeedmph"] * mph_kmh, 2)
            data["windspeedms"] = round(data["windspeedmph"] * mph_ms, 2)
        if "windgustmph" in data:
            data["windgustmph"] = float(data["windgustmph"])
            data["windgustkmh"] = round(data["windgustmph"] * mph_kmh, 2)
            data["windgustms"] = round(data["windgustmph"] * mph_ms, 2)

        # distances
        if "rainratein" in data:
            data["rainratein"] = float(data["rainratein"])
            data["rainratemm"] = round(data["rainratein"] * in_mm, 2)
        if "eventrainin" in data:
            data["eventrainin"] = float(data["eventrainin"])
            data["eventrainmm"] = round(data["eventrainin"] * in_mm, 2)
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
        if "tempc" in data and "humidity" in data:
            data["dewpointc"] = self.get_dew_point_c(data["tempc"],
                                                     data["humidity"])
            data["dewpointf"] = round((data["dewpointc"] * 9.0 / 5.0) + 32.0, 2)

        # Soil moisture
        for j in range(1, 10):
            sm = f"soilmoisture{j}"
            if sm in data:
                data[sm] = int(data[sm])

        return(data)

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
