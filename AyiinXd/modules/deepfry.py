# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

# Original source for the deepfrying code (used under the following
# license): https://github.com/Ovyerus/deeppyer

# MIT License
#
# Copyright (c) 2017 Ovyerus
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# Ported from Xtra-telegram by @heyworld
""" Userbot module for frying stuff. ported by @NeoMatrix90 """

import io
from random import randint, uniform

from PIL import Image, ImageEnhance, ImageOps

from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from AyiinXd.ayiin import check_media

from . import cmd


@ayiin_cmd(pattern="deepfry(?: |$)(.*)")
async def deepfryer(event):
    try:
        frycount = int(event.pattern_match.group(1))
        if frycount < 1:
            raise ValueError
    except ValueError:
        frycount = 1
    if event.is_reply:
        reply_message = await event.get_reply_message()
        data = await check_media(reply_message)
        if isinstance(data, bool):
            return await eod(event, "`Saya tidak bisa menggoreng itu!`")
    else:
        return await eod(
            event,
            "`Balas gambar atau stiker untuk menggorengnya!`"
        )
    # download last photo (highres) as byte array
    xx = await eor(event, "`Mengunduh...`")
    image = io.BytesIO()
    await event.client.download_media(data, image)
    image = Image.open(image)
    # fry the image
    await xx.edit("`Media penggorengan…`")
    for _ in range(frycount):
        image = await deepfry(image)
    fried_io = io.BytesIO()
    fried_io.name = "image.jpeg"
    image.save(fried_io, "JPEG")
    fried_io.seek(0)
    await xx.delete()
    await event.send_file(event.chat_id, file=fried_io, reply_to=event.reply_to_msg_id)


async def deepfry(img: Image) -> Image:
    colours = (
        (randint(50, 200), randint(40, 170), randint(40, 190)),
        (randint(190, 255), randint(170, 240), randint(180, 250)),
    )

    img = img.copy().convert("RGB")

    # Crush image to hell and back
    img = img.convert("RGB")
    width, height = img.width, img.height
    img = img.resize(
        (int(width ** uniform(0.8, 0.9)), int(height ** uniform(0.8, 0.9))),
        resample=Image.LANCZOS,
    )
    img = img.resize(
        (int(width ** uniform(0.85, 0.95)), int(height ** uniform(0.85, 0.95))),
        resample=Image.BILINEAR,
    )
    img = img.resize(
        (int(width ** uniform(0.89, 0.98)), int(height ** uniform(0.89, 0.98))),
        resample=Image.BICUBIC,
    )
    img = img.resize((width, height), resample=Image.BICUBIC)
    img = ImageOps.posterize(img, randint(3, 7))

    # Generate colour overlay
    overlay = img.split()[0]
    overlay = ImageEnhance.Contrast(overlay).enhance(uniform(1.0, 2.0))
    overlay = ImageEnhance.Brightness(overlay).enhance(uniform(1.0, 2.0))

    overlay = ImageOps.colorize(overlay, colours[0], colours[1])

    # Overlay red and yellow onto main image and sharpen the hell out of it
    img = Image.blend(img, overlay, uniform(0.1, 0.4))
    img = ImageEnhance.Sharpness(img).enhance(randint(5, 300))

    return img


CMD_HELP.update(
    {
        "deepfry": f"**Plugin : **`deepfry`\
        \n\n  »  **Perintah :** `{cmd}deepfry` atau `.deepfry` [level(1-8)]\
        \n  »  **Kegunaan : **Deepfry foto atau sticker dari bot @image_deepfrybot.\
        \n\n  »  **Perintah :** `{cmd}deepfry` [level(1-5)]\
        \n  »  **Kegunaan : **Deepfry foto atau sticker.\
    "
    }
)
