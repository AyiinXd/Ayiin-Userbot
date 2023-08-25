# Copyright (C) 2020  @deleteduser420 <https://github.com/code-rgb>
# ported by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

import os

import requests

from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eod, eor

from . import cmd, var


@ayiin_cmd(pattern="detect$")
async def detect(event):
    if var.DEEP_AI is None:
        return await eod(
            event,
            "**Tambahkan VAR** `DEEP_AI` **dan ambil Api Key di web https://deepai.org/**",
            time=120,
        )
    reply = await event.get_reply_message()
    if not reply:
        return await eod(event, "`Bales Ke Gambar/Sticker`", time=90)
    yinsevent = await eor(event, "**MenDownload file untuk diperiksa...**")
    media = await event.client.download_media(reply)
    if not media.endswith(("png", "jpg", "webp")):
        return await eod(event, "`Bales Ke Gambar/Sticker`", time=90)
    yinsevent = await eor(event, "**Mendeteksi batas NSFW...**")
    r = requests.post(
        "https://api.deepai.org/api/nsfw-detector",
        files={
            "image": open(media, "rb"),
        },
        headers={"api-key": var.DEEP_AI},
    )
    os.remove(media)
    if "status" in r.json():
        return await eod(yinsevent, r.json()["status"])
    r_json = r.json()["output"]
    pic_id = r.json()["id"]
    percentage = r_json["nsfw_score"] * 100
    detections = r_json["detections"]
    link = f"https://api.deepai.org/job-view-file/{pic_id}/inputs/image.jpg"
    result = f"<b>Detected Nudity :</b>\n<a href='{link}'>>>></a> <code>{percentage:.3f}%</code>\n\n"
    if detections:
        for parts in detections:
            name = parts["name"]
            confidence = int(float(parts["confidence"]) * 100)
            result += f"<b>• {name}:</b>\n   <code>{confidence} %</code>\n"
    await eor(
        yinsevent,
        result,
        link_preview=False,
        parse_mode="HTML",
    )


CMD_HELP.update(
    {
        "nsfw": f"**Plugin : **`nsfw`\
        \n\n  »  **Perintah :** `{cmd}detect` <reply media>\
        \n  »  **Kegunaan : **Untuk mendeteksi konten 18+ dengan gambar balasan.\
    "
    }
)
