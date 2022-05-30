# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for Telegraph commands """

import os
from datetime import datetime

from PIL import Image
from telegraph import Telegraph, exceptions, upload_file

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from Stringyins import get_string

telegraph = Telegraph()
r = telegraph.create_account(short_name="telegraph")
auth_url = r["auth_url"]


@ayiin_cmd(pattern="tg (m|t)$")
async def telegraphs(graph):
    """For telegraph command, upload media & text to telegraph site."""
    xxnx = await eor(graph, get_string("com_1"))
    if not graph.text[0].isalpha() and graph.text[0] not in (
            "/", "#", "@", "!"):
        if graph.fwd_from:
            return
        if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
            os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
        if graph.reply_to_msg_id:
            start = datetime.now()
            r_message = await graph.get_reply_message()
            input_str = graph.pattern_match.group(1)
            if input_str == "m":
                downloaded_file_name = await graph.client.download_media(
                    r_message, TEMP_DOWNLOAD_DIRECTORY
                )
                end = datetime.now()
                ms = (end - start).seconds
                await xxnx.edit(get_string("tgph_1").format(downloaded_file_name, ms)
                )
                if downloaded_file_name.endswith(".webp"):
                    resize_image(downloaded_file_name)
                try:
                    media_urls = upload_file(downloaded_file_name)
                except exceptions.TelegraphException as exc:
                    await xxnx.edit(get_string("error_1").format(str(exc)))
                    os.remove(downloaded_file_name)
                else:
                    os.remove(downloaded_file_name)
                    await xxnx.edit(get_string("tgph_2").format(media_urls[0]),
                        link_preview=True,
                    )
            elif input_str == "t":
                user_object = await graph.client.get_entity(r_message.sender_id)
                title_of_page = user_object.first_name  # + " " + user_object.last_name
                # apparently, all Users do not have last_name field
                page_content = r_message.message
                if r_message.media:
                    if page_content != "":
                        title_of_page = page_content
                    downloaded_file_name = await graph.client.download_media(
                        r_message, TEMP_DOWNLOAD_DIRECTORY
                    )
                    m_list = None
                    with open(downloaded_file_name, "rb") as fd:
                        m_list = fd.readlines()
                    for m in m_list:
                        page_content += m.decode("UTF-8") + "\n"
                    os.remove(downloaded_file_name)
                page_content = page_content.replace("\n", "<br>")
                response = telegraph.create_page(
                    title_of_page, html_content=page_content
                )
                await xxnx.edit(get_string("tgph_2").format(response["path"]),
                    link_preview=True,
                )
        else:
            await eod(
                xxnx, get_string("tgph_3")
            )


def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")


CMD_HELP.update(
    {
        "telegraph": f"**Plugin : **`telegraph`\
        \n\n  »  **Perintah :** `{cmd}tg` m\
        \n  »  **Kegunaan : **Mengunggah m(Media) Ke Telegraph.\
        \n\n  »  **Perintah :** `{cmd}tg` t\
        \n  »  **Kegunaan : **Mengunggah t(Teks) Ke Telegraph.\
    "
    }
)
