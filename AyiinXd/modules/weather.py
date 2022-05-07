# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for getting the weather of a city. """

import json
from datetime import datetime

from pytz import country_names as c_n
from pytz import country_timezones as c_tz
from pytz import timezone as tz
from requests import get

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd import OPEN_WEATHER_MAP_APPID as OWM_API
from AyiinXd import WEATHER_DEFCITY
from AyiinXd.ayiin import ayiin_cmd, eor
from Stringyins import get_string

DEFCITY = WEATHER_DEFCITY or None


async def get_tz(con):
    """Get time zone of the given country."""
    """ Credits: @aragon12 and @zakaryan2004. """
    for c_code in c_n:
        if con == c_n[c_code]:
            return tz(c_tz[c_code][0])
    try:
        if c_n[con]:
            return tz(c_tz[con][0])
    except KeyError:
        return


@ayiin_cmd(pattern="weather(?: |$)(.*)")
async def get_weather(weather):
    if not OWM_API:
        return await weather.edit(get_string("weather_1")
        )
    xx = await eor(weather, get_string("com_1"))
    APPID = OWM_API
    anonymous = False
    if not weather.pattern_match.group(1):
        CITY = DEFCITY
    elif weather.pattern_match.group(1).lower() == "anon":
        CITY = DEFCITY
        anonymous = True
    else:
        CITY = weather.pattern_match.group(1)
    if not CITY:
        return await xx.edit(get_string("weather_2")
        )
    timezone_countries = {
        timezone: country
        for country, timezones in c_tz.items()
        for timezone in timezones
    }
    if "," in CITY:
        newcity = CITY.split(",")
        if len(newcity[1]) == 2:
            CITY = newcity[0].strip() + "," + newcity[1].strip()
        else:
            country = await get_tz((newcity[1].strip()).title())
            try:
                countrycode = timezone_countries[f"{country}"]
            except KeyError:
                return await weather.edit("`Invalid country.`")
            CITY = newcity[0].strip() + "," + countrycode.strip()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={APPID}"
    request = get(url)
    result = json.loads(request.text)
    if request.status_code != 200:
        return await weather.edit(get_string("weather_3"))
    cityname = result["name"]
    curtemp = result["main"]["temp"]
    humidity = result["main"]["humidity"]
    min_temp = result["main"]["temp_min"]
    max_temp = result["main"]["temp_max"]
    desc = result["weather"][0]
    desc = desc["main"]
    country = result["sys"]["country"]
    sunrise = result["sys"]["sunrise"]
    sunset = result["sys"]["sunset"]
    wind = result["wind"]["speed"]
    winddir = result["wind"]["deg"]
    ctimezone = tz(c_tz[country][0])
    time = datetime.now(ctimezone).strftime("%A, %I:%M %p")
    fullc_n = c_n[f"{country}"]
    dirs = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    div = 360 / len(dirs)
    funmath = int((winddir + (div / 2)) / div)
    findir = dirs[funmath % len(dirs)]
    kmph = str(wind * 3.6).split(".")
    mph = str(wind * 2.237).split(".")

    def fahrenheit(f):
        temp = str((f - 273.15) * 9 / 5 + 32).split(".")
        return temp[0]

    def celsius(c):
        temp = str(c - 273.15).split(".")
        return temp[0]

    def sun(unix):
        return datetime.fromtimestamp(unix, tz=ctimezone).strftime("%I:%M %p")

    results = get_string("weather_4").format(celsius(curtemp), fahrenheit(curtemp), celsius(min_temp), fahrenheit(min_temp), celsius(max_temp), fahrenheit(max_temp), humidity, kmph[0], mph[0], findir, sun(sunrise), sun(sunset), desc, time)
    if not anonymous:
        results += f"`{cityname}, {fullc_n}`"

    await weather.eor(results)


CMD_HELP.update(
    {
        "weather": f"**Plugin : **`weather`\
        \n\n  »  **Perintah :** `{cmd}weather` <city> or `{cmd}weather` <city>, <country name/code>\
        \n  »  **Kegunaan : **Untuk Mendapat informasi cuaca kota.\
        \n\n  »  **Perintah : **`{cmd}weather anon` \
        \n  »  **Kegunaan : **Untuk Mendapat informasi cuaca kota, dan menghilangkan detail lokasi di hasil. (Ini membutuhkan var WEATHER_DEFCITY untuk disetel)\
    "
    }
)
