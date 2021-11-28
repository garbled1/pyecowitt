"""Sensor map"""
import enum

SYSTEM_METRIC = 0
SYSTEM_IMPERIAL = 1
SYSTEM_METRIC_MS = 2

MAP_NAME = "name"
MAP_SYSTEM = "system"
MAP_STYPE = "stype"


class EcoWittSensorTypes(enum.Enum):
    pressure_hpa = 1
    pressure_inhg = 2
    rate_mm = 3
    rate_inches = 4
    humidity = 5
    degree = 6
    speed_kph = 7
    speed_mph = 8
    speed_mps = 9
    temperature_c = 10
    temperature_f = 11
    watt_meters_squared = 12
    uv_index = 13
    pm25 = 14
    timestamp = 15
    count = 16
    distance_km = 17
    distance_miles = 18
    binary = 19
    pm10 = 20
    voltage = 21
    battery_percentage = 22
    length_inches = 23
    length_mm = 24
    co2_ppm = 25
    internal = 26

SENSOR_MAP = {
    "baromabshpa": {
        MAP_NAME: "Absolute Pressure",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.pressure_hpa,
    }, "baromrelhpa": {
        MAP_NAME: "Relative Pressure",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.pressure_hpa,
    }, "baromabsin": {
        MAP_NAME: "Absolute Pressure",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.pressure_inhg,
    }, "baromrelin": {
        MAP_NAME: "Relative Pressure",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.pressure_inhg,
    }, "rainratein": {
        MAP_NAME: "Rain Rate",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.rate_inches,
    }, "eventrainin": {
        MAP_NAME: "Event Rain Rate",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.rate_inches,
    }, "hourlyrainin": {
        MAP_NAME: "Hourly Rain Rate",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.rate_inches,
    }, "totalrainin": {
        MAP_NAME: "Total Rain",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.length_inches,
    }, "dailyrainin": {
        MAP_NAME: "Daily Rain Rate",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.rate_inches,
    }, "weeklyrainin": {
        MAP_NAME: "Weekly Rain Rate",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.rate_inches,
    }, "monthlyrainin": {
        MAP_NAME: "Monthly Rain Rate",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.rate_inches,
    }, "yearlyrainin": {
        MAP_NAME: "Yearly Rain Rate",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.rate_inches,
    }, "rainratemm": {
        MAP_NAME: "Rain Rate",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.rate_mm,
    }, "eventrainmm": {
        MAP_NAME: "Event Rain Rate",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.rate_mm,
    }, "hourlyrainmm": {
        MAP_NAME: "Hourly Rain Rate",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.rate_mm,
    }, "totalrainmm": {
        MAP_NAME: "Total Rain",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.length_mm,
    }, "dailyrainmm": {
        MAP_NAME: "Daily Rain Rate",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.rate_mm,
    }, "weeklyrainmm": {
        MAP_NAME: "Weekly Rain Rate",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.rate_mm,
    }, "monthlyrainmm": {
        MAP_NAME: "Monthly Rain Rate",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.rate_mm,
    }, "yearlyrainmm": {
        MAP_NAME: "Yearly Rain Rate",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.rate_mm,
    }, "humidity": {
        MAP_NAME: "Humidity",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.humidity,
    }, "humidityin": {
        MAP_NAME: "Indoor Humidity",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.humidity,
    }, "humidity1": {
        MAP_NAME: "Humidity 1",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.humidity,
    }, "humidity2": {
        MAP_NAME: "Humidity 2",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.humidity,
    }, "humidity3": {
        MAP_NAME: "Humidity 3",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.humidity,
    }, "humidity4": {
        MAP_NAME: "Humidity 4",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.humidity,
    }, "humidity5": {
        MAP_NAME: "Humidity 5",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.humidity,
    }, "humidity6": {
        MAP_NAME: "Humidity 6",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.humidity,
    }, "humidity7": {
        MAP_NAME: "Humidity 7",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.humidity,
    }, "humidity8": {
        MAP_NAME: "Humidity 8",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.humidity,
    }, "winddir": {
        MAP_NAME: "Wind Direction",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.degree,
    }, "winddir_avg10m": {
        MAP_NAME: "Wind Direction 10m Avg",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.degree,
    }, "windspeedkmh": {
        MAP_NAME: "Wind Speed",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.speed_kph,
    }, "windspdkmh_avg10m": {
        MAP_NAME: "Wind Speed 10m Avg",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.speed_kph,
    }, "windgustkmh": {
        MAP_NAME: "Wind Gust",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.speed_kph,
    }, "maxdailygustkmh": {
        MAP_NAME: "Max Daily Wind Gust",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.speed_kph,
    }, "windspeedmph": {
        MAP_NAME: "Wind Speed",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.speed_mph,
    }, "windspdmph_avg10m": {
        MAP_NAME: "Wind Speed 10m Avg",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.speed_mph,
    }, "windgustmph": {
        MAP_NAME: "Wind Gust",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.speed_mph,
    }, "maxdailygust": {
        MAP_NAME: "Max Daily Wind Gust",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.speed_mph,
    }, "windspeedms": {
        MAP_NAME: "Wind Speed",
        MAP_SYSTEM: SYSTEM_METRIC_MS,
        MAP_STYPE: EcoWittSensorTypes.speed_mps,
    }, "windspdms_avg10m": {
        MAP_NAME: "Wind Speed 10m Avg",
        MAP_SYSTEM: SYSTEM_METRIC_MS,
        MAP_STYPE: EcoWittSensorTypes.speed_mps,
    }, "windgustms": {
        MAP_NAME: "Wind Gust",
        MAP_SYSTEM: SYSTEM_METRIC_MS,
        MAP_STYPE: EcoWittSensorTypes.speed_mps,
    }, "maxdailygustms": {
        MAP_NAME: "Max Daily Wind Gust",
        MAP_SYSTEM: SYSTEM_METRIC_MS,
        MAP_STYPE: EcoWittSensorTypes.speed_mps,
    }, "tempc": {
        MAP_NAME: "Outdoor Temperature",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "tempinc": {
        MAP_NAME: "Indoor Temperature",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "temp1c": {
        MAP_NAME: "Temperature 1",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "temp2c": {
        MAP_NAME: "Temperature 2",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "temp3c": {
        MAP_NAME: "Temperature 3",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "temp4c": {
        MAP_NAME: "Temperature 4",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "temp5c": {
        MAP_NAME: "Temperature 5",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "temp6c": {
        MAP_NAME: "Temperature 6",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "temp7c": {
        MAP_NAME: "Temperature 7",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "temp8c": {
        MAP_NAME: "Temperature 8",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "dewpointc": {
        MAP_NAME: "Dewpoint",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "dewpointinc": {
        MAP_NAME: "Indoor Dewpoint",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "dewpoint1c": {
        MAP_NAME: "Dewpoint 1",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "dewpoint2c": {
        MAP_NAME: "Dewpoint 2",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "dewpoint3c": {
        MAP_NAME: "Dewpoint 3",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "dewpoint4c": {
        MAP_NAME: "Dewpoint 4",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "dewpoint5c": {
        MAP_NAME: "Dewpoint 5",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "dewpoint6c": {
        MAP_NAME: "Dewpoint 6",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "dewpoint7c": {
        MAP_NAME: "Dewpoint 7",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "dewpoint8c": {
        MAP_NAME: "Dewpoint 8",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "windchillc": {
        MAP_NAME: "Windchill",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "tempf": {
        MAP_NAME: "Outdoor Temperature",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "tempinf": {
        MAP_NAME: "Indoor Temperature",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "temp1f": {
        MAP_NAME: "Temperature 1",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "temp2f": {
        MAP_NAME: "Temperature 2",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "temp3f": {
        MAP_NAME: "Temperature 3",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "temp4f": {
        MAP_NAME: "Temperature 4",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "temp5f": {
        MAP_NAME: "Temperature 5",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "temp6f": {
        MAP_NAME: "Temperature 6",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "temp7f": {
        MAP_NAME: "Temperature 7",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "temp8f": {
        MAP_NAME: "Temperature 8",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "dewpointf": {
        MAP_NAME: "Dewpoint",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "dewpointinf": {
        MAP_NAME: "Indoor Dewpoint",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "dewpoint1f": {
        MAP_NAME: "Dewpoint 1",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "dewpoint2f": {
        MAP_NAME: "Dewpoint 2",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "dewpoint3f": {
        MAP_NAME: "Dewpoint 3",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "dewpoint4f": {
        MAP_NAME: "Dewpoint 4",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "dewpoint5f": {
        MAP_NAME: "Dewpoint 5",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "dewpoint6f": {
        MAP_NAME: "Dewpoint 6",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "dewpoint7f": {
        MAP_NAME: "Dewpoint 7",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "dewpoint8f": {
        MAP_NAME: "Dewpoint 8",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "windchillf": {
        MAP_NAME: "Windchill",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "solarradiation": {
        MAP_NAME: "Solar Radiation",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.watt_meters_squared,
    }, "uv": {
        MAP_NAME: "UV Index",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.uv_index,
    }, "soilmoisture1": {
        MAP_NAME: "Soil Moisture 1",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.humidity,
    }, "soilmoisture2": {
        MAP_NAME: "Soil Moisture 2",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.humidity,
    }, "soilmoisture3": {
        MAP_NAME: "Soil Moisture 3",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.humidity,
    }, "soilmoisture4": {
        MAP_NAME: "Soil Moisture 4",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.humidity,
    }, "soilmoisture5": {
        MAP_NAME: "Soil Moisture 5",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.humidity,
    }, "soilmoisture6": {
        MAP_NAME: "Soil Moisture 6",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.humidity,
    }, "soilmoisture7": {
        MAP_NAME: "Soil Moisture 7",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.humidity,
    }, "soilmoisture8": {
        MAP_NAME: "Soil Moisture 8",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.humidity,
    }, "pm25_ch1": {
        MAP_NAME: "PM2.5 1",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.pm25,
    }, "pm25_ch2": {
        MAP_NAME: "PM2.5 2",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.pm25,
    }, "pm25_ch3": {
        MAP_NAME: "PM2.5 3",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.pm25,
    }, "pm25_ch4": {
        MAP_NAME: "PM2.5 4",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.pm25,
    }, "pm25_avg_24h_ch1": {
        MAP_NAME: "PM2.5 24h Average 1",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.pm25,
    }, "pm25_avg_24h_ch2": {
        MAP_NAME: "PM2.5 24h Average 2",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.pm25,
    }, "pm25_avg_24h_ch3": {
        MAP_NAME: "PM2.5 24h Average 3",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.pm25,
    }, "pm25_avg_24h_ch4": {
        MAP_NAME: "PM2.5 24h Average 4",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.pm25,
    }, "lightning_time": {
        MAP_NAME: "Last Lightning strike",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.timestamp,
    }, "lightning_num": {
        MAP_NAME: "Lightning strikes",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.count,
    }, "lightning": {
        MAP_NAME: "Lightning strike distance",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.distance_km,
    }, "lightning_mi": {
        MAP_NAME: "Lightning strike distance",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.distance_miles,
    }, "tf_co2": {
        MAP_NAME: "WH45 Temperature",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "tf_co2c": {
        MAP_NAME: "WH45 Temperature",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "humi_co2": {
        MAP_NAME: "WH45 Humidity",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.humidity,
    }, "pm25_co2": {
        MAP_NAME: "WH45 PM2.5 CO2",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.pm25,
    }, "pm25_24h_co2": {
        MAP_NAME: "WH45 PM2.5 CO2 24h average",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.pm25,
    }, "pm10_co2": {
        MAP_NAME: "WH45 PM10 CO2",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.pm10,
    }, "pm10_24h_co2": {
        MAP_NAME: "WH45 PM10 CO2 24h average",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.pm10,
    }, "co2": {
        MAP_NAME: "WH45 CO2",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.co2_ppm,
    }, "co2_24h": {
        MAP_NAME: "WH45 CO2 24h average",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.co2_ppm,
    }, "co2_batt": {
        MAP_NAME: "WH45 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.battery_percentage,
    }, "leak_ch1": {
        MAP_NAME: "Leak Detection 1",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.binary,
    }, "leak_ch2": {
        MAP_NAME: "Leak Detection 2",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.binary,
    }, "leak_ch3": {
        MAP_NAME: "Leak Detection 3",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.binary,
    }, "leak_ch4": {
        MAP_NAME: "Leak Detection 4",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.binary,
    }, "wh25batt": {
        MAP_NAME: "WH25 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.binary,
    }, "wh26batt": {
        MAP_NAME: "WH26 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.binary,
    }, "wh40batt": {
        MAP_NAME: "WH40 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.voltage,
    }, "wh57batt": {
        MAP_NAME: "WH57 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.battery_percentage,
    }, "wh65batt": {
        MAP_NAME: "WH65 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.binary,
    }, "wh68batt": {
        MAP_NAME: "WH68 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.voltage,
    }, "wh80batt": {
        MAP_NAME: "WH80 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.voltage,
    }, "soilbatt1": {
        MAP_NAME: "Soil Battery 1",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.voltage,
    }, "soilbatt2": {
        MAP_NAME: "Soil Battery 2",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.voltage,
    }, "soilbatt3": {
        MAP_NAME: "Soil Battery 3",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.voltage,
    }, "soilbatt4": {
        MAP_NAME: "Soil Battery 4",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.voltage,
    }, "soilbatt5": {
        MAP_NAME: "Soil Battery 5",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.voltage,
    }, "soilbatt6": {
        MAP_NAME: "Soil Battery 6",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.voltage,
    }, "soilbatt7": {
        MAP_NAME: "Soil Battery 7",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.voltage,
    }, "soilbatt8": {
        MAP_NAME: "Soil Battery 8",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.voltage,
    }, "batt1": {
        MAP_NAME: "Battery 1",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.binary,
    }, "batt2": {
        MAP_NAME: "Battery 2",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.binary,
    }, "batt3": {
        MAP_NAME: "Battery 3",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.binary,
    }, "batt4": {
        MAP_NAME: "Battery 4",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.binary,
    }, "batt5": {
        MAP_NAME: "Battery 5",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.binary,
    }, "batt6": {
        MAP_NAME: "Battery 6",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.binary,
    }, "batt7": {
        MAP_NAME: "Battery 7",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.binary,
    }, "batt8": {
        MAP_NAME: "Battery 8",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.binary,
    }, "pm25batt1": {
        MAP_NAME: "PM2.5 1 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.battery_percentage,
    }, "pm25batt2": {
        MAP_NAME: "PM2.5 2 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.battery_percentage,
    }, "pm25batt3": {
        MAP_NAME: "PM2.5 3 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.battery_percentage,
    }, "pm25batt4": {
        MAP_NAME: "PM2.5 4 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.battery_percentage,
    }, "pm25batt5": {
        MAP_NAME: "PM2.5 5 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.battery_percentage,
    }, "pm25batt6": {
        MAP_NAME: "PM2.5 6 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.battery_percentage,
    }, "pm25batt7": {
        MAP_NAME: "PM2.5 7 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.battery_percentage,
    }, "pm25batt8": {
        MAP_NAME: "PM2.5 8 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.battery_percentage,
    }, "leakbatt1": {
        MAP_NAME: "Leak Detection 1 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.battery_percentage,
    }, "leakbatt2": {
        MAP_NAME: "Leak Detection 2 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.battery_percentage,
    }, "leakbatt3": {
        MAP_NAME: "Leak Detection 3 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.battery_percentage,
    }, "leakbatt4": {
        MAP_NAME: "Leak Detection 4 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.battery_percentage,
    }, "leakbatt5": {
        MAP_NAME: "Leak Detection 5 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.battery_percentage,
    }, "leakbatt6": {
        MAP_NAME: "Leak Detection 6 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.battery_percentage,
    }, "leakbatt7": {
        MAP_NAME: "Leak Detection 7 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.battery_percentage,
    }, "leakbatt8": {
        MAP_NAME: "Leak Detection 8 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.battery_percentage,
    }, "tf_ch1c": {
        MAP_NAME: "Soil Temperature 1",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "tf_ch2c": {
        MAP_NAME: "Soil Temperature 2",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "tf_ch3c": {
        MAP_NAME: "Soil Temperature 3",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "tf_ch4c": {
        MAP_NAME: "Soil Temperature 4",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "tf_ch5c": {
        MAP_NAME: "Soil Temperature 5",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "tf_ch6c": {
        MAP_NAME: "Soil Temperature 6",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "tf_ch7c": {
        MAP_NAME: "Soil Temperature 7",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "tf_ch8c": {
        MAP_NAME: "Soil Temperature 8",
        MAP_SYSTEM: SYSTEM_METRIC,
        MAP_STYPE: EcoWittSensorTypes.temperature_c,
    }, "tf_ch1": {
        MAP_NAME: "Soil Temperature 1",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "tf_ch2": {
        MAP_NAME: "Soil Temperature 2",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "tf_ch3": {
        MAP_NAME: "Soil Temperature 3",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "tf_ch4": {
        MAP_NAME: "Soil Temperature 4",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "tf_ch5": {
        MAP_NAME: "Soil Temperature 5",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "tf_ch6": {
        MAP_NAME: "Soil Temperature 6",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "tf_ch7": {
        MAP_NAME: "Soil Temperature 7",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "tf_ch8": {
        MAP_NAME: "Soil Temperature 8",
        MAP_SYSTEM: SYSTEM_IMPERIAL,
        MAP_STYPE: EcoWittSensorTypes.temperature_f,
    }, "tf_batt1": {
        MAP_NAME: "Soil Temperature 1 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.voltage,
    }, "tf_batt2": {
        MAP_NAME: "Soil Temperature 2 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.voltage,
    }, "tf_batt3": {
        MAP_NAME: "Soil Temperature 3 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.voltage,
    }, "tf_batt4": {
        MAP_NAME: "Soil Temperature 4 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.voltage,
    }, "tf_batt5": {
        MAP_NAME: "Soil Temperature 5 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.voltage,
    }, "tf_batt6": {
        MAP_NAME: "Soil Temperature 6 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.voltage,
    }, "tf_batt7": {
        MAP_NAME: "Soil Temperature 7 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.voltage,
    }, "tf_batt8": {
        MAP_NAME: "Soil Temperature 8 Battery",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.voltage,
    }, "mac": {
        MAP_NAME: "macaddr",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.internal,
    }, "dateutc": {
        MAP_NAME: "dateutc",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.internal,
    }, "fields": {
        MAP_NAME: "field list",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.internal,
    }, "PASSKEY": {
        MAP_NAME: "passkey",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.internal,
    }, "stationtype": {
        MAP_NAME: "stationtype",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.internal,
    }, "freq": {
        MAP_NAME: "freq",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.internal,
    }, "model": {
        MAP_NAME: "model",
        MAP_SYSTEM: None,
        MAP_STYPE: EcoWittSensorTypes.internal,
    }
}
