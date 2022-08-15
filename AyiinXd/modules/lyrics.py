# Credits: @mrismanaziz
# API by @tofik_dn || https://github.com/tofikdn
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

import requests

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eor
from Stringyins import get_string


@ayiin_cmd(pattern="lyrics(?:\\s|$)([\\s\\S]*)")
async def _(event):
    query = event.pattern_match.group(1)
    if not query:
        return await eor(event, get_string("lyric_1"))
    try:
        xxnx = await eor(event, get_string("com_2"))
        respond = requests.get(
            f"https://api-tede.herokuapp.com/api/lirik?l={query}"
        ).json()
        result = f"{respond['data']}"
        await xxnx.edit(result)
    except Exception:
        await xxnx.edit(get_string("lyric_2"))


CMD_HELP.update(
    {
        "lyrics": f"**Plugin : **`lyrics`\
        \n\n  »  **Perintah :** `{cmd}lyrics` <judul lagu>\
        \n  »  **Kegunaan : **Dapatkan lirik lagu yang cocok dengan judul lagu.\
    "
    }
)
