# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# Ported by Koala @manusiarakitann
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio
import os

import heroku3
from telethon.errors import FloodWaitError

from AyiinXd import BLACKLIST_GCAST
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, DEVS, HEROKU_API_KEY, HEROKU_APP_NAME
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from Stringyins import get_string

GCAST_BLACKLIST = [
    -1001675396283,  # AyiinXdSupport
    -1001473548283,  # SharingUserbot
    -1001433238829,  # TedeSupport
    -1001476936696,  # AnosSupport
    -1001327032795,  # UltroidSupport
    -1001294181499,  # UserBotIndo
    -1001419516987,  # VeezSupportGroup
    -1001459812644,  # GeezSupportGroup
    -1001296934585,  # X-PROJECT BOT
    -1001481357570,  # UsergeOnTopic
    -1001459701099,  # CatUserbotSupport
    -1001109837870,  # TelegramBotIndonesia
    -1001752592753,  # Skyzusupport
    -1001788983303,  # KayzuSupport
    -1001380293847,  # NastySupport
    -1001267233272,  # PocongUserbot
    -1001500063792,  # Trident
    -1001687155877,  # CilikSupport
]

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
blchat = os.environ.get("BLACKLIST_GCAST") or ""


@ayiin_cmd(pattern="gcast(?: |$)(.*)")
async def gcast(event):
    if xx := event.pattern_match.group(1):
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await eod(event, get_string("gcast_1"))
    kk = await eor(event, get_string("gcast_3"))
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            if chat not in GCAST_BLACKLIST and chat not in BLACKLIST_GCAST:
                try:
                    await event.client.send_message(chat, msg)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWaitError as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await event.client.send_message(chat, msg)
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(get_string("gcast_2").format(done, er)
    )


@ayiin_cmd(pattern="gucast(?: |$)(.*)")
async def gucast(event):
    if xx := event.pattern_match.group(1):
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await eod(event, get_string("gcast_1"))
    kk = await eor(event, get_string("gcast_3"))
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            if chat not in DEVS:
                try:
                    await event.client.send_message(chat, msg)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWaitError as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await event.client.send_message(chat, msg)
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(get_string("gucast_1").format(done, er)
    )


@ayiin_cmd(pattern="blchat$")
async def sudo(event):
    blacklistgc = "True" if BLACKLIST_GCAST else "False"
    blc = blchat
    list = blc.replace(" ", "\n» ")
    if blacklistgc == "True":
        await eor(
            event, get_string("blkls_1").format(list, cmd)
        )
    else:
        await eod(event, get_string("blkls_2"))


@ayiin_cmd(pattern="addblacklist(?:\\s|$)([\\s\\S]*)")
async def add(event):
    xxnx = await eor(event, get_string("com_1"))
    var = "BLACKLIST_GCAST"
    gc = event.chat_id
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await eod(
            xxnx, get_string("addbl_1").format("menambahkan")
        )
        return
    heroku_Config = app.config()
    if event is None:
        return
    blgc = f"{BLACKLIST_GCAST} {gc}"
    blacklistgrup = (
        blgc.replace("{", "")
        .replace("}", "")
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("set() ", "")
    )
    await xxnx.edit(get_string("addbl_2").format(gc)
    )
    heroku_Config[var] = blacklistgrup


@ayiin_cmd(pattern="delblacklist(?:\\s|$)([\\s\\S]*)")
async def _(event):
    xxx = await eor(event, get_string("com_1"))
    gc = event.chat_id
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await eod(
            xxx, get_string("addbl_1").format("menghapus")
        )
        return
    heroku_Config = app.config()
    if event is None:
        return
    gett = str(gc)
    if gett in blchat:
        blacklistgrup = blchat.replace(gett, "")
        await xxx.edit(get_string("delbl_1").format(gc)
        )
        var = "BLACKLIST_GCAST"
        heroku_Config[var] = blacklistgrup
    else:
        await eod(xxx, get_string("delbl_2"), time=45
        )


CMD_HELP.update(
    {
        "gcast": f"**Plugin : **`gcast`\
        \n\n  »  **Perintah :** `{cmd}gcast` <text/reply media>\
        \n  »  **Kegunaan : **Mengirim Global Broadcast pesan ke Seluruh Grup yang kamu masuk. (Bisa Mengirim Media/Sticker)\
        \n\n  »  **Perintah :** `{cmd}blchat`\
        \n  »  **Kegunaan : **Untuk Mengecek informasi daftar blacklist gcast.\
        \n\n  »  **Perintah :** `{cmd}addblacklist`\
        \n  »  **Kegunaan : **Untuk Menambahkan grup tersebut ke blacklist gcast.\
        \n\n  »  **Perintah :** `{cmd}delblacklist`\
        \n  »  **Kegunaan : **Untuk Menghapus grup tersebut dari blacklist gcast.\
        \n  •  **Note : **Ketik perintah** `{cmd}addblacklist` **dan** `{cmd}delblacklist` **di grup yang kamu Blacklist.\
    "
    }
)


CMD_HELP.update(
    {
        "gucast": f"**Plugin : **`gucast`\
        \n\n  »  **Perintah :** `{cmd}gucast` <text/reply media>\
        \n  »  **Kegunaan : **Mengirim Global Broadcast pesan ke Seluruh Private Massage / PC yang masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)
