# Copyright (C) 2021 Bian Sepang
# All Rights Reserved.
#
# Recode by @mrismanaziz
# @SharingUserbot

import nekos

from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eod, eor

from . import cmd, var


arguments = [
    "feet",
    "yuri",
    "trap",
    "futanari",
    "hololewd",
    "lewdkemo",
    "solog",
    "feetg",
    "cum",
    "erokemo",
    "les",
    "wallpaper",
    "lewdk",
    "ngif",
    "tickle",
    "lewd",
    "feed",
    "gecg",
    "eroyuri",
    "eron",
    "cum_jpg",
    "bj",
    "nsfw_neko_gif",
    "solo",
    "nsfw_avatar",
    "gasm",
    "poke",
    "anal",
    "slap",
    "hentai",
    "avatar",
    "erofeet",
    "holo",
    "keta",
    "blowjob",
    "pussy",
    "tits",
    "holoero",
    "lizard",
    "pussy_jpg",
    "pwankg",
    "classic",
    "kuni",
    "waifu",
    "pat",
    "8ball",
    "kiss",
    "femdom",
    "neko",
    "spank",
    "cuddle",
    "erok",
    "fox_girl",
    "boobs",
    "random_hentai_gif",
    "smallboobs",
    "hug",
    "ero",
    "goose",
    "baka",
    "woof",
    "kemonomimi",
    "smug",
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
        \n\n  •  **Arguments :** `8ball`, `anal`, `avatar`, `baka`, `bj`, `blowjob`, `boobs`, `classic`, `cuddle`, `cum`, `cum_jpg`, `ero`, `erofeet`, `erok`, `erokemo`, `eron`, `eroyuri`, `feed`, `feet`, `feetg`, `femdom`, `fox_girl`, `futanari`, `gasm`, `gecg`,`goose`, `hentai`, `holo`, `holoero`, `hololewd`, `hug`, `kemonomimi`, `keta`, `kiss`, `kuni`,`les`, `lewd`, `lewdk`, `lewdkemo`, `lizard`, `neko`, `ngif`, `nsfw_avatar`, `nsfw_neko_gif`, `pat`, `poke`, `pussy`, `pussy_jpg`, `pwankg`, `random_hentai_gif`, `slap`, `smallboobs`, `smug`, `solo`, `solog`, `spank`, `tickle`, `tits`, `trap`, `waifu`, `wallpaper`, `woof`, `yuri`\
    "
    }
)
