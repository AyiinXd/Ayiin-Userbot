# Copyright (C) 2020 azrim.
# All rights reserved.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

from re import match

from bitlyshortener import Shortener

from AyiinXd.ayiin import ayiin_cmd

from . import var


@ayiin_cmd(pattern="bitly(?: |$)(.*)")
async def shortener(short):
    """
    Shorten link using bit.ly API
    """
    if var.BITLY_TOKEN is not None:
        token = [f"{var.BITLY_TOKEN}"]
        reply = await short.get_reply_message()
        message = short.pattern_match.group(1)
        if message:
            pass
        elif reply:
            message = reply.text
        else:
            await short.edit("`Error! No URL given!`")
            return
        link_match = match(r"\bhttps?://.*\.\S+", message)
        if not link_match:
            await short.edit(
                "`Error! Please provide valid url!`\nexample: https://google.com"
            )
            return
        urls = [f"{message}"]
        bitly = Shortener(tokens=token, max_cache_size=8192)
        raw_output = bitly.shorten_urls(urls)
        string_output = f"{raw_output}"
        output = string_output.replace("['", "").replace("']", "")
        await short.edit(
            f"`Your link shortened successfully!`\nHere is your link {output}"
        )
        if var.BOTLOG_CHATID:
            await short.client.send_message(
                var.BOTLOG_CHATID, f"`#SHORTLINK \nThis Your Link!`\n {output}"
            )
    else:
        await short.edit(
            "Set bit.ly API token first\nGet from [here](https://bitly.com/a/sign_up)"
        )
