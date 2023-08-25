# Copyright (C) 2020 KeselekPermen69
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

import re

from hentai import Hentai, Utils
from natsort import natsorted

from AyiinXd import CMD_HELP, Ayiin
from AyiinXd.events import ayiin_cmd
from AyiinXd.ayiin import post_to_telegraph

from . import cmd


@Ayiin.on(ayiin_cmd(outgoing=True, pattern=r"nhentai(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("`Mencari doujin...`")
    input_str = event.pattern_match.group(1)
    code = input_str
    if "nhentai" in input_str:
        link_regex = r"(?:https?://)?(?:www\.)?nhentai\.net/g/(\d+)"
        match = re.match(link_regex, input_str)
        code = match.group(1)
    if input_str == "random":
        code = Utils.get_random_id()
    try:
        doujin = Hentai(code)
    except BaseException as n_e:
        if "404" in str(n_e):
            return await event.edit(f"Tidak ditemukan doujin untuk `{code}`")
        return await event.edit(f"ERROR: {n_e}")
    msg = ""
    imgs = "".join(f"<img src='{url}'/>" for url in doujin.image_urls)
    imgs = f"&#8205; {imgs}"
    title = doujin.title()
    graph_link = post_to_telegraph(title, imgs)
    msg += f"[{title}]({graph_link})"
    msg += f"\n**Source :**\n[{code}]({doujin.url})"
    if doujin.parody:
        msg += "\n**Parodies :**"
        parodies = [
            "#" + parody.name.replace(" ", "_").replace("-", "_")
            for parody in doujin.parody
        ]

        msg += "\n" + " ".join(natsorted(parodies))
    if doujin.character:
        msg += "\n**Characters :**"
        charas = [
            "#" + chara.name.replace(" ", "_").replace("-", "_")
            for chara in doujin.character
        ]

        msg += "\n" + " ".join(natsorted(charas))
    if doujin.tag:
        msg += "\n**Tags :**"
        tags = [
            "#" +
            tag.name.replace(
                " ",
                "_").replace(
                "-",
                "_") for tag in doujin.tag]

        msg += "\n" + " ".join(natsorted(tags))
    if doujin.artist:
        msg += "\n**Artists :**"
        artists = [
            "#" + artist.name.replace(" ", "_").replace("-", "_")
            for artist in doujin.artist
        ]

        msg += "\n" + " ".join(natsorted(artists))
    if doujin.language:
        msg += "\n**Languages :**"
        languages = [
            "#" + language.name.replace(" ", "_").replace("-", "_")
            for language in doujin.language
        ]

        msg += "\n" + " ".join(natsorted(languages))
    if doujin.category:
        msg += "\n**Categories :**"
        categories = [
            "#" + category.name.replace(" ", "_").replace("-", "_")
            for category in doujin.category
        ]

        msg += "\n" + " ".join(natsorted(categories))
    msg += f"\n**Pages :**\n{doujin.num_pages}"
    await event.edit(msg, link_preview=True)


CMD_HELP.update(
    {
        "nhentai": f"**Plugin : **`nhentai`\
        \n\n  »  **Perintah :** `{cmd}nhentai` <code atau link>\
        \n  »  **Kegunaan : **Melihat nhentai di telegra.ph XD\
        \n\n  »  **Perintah :** `{cmd}nhentai random`>\
        \n  »  **Kegunaan : **Melihat nhentai di telegra.ph XD secara random\
    "
    }
)
