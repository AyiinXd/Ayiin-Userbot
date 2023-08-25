# credits: mrconfused
from geopy.geocoders import Nominatim
from telethon.tl import types

from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eor

from . import cmd


@ayiin_cmd(pattern="gps(?: |$)(.*)")
async def gps(event):
    if event.fwd_from:
        return
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    input_str = event.pattern_match.group(1)
    if not input_str:
        return await event.edit("**Berikan Tempat Yang ingin Dicari**")
    xx = await eor(event, "`Memproses...`")
    geolocator = Nominatim(user_agent="Yins")
    geoloc = geolocator.geocode(input_str)
    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await reply_to_id.edit(
            input_str, file=types.InputMediaGeoPoint(types.InputGeoPoint(lat, lon))
        )
        await xx.delete()
    else:
        await xx.edit("`Maaf Saya Tidak Dapat Menemukannya`")


CMD_HELP.update(
    {
        "gps": f"**Plugin : **`gps`\
        \n\n  »  **Perintah :** `{cmd}gps` <nama lokasi>\
        \n  »  **Kegunaan : **Untuk Mendapatkan Lokasi Map.\
    "
    }
)
