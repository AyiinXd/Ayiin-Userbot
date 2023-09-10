# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# inline credit @keselekpermen69
# Recode by @mrismanaziz
# t.me/SharingUserbot
#
""" Userbot initialization. """

import logging
import time
import sys
from asyncio import get_event_loop
from base64 import b64decode
from logging import getLogger
from math import ceil
from pathlib import Path

from platform import python_version
from velar import GroupCallFactory
from git import Repo
from telethon import Button, __version__ as vsc
from telethon.sync import custom
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sync import TelegramClient

from config import Config

from .connection import validate_session
from .storage import Storage

def STORAGE(n):
    return Storage(Path("data") / n)


var = Config()

# 'bot' variable
if var.STRING_SESSION:
    session = validate_session(var.STRING_SESSION)
else:
    session = "AyiinUserBot"
try:
    Ayiin = TelegramClient(
        session=session,
        api_id=var.API_KEY,
        api_hash=var.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    setattr(
        Ayiin,
        "calls",
        GroupCallFactory(
            Ayiin,
            GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
        ).get_group_call()
    )
except Exception as e:
    print(f"STRING_SESSION - {e}")
    sys.exit()



if var.BOT_TOKEN is not None:
    bot = TelegramClient(
        "TG_BOT_TOKEN",
        api_id=var.API_KEY,
        api_hash=var.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    ).start(bot_token=var.BOT_TOKEN)
else:
    bot = None


# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
CMD_LIST = {}
SUDO_LIST = {}
ZALG_LIST = {}
LOAD_PLUG = {}
INT_PLUG = ""
ISAFK = False
AFKREASON = None
ENABLE_KILLME = True

# Bot Logs setup:
logging.basicConfig(
    format="[%(name)s] - [%(levelname)s] - %(message)s",
    level=logging.INFO,
)
logging.getLogger("asyncio").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)
logging.getLogger("telethon.network.mtprotosender").setLevel(logging.ERROR)
logging.getLogger("telethon.network.connection.connection").setLevel(logging.ERROR)

LOGS = getLogger(__name__)

LOOP = get_event_loop()
StartTime = time.time()
repo = Repo()
branch = repo.active_branch.name


ch = str(b64decode("QEF5aWluQ2hhbm5lbA=="))[2:15]
gc = str(b64decode("QEF5aWluQ2hhdHM="))[2:13]


async def update_restart_msg(chat_id, msg_id):
    from config import var

    message = (
        f"**Ayiin-UserBot v`{var.BOT_VER}` is back up and running!**\n\n"
        f"**Telethon:** `{vsc}`\n"
        f"**Python:** `{python_version()}`\n"
    )
    await Ayiin.edit_message(chat_id, msg_id, message)
    return True


def paginate_help(page_number, loaded_modules, prefix):
    from config import var

    number_of_rows = 6
    number_of_cols = 2
    global looters
    looters = page_number
    helpable_modules = [p for p in loaded_modules if not p.startswith("_")]
    helpable_modules = sorted(helpable_modules)
    modules = [
        custom.Button.inline(
            "{} {} {}".format(f"{var.INLINE_EMOJI}", x, f"{var.INLINE_EMOJI}"),
            data="ub_modul_{}".format(x),
        )
        for x in helpable_modules
    ]
    pairs = list(
        zip(
            modules[::number_of_cols],
            modules[1::number_of_cols],
        )
    )
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows: number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "⪻", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline(
                    "⪼ ʙᴀᴄᴋ ⪻", data="{}_close({})".format(prefix, modulo_page)
                ),
                custom.Button.inline(
                    "⪼", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs


def ibuild_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb


with Ayiin:
    try:
        user = Ayiin.get_me()
        OWNER_ID = user.id
    except BaseException as e:
        LOGS.info(e)