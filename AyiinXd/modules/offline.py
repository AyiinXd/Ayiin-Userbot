# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

import time
from datetime import datetime
from random import randint
from secrets import choice

from telethon.events import StopPropagation
from telethon.tl.functions.account import UpdateProfileRequest

from AyiinXd import AFKREASON
from AyiinXd.ayiin import AyiinChanger, ayiin_cmd, ayiin_handler
from AyiinXd.database.permit import is_approved, get_mode_permit

from . import var

# ========================= CONSTANTS ============================
AFKSTR = [
    "**✧ Maaf Boss {} Sedang OFF!**",
    "**✧ Maaf Boss {} Sedang OFF Tunggu Sampai Online!**",
    "**✧ Maaf Boss {} Sedang OFF Tunggulah Sampai Online**",
    "**✧ Maaf Boss {} Sedang OFF!**",
]
ISAFK = False
USER_AFK = {}
afk_time = None
afk_start = {}

# =================================================================


@ayiin_cmd(pattern="off(?: |$)(.*)")
async def set_afk(afk_e):
    string = afk_e.pattern_match.group(1)
    global ISAFK
    global AFKREASON
    global USER_AFK
    global afk_time
    global afk_start
    global afk_end
    user = await afk_e.client.get_me()
    owner = user.first_name
    USER_AFK = {}
    afk_time = None
    afk_end = {}
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    if string:
        AFKREASON = string
        await afk_e.edit(f"❏ **{owner} Telah OFF**\n└ **Karena:** `{string}`")
    else:
        await afk_e.edit(f"**✧ {owner} Telah OFF**")
    if user.last_name:
        await afk_e.client(
            UpdateProfileRequest(
                first_name=user.first_name, last_name=user.last_name + "【 OFF 】"
            )
        )
    else:
        await afk_e.client(
            UpdateProfileRequest(first_name=user.first_name, last_name="【 OFF 】")
        )
    if var.BOTLOG_CHATID:
        await afk_e.client.send_message(var.BOTLOG_CHATID, f"#OFF\n**✧ {owner} Telah OFF!**")
    ISAFK = True
    afk_time = datetime.now()
    raise StopPropagation


@ayiin_handler(outgoing=True)
async def type_afk_is_not_true(notafk):
    global ISAFK
    global COUNT_MSG
    global USERS
    global AFKREASON
    global USER_AFK
    global afk_time
    global afk_start
    global afk_end
    user = await notafk.client.get_me()
    owner = user.first_name
    last = user.last_name
    last1 = last[:-12] if last and last.endswith("【 OFF 】") else ""
    back_alive = datetime.now()
    afk_end = back_alive.replace(microsecond=0)
    if ISAFK:
        ISAFK = False
        msg = await notafk.respond(f"**✧ {owner} Telah Kembali!**")
        time.sleep(7)
        await msg.delete()
        await notafk.client(
            UpdateProfileRequest(first_name=user.first_name, last_name=last1)
        )
        if var.BOTLOG_CHATID:
            await notafk.client.send_message(
                var.BOTLOG_CHATID,
                "Anda Mendapatkan "
                + str(COUNT_MSG)
                + " Pesan Dari "
                + str(len(USERS))
                + " Obrolan Saat Anda OFFLINE",
            )
            for i in USERS:
                name = await notafk.client.get_entity(i)
                name0 = str(name.first_name)
                await notafk.client.send_message(
                    var.BOTLOG_CHATID,
                    "["
                    + name0
                    + "](tg://user?id="
                    + str(i)
                    + ")"
                    + " Mengirim Mu "
                    + "`"
                    + str(USERS[i])
                    + " Pesan`",
                )
        COUNT_MSG = 0
        USERS = {}
        AFKREASON = None


@ayiin_handler(incoming=True)
async def mention_afk(mention):
    global COUNT_MSG
    global USERS
    global ISAFK
    global USER_AFK
    global afk_time
    global afk_start
    global afk_end
    user = await mention.client.get_me()
    owner = user.first_name
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    afk_since = "**Terakhir Online**"
    if mention.message.mentioned and not (await mention.get_sender()).bot and ISAFK:
        now = datetime.now()
        datime_since_afk = now - afk_time
        time = float(datime_since_afk.seconds)
        days = time // (24 * 3600)
        time %= 24 * 3600
        hours = time // 3600
        time %= 3600
        minutes = time // 60
        time %= 60
        seconds = time
        if days == 1:
            afk_since = "**Kemarin**"
        elif days > 1:
            if days > 6:
                date = now + datetime.timedelta(
                    days=-days, hours=-hours, minutes=-minutes
                )
                afk_since = date.strftime("%A, %Y %B %m, %H:%I")
            else:
                wday = now + datetime.timedelta(days=-days)
                afk_since = wday.strftime("%A")
        elif hours > 1:
            afk_since = f"`{int(hours)} Jam {int(minutes)} Menit`"
        elif minutes > 0:
            afk_since = f"`{int(minutes)} Menit {seconds} Detik`"
        else:
            afk_since = f"`{seconds} Detik`"
        if mention.sender_id not in USERS:
            if AFKREASON:
                await mention.reply(f"❏ **{owner} Sedang OFFLINE**\n├ {afk_since} **Yang Lalu**\n└ **Karena:** `{AFKREASON}`"
                                    )
            else:
                await mention.reply(str(choice(AFKSTR.format(owner))))
            USERS.update({mention.sender_id: 1})
        else:
            if USERS[mention.sender_id] % randint(2, 4) == 0:
                if AFKREASON:
                    await mention.reply(
                        f"**✧ {owner} Masih OFF** {afk_since} **Yang Lalu.**\
                            \n**✧ Karena :** `{AFKREASON}`"
                    )
                else:
                    await mention.reply(str(choice(AFKSTR)))
            USERS[mention.sender_id] = USERS[mention.sender_id] + 1
        COUNT_MSG = COUNT_MSG + 1


@ayiin_handler(incoming=True, func=lambda e: e.is_private)
async def afk_on_pm(sender):
    global ISAFK
    global USERS
    global COUNT_MSG
    global USER_AFK
    global afk_time
    global afk_start
    global afk_end
    back_alivee = datetime.now()
    AyiinBot = await sender.client.get_me()
    owner = AyiinBot.first_name
    afk_end = back_alivee.replace(microsecond=0)
    afk_since = "**Belum Lama**"
    apprv = None
    if (
        sender.is_private
        and sender.sender_id != 777000
        and not (await sender.get_sender()).bot
    ):
        is_app = AyiinChanger(is_approved())
        if get_mode_permit():
            if sender.sender_id in is_app:
                apprv = True
        else:
            apprv = True
        if apprv and ISAFK:
            now = datetime.now()
            datime_since_afk = now - afk_time  # pylint:disable=E0602
            time = float(datime_since_afk.seconds)
            days = time // (24 * 3600)
            time %= 24 * 3600
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            if days == 1:
                afk_since = "**Kemarin**"
            elif days > 1:
                if days > 6:
                    date = now + datetime.timedelta(
                        days=-days, hours=-hours, minutes=-minutes
                    )
                    afk_since = date.strftime("%A, %Y %B %m, %H:%I")
                else:
                    wday = now + datetime.timedelta(days=-days)
                    afk_since = wday.strftime("%A")
            elif hours > 1:
                afk_since = f"`{int(hours)} Jam {int(minutes)} Menit`"
            elif minutes > 0:
                afk_since = f"`{int(minutes)} Menit {seconds} Detik`"
            else:
                afk_since = f"`{seconds} Detik`"
            if sender.sender_id not in USERS:
                if AFKREASON:
                    await sender.reply(
                        f"❏ **{owner} Sedang OFFLINE**\n├ {afk_since} **Yang Lalu**\n└ **Karena:** `{AFKREASON}`"
                    )
                else:
                    await sender.reply(str(choice(AFKSTR)))
                USERS.update({sender.sender_id: 1})
                COUNT_MSG = COUNT_MSG + 1
            elif apprv:
                if USERS[sender.sender_id] % randint(2, 4) == 0:
                    if AFKREASON:
                        await sender.reply(
                            f"❏ **{owner} Sedang OFFLINE**\n├ {afk_since} **Yang Lalu**\n└ **Karena:** `{AFKREASON}`"
                        )
                    else:
                        await sender.reply(str(choice(AFKSTR)))
                USERS[sender.sender_id] = USERS[sender.sender_id] + 1
                COUNT_MSG = COUNT_MSG + 1
