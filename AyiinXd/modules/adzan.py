# ported from uniborg
# https://github.com/muhammedfurkan/UniBorg/blob/master/stdplugins/ezanvakti.py

import json

import requests

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.modules.sql_helper.globals import gvarstatus
from AyiinXd.ayiin import ayiin_cmd, eor
from Stringyins import get_string


@ayiin_cmd(pattern="adzan(?:\\s|$)([\\s\\S]*)")
async def get_adzan(adzan):
    "Shows you the Islamic prayer times of the given city name"
    input_str = adzan.pattern_match.group(1)
    LOKASI = gvarstatus(
        "WEATHER_DEFCITY") or "Jakarta" if not input_str else input_str
    url = f"http://muslimsalat.com/{LOKASI}.json?key=bd099c5825cbedb9aa934e255a81a5fc"
    request = requests.get(url)
    if request.status_code != 200:
        return await eor(adzan, get_string("adzan1").format(LOKASI), time=120
                               )
    result = json.loads(request.text)
    catresult = f"<b>Jadwal Shalat Hari Ini:</b>\
            \n<b>📆 Tanggal </b><code>{result['items'][0]['date_for']}</code>\
            \n<b>📍 Kota</b> <code>{result['query']}</code> | <code>{result['country']}</code>\
            \n\n<b>Terbit  : </b><code>{result['items'][0]['shurooq']}</code>\
            \n<b>Subuh : </b><code>{result['items'][0]['fajr']}</code>\
            \n<b>Zuhur  : </b><code>{result['items'][0]['dhuhr']}</code>\
            \n<b>Ashar  : </b><code>{result['items'][0]['asr']}</code>\
            \n<b>Maghrib : </b><code>{result['items'][0]['maghrib']}</code>\
            \n<b>Isya : </b><code>{result['items'][0]['isha']}</code>\
    "
    await eor(adzan, catresult, "html")


CMD_HELP.update(
    {
        "adzan": f"**Plugin : **`adzan`\
        \n\n  »  **Perintah :** `{cmd}adzan` <nama kota>\
        \n  »  **Kegunaan : **Menunjukkan waktu jadwal sholat dari kota yang diberikan.\
    "
    }
)
