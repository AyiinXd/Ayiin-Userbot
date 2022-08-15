# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# Ported by @mrismanaziz
# @SharingUserbot

import asyncio
import math
import time

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eod, extract_time
from Stringyins import get_string


@ayiin_cmd(
    pattern="f(typing|audio|contact|document|game|location|photo|round|sticker|video) ?(.*)"
)
async def _(e):
    act = e.pattern_match.group(1)
    t = e.pattern_match.group(2)
    if act in ["audio", "round", "video"]:
        act = "record-" + act
    if t.isdigit():
        t = int(t)
    elif t.endswith(("s", "h", "d", "m")):
        t = math.ceil((await extract_time(e, t)) - time.time())
    else:
        t = 60
    await eod(e, get_string("fake_1").format(act, t), time=3)
    async with e.client.action(e.chat_id, act):
        await asyncio.sleep(t)


CMD_HELP.update(
    {
        "fakeaction": f"**Plugin :** `fakeaction`\
        \n\n  »  **Perintah :** `{cmd}ftyping`  <jumlah detik>\
        \n  »  **Kegunaan :** Menampilkan Pengetikan Palsu dalam obrolan\
        \n\n  »  **Perintah :** `{cmd}faudio` <jumlah detik>\
        \n  »  **Kegunaan :** Menampilkan Tindakan Merekam suara Palsu dalam obrolan\
        \n\n  »  **Perintah :** `{cmd}fvideo` <jumlah detik>\
        \n  »  **Kegunaan :** Menampilkan Tindakan Merekam Video Palsu dalam obrolan\
        \n\n  »  **Perintah :** `{cmd}fround` <jumlah detik>\
        \n  »  **Kegunaan :** Menampilkan Tindakan Merekam Live Video Round Palsu dalam obrolan\
        \n\n  »  **Perintah :** `{cmd}fgame` <jumlah detik>\
        \n  »  **Kegunaan :** Menampilkan sedang bermain game Palsu dalam obrolan\
        \n\n  »  **Perintah :** `{cmd}fphoto` <jumlah detik>\
        \n  »  **Kegunaan :** Menampilkan Tindakan Mengirim Photo Palsu dalam obrolan\
        \n\n  »  **Perintah :** `{cmd}fdocument` <jumlah detik>\
        \n  »  **Kegunaan :** Menampilkan Tindakan Mengirim Document/File Palsu dalam obrolan\
        \n\n  »  **Perintah :** `{cmd}flocation` <jumlah detik>\
        \n  »  **Kegunaan :** Menampilkan Tindakan Share Lokasi Palsu dalam obrolan\
        \n\n  »  **Perintah :** `{cmd}fcontact` <jumlah detik>\
        \n  »  **Kegunaan :** Menampilkan Tindakan Share Contact Palsu dalam obrolan\
        \n\n  »  **Perintah :** `{cmd}fsticker` <jumlah detik>\
        \n  »  **Kegunaan :** Menampilkan Tindakan Memilih Sticker Palsu dalam obrolan\
    "
    }
)
