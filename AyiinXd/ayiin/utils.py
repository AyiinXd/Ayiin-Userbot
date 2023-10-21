# Credits: @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
#
# autopilot by @kenkan

import asyncio
import importlib
import logging
import os
import random
import sys
from pathlib import Path
from random import randint
from traceback import format_exc

from telethon.tl.functions.contacts import UnblockRequest
from telethon.errors import ChannelsTooMuchError
from telethon.tl.functions.channels import CreateChannelRequest, EditAdminRequest, EditPhotoRequest, InviteToChannelRequest
from telethon.tl.types import ChatPhotoEmpty, InputChatUploadedPhoto, ChatAdminRights
from telethon.utils import get_peer_id

from config import var
from AyiinXd import (
    Ayiin,
    CMD_HELP,
    LOGS,
)

from .tools import download_file, set_var_value


new_rights = ChatAdminRights(
    add_admins=True,
    invite_users=True,
    change_info=True,
    ban_users=True,
    delete_messages=True,
    pin_messages=True,
    manage_call=True,
)


async def autopilot():
    LOGS.info("TUNGGU SEBENTAR. SEDANG MEMBUAT GROUP LOG USERBOT UNTUK ANDA")
    try:
        r = await Ayiin(
            CreateChannelRequest(
                title="Aʏɪɪɴ-Usᴇʀʙᴏᴛ Lᴏɢs",
                about="» Group log Created by: Ayiin-Userbot\n\n» Support : @AyiinChats\n» Support: @AyiinChannel",
                megagroup=True,
            ),
        )
    except ChannelsTooMuchError:
        LOGS.info(
            "Channel dan Group Anda Melebihi batas, Hapus Salah Satu Dan Restart Lagi"
        )
        exit(1)
    except BaseException:
        LOGS.info(
            "Terjadi kesalahan, Buat sebuah grup lalu isi id nya di config var BOTLOG_CHATID."
        )
        exit(1)
    chat = r.chats[0]
    channel = get_peer_id(chat)
    if isinstance(chat.photo, ChatPhotoEmpty):
        photo = await download_file(
            "https://telegra.ph/file/b88d710cee9a6d6783abc.jpg", "photoyins.jpg"
        )
        ll = await Ayiin.upload_file(photo)
        try:
            await Ayiin(
                EditPhotoRequest(int(channel), InputChatUploadedPhoto(ll))
            )
        except BaseException as er:
            LOGS.exception(er)
    if not str(chat.id).startswith("-100"):
        Value_id = "-100" + str(chat.id)
    else:
        Value_id = str(chat.id)
    await set_var_value("BOTLOG_CHATID", Value_id)
    os.execvp(sys.executable, [sys.executable, "-m", "AyiinXd"])


async def autobot():
    try:
        await Ayiin.start()
        await asyncio.sleep(15)
        await Ayiin.send_message(
            var.BOTLOG_CHATID,
            "**MOHON TUNGGU SEBENTAR, SEDANG MEMBUAT ASSISTANT BOT ANDA DI @BotFather**"
        )
        LOGS.info("MOHON TUNGGU SEBENTAR, SEDANG MEMBUAT ASSISTANT BOT ANDA.")
        who = await Ayiin.get_me()
        name = f"{who.first_name} Assistant Bot"
        if who.username:
            username = f"{who.username}_bot"
        else:
            username = f"Ayiin{(str(who.id))[5:]}bot"
        bf = "@BotFather"
        await Ayiin(UnblockRequest(bf))
        await Ayiin.send_message(bf, "/cancel")
        await asyncio.sleep(1)
        await Ayiin.send_message(bf, "/start")
        await asyncio.sleep(1)
        await Ayiin.send_message(bf, "/newbot")
        await asyncio.sleep(1)
        isdone = (await Ayiin.get_messages(bf, limit=1))[0].text
        if isdone.startswith("That I cannot do."):
            LOGS.info(
                "Silakan buat Bot dari @BotFather dan tambahkan tokennya di var BOT_TOKEN"
            )
            sys.exit(1)
        await Ayiin.send_message(bf, name)
        await asyncio.sleep(1)
        isdone = (await Ayiin.get_messages(bf, limit=1))[0].text
        if not isdone.startswith("Good."):
            await Ayiin.send_message(bf, "My Assistant Bot")
            await asyncio.sleep(1)
            isdone = (await Ayiin.get_messages(bf, limit=1))[0].text
            if not isdone.startswith("Good."):
                LOGS.info(
                    "Silakan buat Bot dari @BotFather dan tambahkan tokennya di var BOT_TOKEN"
                )
                sys.exit(1)
        filogo = random.choice(
            [
                "https://telegra.ph/file/2127175807fe36f6a40f1.jpg",
                "AyiinXd/resources/logo.jpg",
            ]
        )
        await Ayiin.send_message(bf, username)
        await asyncio.sleep(3)
        isdone = (await Ayiin.get_messages(bf, limit=1))[0].text
        await Ayiin.send_read_acknowledge("botfather")
        await asyncio.sleep(3)
        if isdone.startswith("Sorry,"):
            ran = randint(1, 100)
            username = f"Ayiin{(str(who.id))[6:]}{str(ran)}bot"
            await Ayiin.send_message(bf, username)
            await asyncio.sleep(3)
            nowdone = (await Ayiin.get_messages(bf, limit=1))[0].text
            if nowdone.startswith("Done!"):
                token = nowdone.split("`")[1]
                await Ayiin.send_message(bf, "/setinline")
                await asyncio.sleep(1)
                await Ayiin.send_message(bf, f"@{username}")
                await asyncio.sleep(1)
                await Ayiin.send_message(bf, "Search")
                await asyncio.sleep(3)
                await Ayiin.send_message(bf, "/setuserpic")
                await asyncio.sleep(1)
                await Ayiin.send_message(bf, f"@{username}")
                await asyncio.sleep(1)
                await Ayiin.send_file(bf, filogo)
                await asyncio.sleep(3)
                await Ayiin.send_message(bf, "/setabouttext")
                await asyncio.sleep(1)
                await Ayiin.send_message(bf, f"@{username}")
                await asyncio.sleep(1)
                await Ayiin.send_message(bf, f"Managed With ✨ By {who.first_name}")
                await asyncio.sleep(3)
                await Ayiin.send_message(bf, "/setdescription")
                await asyncio.sleep(1)
                await Ayiin.send_message(bf, f"@{username}")
                await asyncio.sleep(1)
                await Ayiin.send_message(
                    bf, f"✨ Owner ~ {who.first_name} ✨\n\n✨ Powered By ~ @AyiinChannel ✨"
                )
                await Ayiin.send_message(
                    var.BOTLOG_CHATID,
                    f"**BERHASIL MEMBUAT ASSISTANT BOT ANDA DENGAN USERNAME @{username}**",
                )
                LOGS.info(
                    f"BERHASIL MEMBUAT ASSISTANT BOT ANDA DENGAN USERNAME @{username}")
                try:
                    await Ayiin(InviteToChannelRequest(int(var.BOTLOG_CHATID), [username]))
                    await asyncio.sleep(3)
                except BaseException:
                    pass
                try:
                    await Ayiin(EditAdminRequest(var.BOTLOG_CHATID, username, new_rights, "Assɪsᴛᴀɴᴛ Aʏɪɪɴ"))
                    await asyncio.sleep(3)
                except BaseException:
                    pass
                await Ayiin.send_message(
                    var.BOTLOG_CHATID,
                    "**SEDANG MERESTART USERBOT HARAP TUNGGU.**",
                )
                await set_var_value("BOT_TOKEN", token)
                await set_var_value("BOT_USERNAME", f"{username}")
                os.execvp(sys.executable, [sys.executable, "-m", "AyiinXd"])
            else:
                LOGS.info(
                    "Silakan Hapus Beberapa Bot Telegram Anda di @Botfather atau Set Var BOT_TOKEN dengan token bot"
                )
                sys.exit(1)
        elif isdone.startswith("Done!"):
            token = isdone.split("`")[1]
            await Ayiin.send_message(bf, "/setinline")
            await asyncio.sleep(1)
            await Ayiin.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await Ayiin.send_message(bf, "Search")
            await asyncio.sleep(3)
            await Ayiin.send_message(bf, "/setuserpic")
            await asyncio.sleep(1)
            await Ayiin.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await Ayiin.send_file(bf, filogo)
            await asyncio.sleep(3)
            await Ayiin.send_message(bf, "/setabouttext")
            await asyncio.sleep(1)
            await Ayiin.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await Ayiin.send_message(bf, f"Managed With ✨ By {who.first_name}")
            await asyncio.sleep(3)
            await Ayiin.send_message(bf, "/setdescription")
            await asyncio.sleep(1)
            await Ayiin.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await Ayiin.send_message(
                bf, f"✨ Owner ~ {who.first_name} ✨\n\n✨ Powered By ~ @AyiinChannel ✨"
            )
            await Ayiin.send_message(
                var.BOTLOG_CHATID,
                f"**BERHASIL MEMBUAT ASSISTANT BOT ANDA DENGAN USERNAME @{username}**",
            )
            LOGS.info(
                f"BERHASIL MEMBUAT ASSISTANT BOT DENGAN USERNAME @{username}"
            )
            try:
                await Ayiin(InviteToChannelRequest(int(var.BOTLOG_CHATID), [username]))
                await asyncio.sleep(3)
            except BaseException:
                pass
            try:
                await Ayiin(EditAdminRequest(var.BOTLOG_CHATID, username, new_rights, "Assɪsᴛᴀɴᴛ Aʏɪɪɴ"))
                await asyncio.sleep(3)
            except BaseException:
                pass
            await Ayiin.send_message(
                var.BOTLOG_CHATID,
                "**SEDANG MERESTART USERBOT HARAP TUNGGU.**",
            )
            await set_var_value("BOT_TOKEN", token)
            await set_var_value("BOT_USERNAME", f"{username}")
            os.execvp(sys.executable, [sys.executable, "-m", "AyiinXd"])
        else:
            LOGS.info(
                "Silakan Hapus Beberapa Bot Telegram Anda di @Botfather atau Set Var BOT_TOKEN dengan token bot"
            )
            sys.exit(1)
    except BaseException:
        LOGS.info(format_exc())


def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        path = Path(f"AyiinXd/modules/{shortname}.py")
        name = "AyiinXd.modules.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("Successfully imported " + shortname)
    else:

        path = Path(f"AyiinXd/modules/{shortname}.py")
        name = "AyiinXd.modules.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.Ayiin = Ayiin
        mod.LOGS = LOGS
        mod.CMD_HELP = CMD_HELP
        mod.logger = logging.getLogger(shortname)
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["AyiinXd.modules." + shortname] = mod
        LOGS.info("Successfully imported " + shortname)


def start_assistant(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        path = Path(f"AyiinXd/modules/assistant/{shortname}.py")
        name = "AyiinXd.modules.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("Starting Your Assistant Bot.")
        LOGS.info("Assistant Sucessfully imported " + shortname)
    else:
        path = Path(f"AyiinXd/modules/assistant/{shortname}.py")
        name = "AyiinXd.modules.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = Ayiin.bot
        spec.loader.exec_module(mod)
        sys.modules["AyiinXd.modules.assistant" + shortname] = mod
        LOGS.info("Assistant Successfully imported" + shortname)


def remove_plugin(shortname):
    try:
        try:
            for i in CMD_HELP[shortname]:
                Ayiin.remove_event_handler(i)
            del CMD_HELP[shortname]

        except BaseException:
            name = f"AyiinXd.modules.{shortname}"

            for i in reversed(range(len(Ayiin._event_builders))):
                ev, cb = Ayiin._event_builders[i]
                if cb.__module__ == name:
                    del Ayiin._event_builders[i]
    except BaseException:
        raise ValueError
