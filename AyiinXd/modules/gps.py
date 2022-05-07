# credits: mrconfused
from geopy.geocoders import Nominatim
from telethon.tl import types

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eor
from Stringyins import get_string


@ayiin_cmd(pattern="gps(?: |$)(.*)")
async def gps(event):
    if event.fwd_from:
        return
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    input_str = event.pattern_match.group(1)
    if not input_str:
        return await event.edit(get_string("gps_1"))
    xx = await eor(event, get_string("com_1"))
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
        await xx.edit(get_string("gps_2"))


CMD_HELP.update(
    {
        "gps": f"**Plugin : **`gps`\
        \n\n  »  **Perintah :** `{cmd}gps` <nama lokasi>\
        \n  »  **Kegunaan : **Untuk Mendapatkan Lokasi Map.\
    "
    }
)
