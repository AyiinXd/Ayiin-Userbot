# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import BOT_USERNAME, CMD_HELP, bot, ch
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from Stringyins import get_string


@ayiin_cmd(pattern="help(?: |$)(.*)")
async def help(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await eor(event, get_string("help_5").format(CMD_HELP[args], ch))
        else:
            await eod(event, get_string("help_10").format(args, cmd))
    else:
        try:
            results = await bot.inline_query(  # pylint:disable=E0602
                BOT_USERNAME, "@AyiinXdSupport"
            )
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except Exception as e:
            await eor(event, get_string("error_1").format(e)
                      )
