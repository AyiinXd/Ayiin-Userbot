# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# Ported by @AyiinXd
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


import asyncio
import os

import cv2
import numpy as np

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from Stringyins import get_string


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


@ayiin_cmd(pattern=r"sketch(?: |$)(.*)")
async def sketch(e):
    ureply = await e.get_reply_message()
    xx = await eor(e, get_string("com_1"))
    if not (ureply and (ureply.media)):
        return await eod(xx, get_string("failed9"))

    yins = await ureply.download_media()
    if yins.endswith(".tgs"):
        await xx.edit(get_string("com_1"))
        cmd = ["lottie_convert.py", yins, "ayiin.png"]
        file = "ayiin.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await xx.edit(get_string("yimg_1"))
        img = cv2.VideoCapture(yins)
        heh, lol = img.read()
        cv2.imwrite("ayiin.png", lol)
        file = "ayiin.png"
    img = cv2.imread(file)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted_gray_image = 255 - gray_image
    blurred_img = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)
    inverted_blurred_img = 255 - blurred_img
    pencil_sketch_IMG = cv2.divide(
        gray_image, inverted_blurred_img, scale=256.0)
    cv2.imwrite("ayiinxd.png", pencil_sketch_IMG)
    await xx.respond(get_string("yimg_3"), file="ayiinxd.png")
    await xx.delete()
    os.remove(file)
    os.remove("ayiinxd.png")


@ayiin_cmd(pattern=r"grey(?: |$)(.*)")
async def xnxx(event):
    ureply = await event.get_reply_message()
    yins = await eor(event, get_string("com_1"))
    if not (ureply and (ureply.media)):
        return await eod(yins, get_string("failed9"))

    ayiin = await ureply.download_media()
    if ayiin.endswith(".tgs"):
        await yins.edit(get_string("com_1"))
        cmd = ["lottie_convert.py", ayiin, "yin.png"]
        file = "yin.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await yins.edit(get_string("yimg_1"))
        img = cv2.VideoCapture(ayiin)
        heh, lol = img.read()
        cv2.imwrite("yin.png", lol)
        file = "yin.png"
    yin = cv2.imread(file)
    ayiinxd = cv2.cvtColor(yin, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("yin.jpg", ayiinxd)
    await event.client.send_file(
        event.chat_id,
        "yin.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await yins.delete()
    os.remove("yin.png")
    os.remove("yin.jpg")
    os.remove(ayiin)


@ayiin_cmd(pattern=r"blur(?: |$)(.*)")
async def ayiin(event):
    ureply = await event.get_reply_message()
    xd = await eor(event, get_string("com_1"))
    if not (ureply and (ureply.media)):
        return await eod(xd, get_string("failed9"))

    yins = await ureply.download_media()
    if yins.endswith(".tgs"):
        await xd.edit(get_string("com_1"))
        cmd = ["lottie_convert.py", yins, "yin.png"]
        file = "yin.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await xd.edit(get_string("yimg_1"))
        img = cv2.VideoCapture(yins)
        heh, lol = img.read()
        cv2.imwrite("yin.png", lol)
        file = "yin.png"
    yin = cv2.imread(file)
    ayiinxd = cv2.GaussianBlur(yin, (35, 35), 0)
    cv2.imwrite("yin.jpg", ayiinxd)
    await event.client.send_file(
        event.chat_id,
        "yin.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await xd.delete()
    for i in ["yin.png", "yin.jpg", yins]:
        if os.path.exists(i):
            os.remove(i)


@ayiin_cmd(pattern=r"negative(?: |$)(.*)")
async def yinsxd(event):
    ureply = await event.get_reply_message()
    ayiin = await eor(event, get_string("com_1"))
    if not (ureply and (ureply.media)):
        return await eod(ayiin, get_string("failed9"))

    ayiinxd = await ureply.download_media()
    if ayiinxd.endswith(".tgs"):
        await ayiin.edit(get_string("com_1"))
        cmd = ["lottie_convert.py", ayiinxd, "yin.png"]
        file = "yin.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await ayiin.edit(get_string("yimg_1"))
        img = cv2.VideoCapture(ayiinxd)
        heh, lol = img.read()
        cv2.imwrite("yin.png", lol)
        file = "yin.png"
    yinsex = cv2.imread(file)
    kntlxd = cv2.bitwise_not(yinsex)
    cv2.imwrite("yin.jpg", kntlxd)
    await event.client.send_file(
        event.chat_id,
        "yin.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await ayiin.delete()
    os.remove("yin.png")
    os.remove("yin.jpg")
    os.remove(kntlxd)


@ayiin_cmd(pattern=r"miror(?: |$)(.*)")
async def kntl(event):
    ureply = await event.get_reply_message()
    kentu = await eor(event, get_string("com_1"))
    if not (ureply and (ureply.media)):
        return await eod(kentu, get_string("failed9"))

    xnxx = await ureply.download_media()
    if xnxx.endswith(".tgs"):
        await kentu.edit(get_string("com_1"))
        cmd = ["lottie_convert.py", xnxx, "yin.png"]
        file = "yin.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await kentu.edit(get_string("yimg_1"))
        img = cv2.VideoCapture(xnxx)
        kont, tol = img.read()
        cv2.imwrite("yin.png", tol)
        file = "yin.png"
    yin = cv2.imread(file)
    mmk = cv2.flip(yin, 1)
    ayiinxd = cv2.hconcat([yin, mmk])
    cv2.imwrite("yin.jpg", ayiinxd)
    await event.client.send_file(
        event.chat_id,
        "yin.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await kentu.delete()
    os.remove("yin.png")
    os.remove("yin.jpg")
    os.remove(xnxx)


@ayiin_cmd(pattern=r"flp(?: |$)(.*)")
async def ayiin(kontol):
    ureply = await kontol.get_reply_message()
    mmk = await eor(kontol, get_string("com_1"))
    if not (ureply and (ureply.media)):
        return await eod(mmk, get_string("failed9"))

    ayiinxd = await ureply.download_media()
    if ayiinxd.endswith(".tgs"):
        await mmk.edit(get_string("com_1"))
        cmd = ["lottie_convert.py", ayiinxd, "yins.png"]
        file = "yins.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await mmk.edit(get_string("yimg_1"))
        img = cv2.VideoCapture(ayiinxd)
        kon, tol = img.read()
        cv2.imwrite("yins.png", tol)
        file = "yins.png"
    ayin = cv2.imread(file)
    trn = cv2.flip(ayin, 1)
    asu = cv2.rotate(trn, cv2.ROTATE_180)
    yinz = cv2.vconcat([ayin, asu])
    cv2.imwrite("yins.jpg", yinz)
    await kontol.client.send_file(
        kontol.chat_id,
        "yins.jpg",
        force_document=False,
        reply_to=kontol.reply_to_msg_id,
    )
    await mmk.delete()
    os.remove("yins.png")
    os.remove("yins.jpg")
    os.remove(ayiinxd)


@ayiin_cmd(pattern=r"quad(?: |$)(.*)")
async def ayiin(memek):
    ureply = await memek.get_reply_message()
    kntl = await eor(memek, get_string("com_1"))
    if not (ureply and (ureply.media)):
        return await eod(kntl, get_string("failed9"))

    yinsex = await ureply.download_media()
    if yinsex.endswith(".tgs"):
        await kntl.edit(get_string("com_1"))
        cmd = ["lottie_convert.py", yinsex, "yins.png"]
        file = "yins.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await kntl.edit(get_string("yimg_1"))
        img = cv2.VideoCapture(yinsex)
        kon, tol = img.read()
        cv2.imwrite("yins.png", tol)
        file = "yins.png"
    ayin = cv2.imread(file)
    xnxx = cv2.flip(ayin, 1)
    mici = cv2.hconcat([ayin, xnxx])
    fr = cv2.flip(mici, 1)
    trn = cv2.rotate(fr, cv2.ROTATE_180)
    ayiinxd = cv2.vconcat([mici, trn])
    cv2.imwrite("yins.jpg", ayiinxd)
    await memek.client.send_file(
        memek.chat_id,
        "yins.jpg",
        force_document=False,
        reply_to=memek.reply_to_msg_id,
    )
    await kntl.delete()
    os.remove("yins.png")
    os.remove("yins.jpg")
    os.remove(yinsex)


@ayiin_cmd(pattern=r"toon(?: |$)(.*)")
async def yins(event):
    ureply = await event.get_reply_message()
    xd = await eor(event, get_string("com_1"))
    if not (ureply and (ureply.media)):
        return await eod(xd, get_string("failed9"))

    yinsex = await ureply.download_media()
    if yinsex.endswith(".tgs"):
        await xd.edit(get_string("com_1"))
        cmd = ["lottie_convert.py", yinsex, "yins.png"]
        file = "yins.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await xd.edit(get_string("yimg_1"))
        img = cv2.VideoCapture(yinsex)
        kon, tol = img.read()
        cv2.imwrite("yins.png", tol)
        file = "yins.png"
    yins = cv2.imread(file)
    height, width, channels = yins.shape
    samples = np.zeros([height * width, 3], dtype=np.float32)
    count = 0
    for x in range(height):
        for y in range(width):
            samples[count] = yins[x][y]
            count += 1
    compactness, labels, centers = cv2.kmeans(
        samples,
        12,
        None,
        (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10000, 0.0001),
        5,
        cv2.KMEANS_PP_CENTERS,
    )
    centers = np.uint8(centers)
    asu = centers[labels.flatten()]
    ayiinxd = asu.reshape(yins.shape)
    cv2.imwrite("yins.jpg", ayiinxd)
    await event.client.send_file(
        event.chat_id,
        "yins.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await xd.delete()
    os.remove("yins.png")
    os.remove("yins.jpg")
    os.remove(yinsex)


@ayiin_cmd(pattern=r"danger(?: |$)(.*)")
async def ayiin(event):
    ureply = await event.get_reply_message()
    ayiin = await eor(ayiin, get_string("com_1"))
    if not (ureply and (ureply.media)):
        return await eod(ayiin, get_string("failed9"))

    ayiinxd = await ureply.download_media()
    if ayiinxd.endswith(".tgs"):
        await ayiin.edit(get_string("com_1"))
        cmd = ["lottie_convert.py", ayiinxd, "yins.png"]
        file = "yins.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await ayiin.edit(get_string("yimg_1"))
        img = cv2.VideoCapture(ayiinxd)
        kon, tol = img.read()
        cv2.imwrite("yins.png", tol)
        file = "yins.png"
    yins = cv2.imread(file)
    dan = cv2.cvtColor(yins, cv2.COLOR_BGR2RGB)
    kontol = cv2.cvtColor(dan, cv2.COLOR_HSV2BGR)
    cv2.imwrite("yins.jpg", kontol)
    await event.client.send_file(
        event.chat_id,
        "yins.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await ayiin.delete()
    os.remove("yins.png")
    os.remove("yins.jpg")
    os.remove(ayiinxd)


@ayiin_cmd(pattern=r"border(?: |$)(.*)")
async def ayiixd(event):
    mmk = await event.get_reply_message()
    if not (mmk and (mmk.photo or mmk.sticker)):
        return await eod(event, get_string("failed9"))
    kntl = event.pattern_match.group(1).strip()
    wh = 20
    if not kntl:
        kntl = [255, 255, 255]
    else:
        try:
            if ";" in kntl:
                col_ = kntl.split(";", maxsplit=1)
                wh = int(col_[1])
                kntl = col_[0]
            kntl = [int(kntl) for kntl in kntl.split(",")[:2]]
        except ValueError:
            return await eod(event, get_string("yimg_2"))
    yups = await mmk.download_media()
    img1 = cv2.imread(yups)
    constant = cv2.copyMakeBorder(
        img1, wh, wh, wh, wh, cv2.BORDER_CONSTANT, value=kntl)
    cv2.imwrite("output.png", constant)
    await event.client.send_file(event.chat.id, "output.png")
    os.remove("output.png")
    os.remove(yups)
    await event.delete()


@ayiin_cmd(pattern=r"pixelator(?: |$)(.*)")
async def pixelator(event):
    reply_message = await event.get_reply_message()
    if not (reply_message and reply_message.photo):
        return await eod(event, get_string("failed9"))
    hw = 50
    try:
        hw = int(event.pattern_match.group(1).strip())
    except (ValueError, TypeError):
        pass
    yins = await eor(event, get_string("com_1"))
    imayiin = await reply_message.download_media()
    input_ = cv2.imread(imayiin)
    height, width = input_.shape[:2]
    w, h = (hw, hw)
    temp = cv2.resize(input_, (w, h), interpolation=cv2.INTER_LINEAR)
    output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
    cv2.imwrite("output.jpg", output)
    await yins.respond(get_string("yimg_4"), file="output.jpg")
    await yins.delete()
    os.remove("output.jpg")
    os.remove(imayiin)


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "yinsimg": f"**Plugin : **`yinsimg`\
        \n\n  »  **Perintah :** `{cmd}sketch` <reply ke Foto/Sticker>\
        \n  »  **Kegunaan :** Coba Dulu Tod.\
        \n\n  »  **Perintah :** `{cmd}grey` <reply ke Foto/Sticker>\
        \n  »  **Kegunaan :** Coba Dulu Tod.\
        \n\n  »  **Perintah :** `{cmd}blur` <reply ke Foto/Sticker>\
        \n  »  **Kegunaan :** Coba Dulu Tod.\
        \n\n  »  **Perintah :** `{cmd}negative` <reply ke Foto/Sticker>\
        \n  »  **Kegunaan :** Coba Dulu Tod.\
        \n\n  »  **Perintah :** `{cmd}miror` <reply ke Foto/Sticker>\
        \n  »  **Kegunaan :** Coba Dulu Tod.\
        \n\n  »  **Perintah :** `{cmd}flp` <reply ke Foto/Sticker>\
        \n  »  **Kegunaan :** Coba Dulu Tod.\
        \n\n  »  **Perintah :** `{cmd}quad` <reply ke Foto/Sticker>\
        \n  »  **Kegunaan :** Coba Dulu Tod.\
        \n\n  »  **Perintah :** `{cmd}toon` <reply ke Foto/Sticker>\
        \n  »  **Kegunaan :** Coba Dulu Tod.\
        \n\n  »  **Perintah :** `{cmd}danger` <reply ke Foto/Sticker>\
        \n  »  **Kegunaan :** Coba Dulu Tod.\
        \n\n  »  **Perintah :** `{cmd}border` <reply ke Foto/Sticker>\
        \n  »  **Kegunaan :** Coba Dulu Tod.\
        \n\n  »  **Perintah :** `{cmd}pixelator` <reply ke Foto/Sticker>\
        \n  »  **Kegunaan :** Coba Dulu Tod.\
    "
    }
)
