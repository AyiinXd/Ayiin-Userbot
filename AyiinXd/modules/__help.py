# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

from AyiinXd import BOT_USERNAME, CMD_HELP, bot, ch
from AyiinXd.utils import edit_delete, edit_or_reply, ayiin_cmd


@ayiin_cmd(pattern="help(?: |$)(.*)")
async def help(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await edit_or_reply(event, f"{CMD_HELP[args]}\n\n© {ch}")
        else:
            await edit_delete(event, f"**Modules {args} Gak Ada Tod**, **Ketik Yang Bener Anj.**")
    else:
        try:
            results = await event.client.inline_query(  # pylint:disable=E0602
                BOT_USERNAME, "@AyiinXdSupport"
            )
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except Exception as e:
            await edit_or_reply(event, f"**INFO :** `{e}`"
                                )
