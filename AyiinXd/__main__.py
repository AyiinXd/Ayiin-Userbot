# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# Copyright (C) 2021 TeamUltroid for autobot
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
#
""" Userbot start point """


import sys
from importlib import import_module
from platform import python_version
from traceback import format_exc

from telethon import version
from telethon.tl.alltlobjects import LAYER

from AyiinXd import Ayiin, LOGS, LOOP, bot, bot_on
from AyiinXd.ayiin import autobot, autopilot, checking, heroku
from AyiinXd.modules import ALL_MODULES

from .database.core import db


async def AyiinMain():
    from config import var

    if db.is_connected:
        db.close()
    db.connect()

    await Ayiin.start()
    if not var.BOTLOG_CHATID:
        await autopilot()
    if not var.BOT_TOKEN:
        await autobot()
    try:
        for module_name in ALL_MODULES:
            imported_module = import_module(f"AyiinXd.modules.{module_name}")
        await bot.start()
        LOGS.info(f"Python Version - {python_version()}")
        LOGS.info(f"Telethon Version - {version.__version__} [Layer: {LAYER}]")
        LOGS.info(f"Userbot Version - {var.BOT_VER}")
        LOGS.info(f"Ayiin Version - 4.0.0")
        LOGS.info("[✨ BERHASIL DIAKTIFKAN! ✨]")
        await checking(Ayiin)
        await bot_on()
    except (ConnectionError, KeyboardInterrupt, NotImplementedError, SystemExit):
        pass
    except BaseException as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    try:
        heroku()
        LOOP.run_until_complete(AyiinMain())
    except BaseException:
        LOGS.error(format_exc())
        sys.exit()

if len(sys.argv) not in (1, 3, 4):
    Ayiin.disconnect()
else:
    try:
        Ayiin.run_until_disconnected()
    except ConnectionError:
        pass
