# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

""" Userbot module for System Stats commands """

import asyncio
import platform
import sys
import time
from asyncio import create_subprocess_exec as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from datetime import datetime
from os import remove
from platform import python_version
from shutil import which

import psutil
from telethon import __version__, version

from AyiinXd import CMD_HELP, StartTime
from AyiinXd.ayiin import (
    HOSTED_ON,
    bash,
    edit_or_reply,
    ayiin_cmd,
)

from . import cmd, var
from .ping import get_readable_time

try:
    from carbonnow import Carbon
except ImportError:
    Carbon = None

modules = CMD_HELP
emoji = var.ALIVE_EMOJI
alive_text = var.ALIVE_TEKS_CUSTOM


@ayiin_cmd(
    pattern="sysinfo$",
)
async def _(e):
    xxnx = await edit_or_reply(e, "`Processing...`")
    x, y = await bash("neofetch|sed 's/\x1B\\[[0-9;\\?]*[a-zA-Z]//g' >> neo.txt")
    with open("neo.txt", "r") as neo:
        p = (neo.read()).replace("\n\n", "")
    ok = Carbon(base_url="https://carbonara.vercel.app/api/cook", code=p)
    haa = await ok.memorize("neofetch")
    await e.reply(file=haa)
    await xxnx.delete()
    remove("neo.txt")


@ayiin_cmd(pattern=r"spc")
async def psu(event):
    uname = platform.uname()
    softw = "**Iɴғᴏʀᴍᴀsɪ Sɪsᴛᴇᴍ**\n"
    softw += f"**Sɪsᴛᴇᴍ   :** `{uname.system}`\n"
    softw += f"**Rɪʟɪs    :** `{uname.release}`\n"
    softw += f"**Vᴇʀsɪ    :** `{uname.version}`\n"
    softw += f"**Mᴇsɪɴ    :** `{uname.machine}`\n"
    # Boot Time
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    softw += f"**Wᴀᴋᴛᴜ Hɪᴅᴜᴘ:** `{bt.day}/{bt.month}/{bt.year}  {bt.hour}:{bt.minute}:{bt.second}`\n"
    # CPU Cores
    cpuu = "**Iɴғᴏʀᴍᴀsɪ CPU**\n"
    cpuu += "**Pʜʏsɪᴄᴀʟ Cᴏʀᴇs   :** `" + \
        str(psutil.cpu_count(logical=False)) + "`\n"
    cpuu += "**Tᴏᴛᴀʟ Cᴏʀᴇs      :** `" + \
        str(psutil.cpu_count(logical=True)) + "`\n"
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    cpuu += f"**Mᴀx Fʀᴇǫᴜᴇɴᴄʏ    :** `{cpufreq.max:.2f}Mhz`\n"
    cpuu += f"**Mɪɴ Fʀᴇǫᴜᴇɴᴄʏ    :** `{cpufreq.min:.2f}Mhz`\n"
    cpuu += f"**Cᴜʀʀᴇɴᴛ Fʀᴇǫᴜᴇɴᴄʏ:** `{cpufreq.current:.2f}Mhz`\n\n"
    # CPU usage
    cpuu += "**CPU Usᴀɢᴇ Pᴇʀ Cᴏʀᴇ**\n"
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        cpuu += f"**Cᴏʀᴇ {i}  :** `{percentage}%`\n"
    cpuu += "**Tᴏᴛᴀʟ CPU Usᴀɢᴇ**\n"
    cpuu += f"**Sᴇᴍᴜᴀ Cᴏʀᴇ:** `{psutil.cpu_percent()}%`\n"
    # RAM Usage
    svmem = psutil.virtual_memory()
    memm = "**Mᴇᴍᴏʀʏ Dɪɢᴜɴᴀᴋᴀɴ**\n"
    memm += f"**Tᴏᴛᴀʟ     :** `{get_size(svmem.total)}`\n"
    memm += f"**Aᴠᴀɪʟᴀʙʟᴇ :** `{get_size(svmem.available)}`\n"
    memm += f"**Usᴇᴅ      :** `{get_size(svmem.used)}`\n"
    memm += f"**Pᴇʀᴄᴇɴᴛᴀɢᴇ:** `{svmem.percent}%`\n"
    # Bandwidth Usage
    bw = "**Bᴀɴᴅᴡɪᴛʜ Dɪɢᴜɴᴀᴋᴀɴ**\n"
    bw += f"**Uɴɢɢᴀʜ  :** `{get_size(psutil.net_io_counters().bytes_sent)}`\n"
    bw += f"**Dᴏᴡɴʟᴏᴀᴅ:** `{get_size(psutil.net_io_counters().bytes_recv)}`\n"
    help_string = f"{softw}\n"
    help_string += f"{cpuu}\n"
    help_string += f"{memm}\n"
    help_string += f"{bw}\n"
    help_string += "**Iɴғᴏʀᴍᴀsɪ Mᴇsɪɴ**\n"
    help_string += f"**Pʏᴛʜᴏɴ :** `{sys.version}`\n"
    help_string += f"**Tᴇʟᴇᴛʜᴏɴ :**`{__version__}`\n"
    help_string += f"**Pʏ-Aʏɪɪɴ :** `0.4.6`\n"
    help_string += f"**Aʏɪɪɴ-Vᴇʀsɪᴏɴ :** `{var.BOT_VER} [{HOSTED_ON}]`"
    await edit_or_reply(event, help_string)


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


@ayiin_cmd(pattern="sysd$")
async def sysdetails(sysd):
    if not sysd.text[0].isalpha() and sysd.text[0] not in ("/", "#", "@", "!"):
        try:
            fetch = await asyncrunapp(
                "neofetch",
                "--stdout",
                stdout=asyncPIPE,
                stderr=asyncPIPE,
            )

            stdout, stderr = await fetch.communicate()
            result = str(stdout.decode().strip()) + \
                str(stderr.decode().strip())

            await edit_or_reply(sysd, "`" + result + "`")
        except FileNotFoundError:
            await edit_or_reply(sysd, "**Install neofetch Terlebih dahulu!!**")


@ayiin_cmd(pattern="botver$")
async def bot_ver(event):
    if event.text[0].isalpha() or event.text[0] in ("/", "#", "@", "!"):
        return
    if which("git") is not None:
        ver = await asyncrunapp(
            "git",
            "describe",
            "--all",
            "--long",
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )
        stdout, stderr = await ver.communicate()
        verout = str(stdout.decode().strip()) + str(stderr.decode().strip())

        rev = await asyncrunapp(
            "git",
            "rev-list",
            "--all",
            "--count",
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )
        stdout, stderr = await rev.communicate()
        revout = str(stdout.decode().strip()) + str(stderr.decode().strip())

        await edit_or_reply(
            event,
            "✧ **Userbot Versi :** " f"`{verout}`" "\n✧ **Revisi :** " f"`{revout}`",
        )
    else:
        await edit_or_reply(
            event, "anda tidak memiliki git, Anda Menjalankan Bot - 'v1.beta.4'!"
        )


@ayiin_cmd(pattern="(?:alive|yinson)\\s?(.)?")
async def amireallyalive(alive):
    user = await alive.client.get_me()
    uptime = await get_readable_time((time.time() - StartTime))
    await alive.edit("😈")
    await asyncio.sleep(3)
    output = (
        f"**Tʜᴇ [Aʏɪɪɴ-Usᴇʀʙᴏᴛ](https://github.com/AyiinXd/Ayiin-Userbot)**\n\n"
        f"**{alive_text}**\n\n"
        f"╭✠╼━━━━━━━━━━━━━━━✠╮\n"
        f"{emoji} **Aʏɪɪɴ Vᴇʀsɪᴏɴ :** `{var.BOT_VER}`\n"
        f"{emoji} **Bᴏᴛ Uᴘᴛɪᴍᴇ :** `{uptime}`\n"
        f"{emoji} **Dᴇᴘʟᴏʏ Oɴ :** {HOSTED_ON}\n"
        f"{emoji} **Mᴏᴅᴜʟᴇs :** `{len(modules)} Modules` \n"
        f"{emoji} **Oᴡɴᴇʀ :** [{user.first_name}](tg://user?id={user.id}) \n"
        f"{emoji} **Pʏᴛʜᴏɴ Vᴇʀsɪᴏɴ :** `{python_version()}` \n"
        f"{emoji} **PʏTɢCᴀʟʟs Vᴇʀsɪᴏɴ :** `Unlimited` \n"
        f"{emoji} **Pʏ-Aʏɪɪɴ Vᴇʀsɪᴏɴ :** `0.4.6`\n"
        f"{emoji} **Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ :** `{version.__version__}` \n"
        "╰✠╼━━━━━━━━━━━━━━━✠╯\n\n"
    )
    if var.ALIVE_LOGO:
        try:
            logo = var.ALIVE_LOGO
            await alive.delete()
            await alive.client.send_file(alive.chat_id, logo, caption=output)
        except BaseException:
            await alive.edit(
                output
            )
            return
    else:
        await edit_or_reply(alive, output)


CMD_HELP.update(
    {
        "system": f"**Plugin : **`system`.\
        \n\n  »  **Perintah :** `{cmd}sysinfo`\
        \n  »  **Kegunaan : **Informasi sistem menggunakan neofetch mengirim sebagai gambar.\
        \n\n  »  **Perintah :** `{cmd}sysd`\
        \n  »  **Kegunaan : **Informasi sistem menggunakan neofetch.\
        \n\n\n  »  **Perintah :** `{cmd}botver`\
        \n  »  **Kegunaan : **Menampilkan versi userbot.\
        \n\n  »  **Perintah :** `{cmd}spc`\
        \n  »  **Kegunaan : **Menampilkan spesifikasi sistem secara lengkap.\
    "
    }
)


CMD_HELP.update(
    {
        "alive": f"**Plugin : **`alive`\
        \n\n  »  **Perintah :** `{cmd}alive` atau `{cmd}yinson`\
        \n  »  **Kegunaan : **Untuk melihat apakah bot Anda berfungsi atau tidak.\
    "
    }
)
