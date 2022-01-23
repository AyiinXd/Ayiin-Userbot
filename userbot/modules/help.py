# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

from userbot import CHANNEL
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, ICON_HELP, bot
from userbot.utils import edit_delete, edit_or_reply, man_cmd

modules = CMD_HELP


@man_cmd(pattern="help(?: |$)(.*)")
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
        await edit_or_reply(
            event,
            f"**😈 𝘿𝙖𝙛𝙩𝙖𝙧 𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 𝙐𝙣𝙩𝙪𝙠 [𝘼𝙮𝙞𝙞𝙣-𝙐𝙨𝙚𝙧𝙗𝙤𝙩](https://github.com/AyiinXd/Ayiin-Userbot):**\n"
            f"**🕯️ 𝙅𝙪𝙢𝙡𝙖𝙝** `{len(modules)}` **Modules**\n"
            f"**👑 𝙊𝙬𝙣𝙚𝙧:** [{user.first_name}](tg://user?id={user.id})\n\n"
            f"{ICON_HELP}   {string}"
            f"**𝙎𝙪𝙥𝙥𝙤𝙧𝙩      [𝘼𝙮𝙞𝙞𝙣𝙎𝙪𝙥𝙥𝙤𝙧𝙩](https://t.me/AyiinXdSupport):**\n",
        )
        await event.reply(
            f"\n**Contoh Ketik** `{cmd}help afk` **Untuk Melihat Informasi Module**"
        )
