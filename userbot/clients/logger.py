# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

from telethon.tl.functions.channels import InviteToChannelRequest

from userbot import BOT_USERNAME
from userbot import BOT_VER as version
from userbot import BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import AYIIN2, AYIIN3, AYIIN4, AYIIN5, bot, branch

MSG_ON = """
✨ **Ayiin-Userbot Berhasil Di Aktifkan**
━━
➠ **Userbot Version -** `{}@{}`
➠ **Ketik** `{}alive` **untuk Mengecheck Bot**
━━
"""


async def ayiin_userbot_on():
    try:
        if bot:
            if BOTLOG_CHATID != 0:
                await bot.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if AYIIN2:
            if BOTLOG_CHATID != 0:
                await AYIIN2.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if AYIIN3:
            if BOTLOG_CHATID != 0:
                await AYIIN3.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if AYIIN4:
            if BOTLOG_CHATID != 0:
                await AYIIN4.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if AYIIN5:
            if BOTLOG_CHATID != 0:
                await AYIIN5.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass
