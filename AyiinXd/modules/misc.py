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

from AyiinXd import BOTLOG_CHATID
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, HEROKU_API_KEY, HEROKU_APP_NAME
from AyiinXd.ayiin import ayiin_cmd, eor, time_formatter
from Stringyins import get_string

# ================= CONSTANT =================
if HEROKU_APP_NAME is not None and HEROKU_API_KEY is not None:
    HEROKU_APP = from_key(HEROKU_API_KEY).apps()[HEROKU_APP_NAME]
else:
    HEROKU_APP = None
# ============================================

opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.70 Mobile Safari/537.36"
opener.addheaders = [("User-agent", useragent)]


@ayiin_cmd(pattern="sleep ([0-9]+)$", allow_sudo=False)
async def sleepybot(time):
    counter = int(time.pattern_match.group(1))
    xx = await eor(time, get_string("slbt_1"))
    if BOTLOG_CHATID:
        str_counter = time_formatter(counter)
        await time.client.send_message(
            BOTLOG_CHATID, get_string("slbt_2").format(str_counter)
        )
    sleep(counter)
    await xx.edit(get_string("slbt_3"))


@ayiin_cmd(pattern="shutdown$", allow_sudo=False)
async def shutdown_bot(event):
    if event.fwd_from:
        return
    if BOTLOG_CHATID:
        await event.client.send_message(
            BOTLOG_CHATID, get_string("shtdwn_1")
        )
    await eor(event, get_string("shtdwn_2"))
    if HEROKU_APP is not None:
        HEROKU_APP.process_formation()["worker"].scale(0)
    else:
        sys.exit(0)


@ayiin_cmd(pattern="restart$", allow_sudo=False)
async def restart_bot(event):
    await eor(event, get_string("rstrt_1"))
    if BOTLOG_CHATID:
        await event.client.send_message(
            BOTLOG_CHATID, get_string("rstrt_2")
        )
    args = [sys.executable, "-m", "AyiinXd"]
    execle(sys.executable, *args, environ)


@ayiin_cmd(pattern="readme$")
async def reedme(event):
    await eor(
        event, get_string("rdme_1")
    )


@ayiin_cmd(pattern="repeat (.*)")
async def repeat(event):
    cnt, txt = event.pattern_match.group(1).split(" ", 1)
    replyCount = int(cnt)
    toBeRepeated = txt

    replyText = toBeRepeated + "\n"

    for _ in range(replyCount - 1):
        replyText += toBeRepeated + "\n"

    await eor(event, replyText)


@ayiin_cmd(pattern="repo$")
async def repo_is_here(event):
    ayiin = await eor(event, "🤖")
    sleep(3)
    await ayiin.edit(get_string("repo_1")
    )


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
            event, get_string("raw_1")
        )
        await event.client.send_file(
            BOTLOG_CHATID,
            out_file,
            force_document=True,
            allow_cache=False,
            reply_to=reply_to_id,
            caption=get_string("raw_2"),
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
        return await eor(img, get_string("failed9"))
    if photo:
        xx = await eor(img, get_string("com_1"))
        try:
            image = Image.open(photo)
        except OSError:
            await xx.edit(get_string("com_4"))
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
            await xx.edit(get_string("rvrse_1")
            )
        else:
            return await xx.edit(get_string("rvrse_2"))
        os.remove(name)
        match = await ParseSauce(fetchUrl + "&preferences?hl=en&fg=1#languages")
        guess = match["best_guess"]
        imgspage = match["similar_images"]
        if guess and imgspage:
            await xx.edit(get_string("rvrse_3").format(guess, fetchUrl))
        else:
            await xx.edit(get_string("rvrse_4"))
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
        await xx.edit(get_string("rvrse_5").format(guess, fetchUrl, imgspage)
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
            event, get_string("send_1")
        )
    chat = event.pattern_match.group(1)
    xx = await eor(event, get_string("send_2"))
    try:
        chat = int(chat)
    except ValueError:
        pass
    try:
        chat = await event.client.get_entity(chat)
    except (TypeError, ValueError):
        return await xx.edit(get_string("send_3"))
    message = await event.get_reply_message()
    await event.client.send_message(entity=chat, message=message)
    await xx.edit(get_string("send_4").format(chat.title))


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
        "repo": f"**Plugin : **`Repository Ayiin-Userbot`\
        \n\n  »  **Perintah :** `{cmd}repo`\
        \n  »  **Kegunaan : **Menampilan link Repository Ayiin-Userbot\
        \n\n  »  **Perintah :** `{cmd}string`\
        \n  »  **Kegunaan : **Menampilan link String Ayiin-Userbot\
    "
    }
)


CMD_HELP.update(
    {
        "readme": f"**Plugin : **`Panduan Menggunakan userbot`\
        \n\n  »  **Perintah :** `{cmd}readme`\
        \n  »  **Kegunaan : **Menyediakan tautan untuk mengatur userbot dan modulnya\
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
        "shutdown": f"**Plugin : **`shutdown`\
        \n\n  »  **Perintah :** `{cmd}shutdown`\
        \n  »  **Kegunaan : **Mematikan Userbot.\
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
