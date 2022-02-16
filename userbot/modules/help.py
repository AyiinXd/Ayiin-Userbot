# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

from userbot import CHANNEL
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, ICON_HELP, bot
from userbot.utils import edit_delete, edit_or_reply, ayiin_cmd
from time import sleep

modules = CMD_HELP


@ayiin_cmd(pattern="help(?: |$)(.*)")
async def help(event):
    """For help command"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await edit_or_reply(event, str(CMD_HELP[args]))
        else:
            await edit_delete(event, f"`{args}` **Tidak Ada Modul.**")
    else:
        user = await bot.get_me()
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += f"`\t\t\t{ICON_HELP}\t\t\t"
        await event.edit("🗿")
        sleep(3)
        await edit_or_reply(
            event,
            f"**[᯽ 𝙰𝚈𝙸𝙸𝙽-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ᯽](https://github.com/AyiinXd/Ayiin-Userbot):**\n"
            f"**߷ 𝙹𝚄𝙼𝙻𝙰𝙷** `{len(modules)}` **Modules**\n"
            f"**♕︎ 𝙾𝚆𝙽𝙴𝚁:** [{user.first_name}](tg://user?id={user.id})\n\n"
            f"{ICON_HELP}   {string}"
            f"\n\n☞  𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @AyiinXdSupport\n☞  𝙽𝙾𝚃𝙴𝚂 :  '{cmd}help yinsubot' Untuk Melihat Module Lainnya"
        )
