# Copyright (C) 2021 Bian Sepang
# All Rights Reserved.
#
# Recode by @mrismanaziz
# @SharingUserbot

import nekos

from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eod, eor

from . import cmd


arguments = [
    'wallpaper',
    'ngif',
    'tickle',
    'feed',
    'gecg',
    'gasm',
    'slap',
    'avatar',
    'lizard',
    'waifu',
    'pat',
    '8ball',
    'kiss',
    'neko',
    'spank',
    'cuddle',
    'fox_girl',
    'hug',
    'smug',
    'goose',
    'woof'
]


@ayiin_cmd(pattern="nekos(?: |$)(.*)")
async def nekos_img(event):
    args = event.pattern_match.group(1)
    if not args or args not in arguments:
        return await eod(
            event,
            f"ketik `{cmd}help nekos` untuk melihat argumen yang tersedia."
        )
    xx = await eor(event, "`Mengambil dari nekos...`")
    pic = nekos.img(args)
    await event.client.send_file(
        event.chat_id,
        pic,
    )
    await xx.delete()


CMD_HELP.update(
    {
        "nekos": f"**Plugin : **`nekos`\
        \n\n  »  **Perintah :** `{cmd}nekos` <arguments>\
        \n  »  **Kegunaan : **Untuk mencari gif hentai anime untuk bahan para wibu bau bawang.\
        \n\n  •  **Arguments :** `wallpaper`, `ngif`, `tickle`, `feed`, `gecg`, `gasm`, `slap`, `avatar`, `lizard`, `waifu`, `pat`, `8ball`, `kiss`, `neko`, `spank`, `cuddle`, `fox_girl`, `hug`, `smug`, `goose`, `woof`\
    "
    }
)
