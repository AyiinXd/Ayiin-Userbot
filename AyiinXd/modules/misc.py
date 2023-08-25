# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# You can find misc modules, which dont fit in anything xD
#
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
#

import io
import os
import re
import sys
import urllib
from os import environ, execle
from time import sleep

import requests
from bs4 import BeautifulSoup
from heroku3 import from_key
from PIL import Image

from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eor, time_formatter

from . import cmd, var


opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.70 Mobile Safari/537.36"
opener.addheaders = [("User-agent", useragent)]


@ayiin_cmd(pattern="sleep ([0-9]+)$", allow_sudo=False)
async def sleepybot(time):
    counter = int(time.pattern_match.group(1))
    xx = await eor(time, "`Saya mengantuk dan tertidur...`")
    if var.BOTLOG_CHATID:
        str_counter = time_formatter(counter)
        await time.client.send_message(
            var.BOTLOG_CHATID,
            f"**Anda menyuruh bot untuk tidur selama** {str_counter}."
        )
    sleep(counter)
    await xx.edit("**Oke, Saya siap membantu mu lagi**")


@ayiin_cmd(pattern="restart$", allow_sudo=False)
async def restart_bot(event):
    await eor(event, "**᯽ 𝙰𝚈𝙸𝙸𝙽-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ᯽ Berhasil di Restart**")
    if var.BOTLOG_CHATID:
        await event.client.send_message(
            var.BOTLOG_CHATID,
            "#RESTART \n**᯽ 𝙰𝚈𝙸𝙸𝙽-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ᯽ Berhasil Di Restart**"
        )
    args = [sys.executable, "-m", "AyiinXd"]
    execle(sys.executable, *args, environ)


@ayiin_cmd(pattern="repeat (.*)")
async def repeat(event):
    cnt, txt = event.pattern_match.group(1).split(" ", 1)
    replyCount = int(cnt)
    toBeRepeated = txt

    replyText = toBeRepeated + "\n"

    for _ in range(replyCount - 1):
        replyText += toBeRepeated + "\n"

    await eor(event, replyText)


@ayiin_cmd(pattern="raw$")
async def raw(event):
    the_real_message = None
    reply_to_id = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.stringify()
        reply_to_id = event.reply_to_msg_id
    else:
        the_real_message = event.stringify()
        reply_to_id = event.message.id
    with io.BytesIO(str.encode(the_real_message)) as out_file:
        out_file.name = "raw_message_data.txt"
        await eor(
            event,
            "`Periksa log userbot untuk data pesan yang didekodekan !!`"
        )
        await event.client.send_file(
            var.BOTLOG_CHATID,
            out_file,
            force_document=True,
            allow_cache=False,
            reply_to=reply_to_id,
            caption="**Inilah data pesan yang didecodekan !!**",
        )


@ayiin_cmd(pattern="reverse(?: |$)(\\d*)")
async def okgoogle(img):
    if os.path.isfile("okgoogle.png"):
        os.remove("okgoogle.png")
    message = await img.get_reply_message()
    if message and message.media:
        photo = io.BytesIO()
        await img.client.download_media(message, photo)
    else:
        return await eor(img, "`Bales Ke Gambar/Sticker`")
    if photo:
        xx = await eor(img, "**Memproses...**")
        try:
            image = Image.open(photo)
        except OSError:
            await xx.edit("`Media Tidak Didukung..`")
            return
        name = "okgoogle.png"
        image.save(name, "PNG")
        image.close()
        # https://stackoverflow.com/questions/23270175/google-reverse-image-search-using-post-request#28792943
        searchUrl = "https://www.google.com/searchbyimage/upload"
        multipart = {
            "encoded_image": (
                name,
                open(
                    name,
                    "rb")),
            "image_content": ""}
        response = requests.post(
            searchUrl,
            files=multipart,
            allow_redirects=False)
        fetchUrl = response.headers["Location"]
        if response != 400:
            await xx.edit(
                "`Gambar berhasil diunggah ke Google. Mungkin.`\n`Mengurai sumber sekarang. Mungkin.`"
            )
        else:
            return await xx.edit("**Google menyuruhku pergi.**")
        os.remove(name)
        match = await ParseSauce(fetchUrl + "&preferences?hl=en&fg=1#languages")
        guess = match["best_guess"]
        imgspage = match["similar_images"]
        if guess and imgspage:
            await xx.edit(f"[{guess}]({fetchUrl})\n\n`Mencari gambar...`")
        else:
            await xx.edit("**Tidak dapat menemukan apa pun.**")
            return
        lim = img.pattern_match.group(1) or 3
        images = await scam(match, lim)
        yeet = []
        for i in images:
            k = requests.get(i)
            yeet.append(k.content)
        try:
            await img.client.send_file(
                entity=await img.client.get_input_entity(img.chat_id),
                file=yeet,
                reply_to=img,
            )
        except TypeError:
            pass
        await xx.edit(f"[{guess}]({fetchUrl})\n\n[Gambar yang mirip secara visual]({imgspage})"
        )


async def ParseSauce(googleurl):
    source = opener.open(googleurl).read()
    soup = BeautifulSoup(source, "html.parser")
    results = {"similar_images": "", "best_guess": ""}
    try:
        for similar_image in soup.findAll("input", {"class": "gLFyf"}):
            url = "https://www.google.com/search?tbm=isch&q=" + \
                urllib.parse.quote_plus(similar_image.get("value"))
            results["similar_images"] = url
    except BaseException:
        pass
    for best_guess in soup.findAll("div", attrs={"class": "r5a77d"}):
        results["best_guess"] = best_guess.get_text()
    return results


async def scam(results, lim):
    single = opener.open(results["similar_images"]).read()
    decoded = single.decode("utf-8")
    imglinks = []
    counter = 0
    pattern = r"^,\[\"(.*[.png|.jpg|.jpeg])\",[0-9]+,[0-9]+\]$"
    oboi = re.findall(pattern, decoded, re.I | re.M)
    for imglink in oboi:
        counter += 1
        if counter < int(lim):
            imglinks.append(imglink)
        else:
            break
    return imglinks


@ayiin_cmd(pattern="send (.*)")
async def send(event):
    if not event.is_reply:
        return await eor(
            event,
            "**Mohon Balas ke pesan yang ingin dikirim!**"
        )
    chat = event.pattern_match.group(1)
    xx = await eor(event, "**Berhasil Mengirim pesan ini**")
    try:
        chat = int(chat)
    except ValueError:
        pass
    try:
        chat = await event.client.get_entity(chat)
    except (TypeError, ValueError):
        return await xx.edit("**Link yang diberikan tidak valid!**")
    message = await event.get_reply_message()
    await event.client.send_message(entity=chat, message=message)
    await xx.edit(f"**Berhasil Mengirim pesan ini ke** `{chat.title}`")


CMD_HELP.update(
    {
        "send": f"**Plugin : **`send`\
        \n\n  »  **Perintah :** `{cmd}send` <username/id>\
        \n  »  **Kegunaan : **Meneruskan pesan balasan ke obrolan tertentu tanpa tag Forwarded from. Bisa mengirim ke Group Chat atau ke Personal Message\
    "
    }
)

CMD_HELP.update(
    {
        "random": f"**Plugin : **`random`\
        \n\n  »  **Perintah :** `{cmd}random`\
        \n  »  **Kegunaan : **Dapatkan item acak dari daftar item. \
    "
    }
)

CMD_HELP.update(
    {
        "sleep": f"**Plugin : **`sleep`\
        \n\n  »  **Perintah :** `{cmd}sleep`\
        \n  »  **Kegunaan : **Biarkan Ayiin-Userbot tidur selama beberapa detik \
    "
    }
)


CMD_HELP.update(
    {
        "restart": f"**Plugin : **`Restart Ayiin-Userbot`\
        \n\n  »  **Perintah :** `{cmd}restart`\
        \n  »  **Kegunaan : **Untuk Merestart userbot.\
    "
    }
)


CMD_HELP.update(
    {
        "raw": f"**Plugin : **`raw`\
        \n\n  »  **Perintah :** `{cmd}raw`\
        \n  »  **Kegunaan : **Dapatkan data berformat seperti JSON terperinci tentang pesan yang dibalas.\
    "
    }
)


CMD_HELP.update(
    {
        "repeat": f"**Plugin : **`repeat`\
        \n\n  »  **Perintah :** `{cmd}repeat`\
        \n  »  **Kegunaan : **Mengulangi teks untuk beberapa kali. Jangan bingung ini dengan spam tho.\
    "
    }
)
