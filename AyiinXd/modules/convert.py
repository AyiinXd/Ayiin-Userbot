# Copyright (C) 2020 Yusuf Usta.
#
# Licensed under the  GPL-3.0 License;
# you may not use this file except in compliance with the License.
#
# Ported by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
#

import asyncio
import io
import os

from PIL import Image

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import eod, eor
from AyiinXd.ayiin import ayiin_cmd, runcmd
from Stringyins import get_string


@ayiin_cmd(pattern="convert ?(foto|audio|gif|voice|photo|mp3)? ?(.*)")
async def cevir(event):
    botyins = event.pattern_match.group(1)
    try:
        if len(botyins) < 1:
            await eod(event, get_string("cvt_9").format(cmd),
                      time=30,
                      )
            return
    except BaseException:
        await eod(event, get_string("cvt_9").format(cmd),
                  time=30,
                  )
        return
    if botyins in ["foto", "photo"]:
        rep_msg = await event.get_reply_message()
        if not event.is_reply or not rep_msg.sticker:
            await eod(event, get_string("cvt_8"))
            return
        xxnx = await eor(event, get_string("cvt_2"))
        foto = io.BytesIO()
        foto = await event.client.download_media(rep_msg.sticker, foto)
        im = Image.open(foto).convert("RGB")
        im.save("sticker.png", "png")
        await event.client.send_file(
            event.chat_id,
            "sticker.png",
            reply_to=rep_msg,
        )
        await xxnx.delete()
        os.remove("sticker.png")
    elif botyins in ["sound", "audio"]:
        EFEKTLER = ["bengek", "robot", "jedug", "fast", "echo"]
        efekt = event.pattern_match.group(2)
        if len(efekt) < 1:
            return await eod(
                event, get_string("cvt_6"),
                time=30,
            )
        rep_msg = await event.get_reply_message()
        if not event.is_reply or not (rep_msg.voice or rep_msg.audio):
            return await eod(event, get_string("cvt_7"))
        xxx = await eor(event, get_string("cvt_3"))
        if efekt in EFEKTLER:
            indir = await rep_msg.download_media()
            KOMUT = {
                "bengek": '-filter_complex "rubberband=pitch=1.5"',
                "robot": "-filter_complex \"afftfilt=real='hypot(re,im)*sin(0)':imag='hypot(re,im)*cos(0)':win_size=512:overlap=0.75\"",
                "jedug": '-filter_complex "acrusher=level_in=8:level_out=18:bits=8:mode=log:aa=1"',
                "fast": "-filter_complex \"afftfilt=real='hypot(re,im)*cos((random(0)*2-1)*2*3.14)':imag='hypot(re,im)*sin((random(1)*2-1)*2*3.14)':win_size=128:overlap=0.8\"",
                "echo": '-filter_complex "aecho=0.8:0.9:500|1000:0.2|0.1"',
            }
            ses = await asyncio.create_subprocess_shell(
                f"ffmpeg -i '{indir}' {KOMUT[efekt]} output.mp3"
            )
            await ses.communicate()
            await event.client.send_file(
                event.chat_id,
                "output.mp3",
                thumb="AyiinXd/resources/logo.jpg",
                reply_to=rep_msg,
            )
            await xxx.delete()
            os.remove(indir)
            os.remove("output.mp3")
        else:
            await xxx.edit(get_string("cvt_6")
                           )
    elif botyins == "mp3":
        rep_msg = await event.get_reply_message()
        if not event.is_reply or not rep_msg.video:
            return await eod(event, get_string("cvt_10"))
        xx = await eor(event, get_string("cvt_1"))
        video = io.BytesIO()
        video = await event.client.download_media(rep_msg.video)
        gif = await asyncio.create_subprocess_shell(
            f"ffmpeg -y -i '{video}' -vn -b:a 128k -c:a libmp3lame out.mp3"
        )
        await gif.communicate()
        await xx.edit(get_string("com_6"))
        try:
            await event.client.send_file(
                event.chat_id,
                "out.mp3",
                thumb="AyiinXd/resources/logo.jpg",
                reply_to=rep_msg,
            )
        except BaseException:
            os.remove(video)
            return await xx.edit(get_string("cvt_11"))
        await xx.delete()
        os.remove("out.mp3")
        os.remove(video)
    else:
        await xx.edit(get_string("cvt_9")
                      )
        return


@ayiin_cmd(pattern="makevoice$")
async def makevoice(event):
    if not event.reply_to:
        return await eod(event, get_string("cvt_13"))
    msg = await event.get_reply_message()
    if not event.is_reply or not (msg.audio or msg.video):
        return await eod(event, get_string("cvt_13"))
    xxnx = await eor(event, get_string("com_1"))
    dl = msg.file.name
    file = await msg.download_media(dl)
    await xxnx.edit(get_string("cvt_12"))
    await runcmd(
        f"ffmpeg -i '{file}' -map 0:a -codec:a libopus -b:a 100k -vbr on yins.opus"
    )
    await event.client.send_message(
        event.chat_id, file="yins.opus", force_document=False, reply_to=msg
    )
    await xxnx.delete()
    os.remove(file)
    os.remove("yins.opus")


CMD_HELP.update(
    {
        "convert": f"**Plugin : **`core`\
        \n\n  »  **Perintah :** `{cmd}convert foto`\
        \n  »  **Kegunaan : **Untuk Mengconvert sticker ke foto\
        \n\n  »  **Perintah :** `{cmd}convert mp3`\
        \n  »  **Kegunaan : **Untuk Mengconvert dari video ke file mp3\
        \n\n  »  **Perintah :** `{cmd}makevoice`\
        \n  »  **Kegunaan : **Untuk Mengconvert audio ke voice note\
        \n\n  »  **Perintah :** `{cmd}convert audio` <efek>\
        \n  »  **Kegunaan : **Untuk Menambahkan efek suara jadi berskin\
        \n  •  **List Efek :** `bengek`, `jedug`, `echo`, `robot`\
    "
    }
)
