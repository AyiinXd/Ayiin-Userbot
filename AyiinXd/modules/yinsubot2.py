# Copyright (C) 2021 Kyy - Userbot
# Credit by kyy
# Recode by @AyiinXd


from time import sleep

from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd

from . import cmd

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


@ayiin_cmd(pattern=r"lipkol(?: |$)(.*)")
async def _(a):
    ayiin = await a.edit("**Ayaaang** 🥺")
    sleep(2)
    await ayiin.edit("**Kangeeen** 👉👈")
    sleep(1)
    await ayiin.edit("**Pingiinn Slipkool Yaaang** 🥺👉👈")


# Create by myself @localheart


@ayiin_cmd(pattern=r"nakal(?: |$)(.*)")
async def _(y):
    ayiin = await y.edit("**Ayaaang Ih** 🥺")
    sleep(1)
    await ayiin.edit("**Nakal Banget Dah Ayang** 🥺")
    sleep(1)
    await ayiin.edit("**Aku Gak Like Ayang** 😠")
    sleep(1)
    await ayiin.edit("**Pokoknya Aku Gak Like Ih** 😠")
  


@ayiin_cmd(pattern=r"favboy(?: |$)(.*)")
async def _(i):
    ayiin = await i.edit("**Duuhh Ada Cowo Ganteng** 👉👈")
    sleep(1.5)
    await ayiin.edit("**You Are My Favorit Boy** 😍")
    sleep(1.5)
    await ayiin.edit("**Kamu Harus Jadi Cowo Aku Ya** 😖")
    sleep(1.5)
    await ayiin.edit("**Pokoknya Harus Jadi Cowo Aku** 👉👈")
    sleep(1.5)
    await ayiin.edit("**Gak Boleh Ada Yang Lain** 😠")


@ayiin_cmd(pattern=r"favgirl(?: |$)(.*)")
async def _(i):
    ayiin = await i.edit("**Duuhh Ada Cewe Cantik** 👉👈")
    sleep(2)
    await ayiin.edit("**You Are My Favorit Girl** 😍")
    sleep(2)
    await ayiin.edit("**Kamu Harus Jadi Cewe Aku Ya** 😖")
    sleep(2)
    await ayiin.edit("**Pokoknya Harus Jadi Cewe Aku** 👉👈")
    sleep(2)
    await ayiin.edit("**Gak Boleh Ada Yang Lain** 😠")


@ayiin_cmd(pattern=r"canlay(?: |$)(.*)")
async def _(n):
    ayiin = await n.edit("**Eh Kamu Cantik-cantik**")
    sleep(2)
    await ayiin.edit("**Kok Alay Banget**")
    sleep(2)
    await ayiin.edit("**Spam Bot Mulu**")
    sleep(2)
    await ayiin.edit("**Baru Bikin Userbot Ya??**")
    sleep(2)
    await ayiin.edit("**Pantes Norak Xixixi**")


@ayiin_cmd(pattern=r"ganlay(?: |$)(.*)")
async def _(x):
    ayiin = await x.edit("**Eh Kamu Ganteng-ganteng**")
    sleep(2)
    await ayiin.edit("**Kok Alay Banget**")
    sleep(2)
    await ayiin.edit("**Spam Bot Mulu**")
    sleep(2)
    await ayiin.edit("**Baru Bikin Userbot Ya??**")
    sleep(2)
    await ayiin.edit("**Pantes Norak Xixixi**")


@ayiin_cmd(pattern=r"ange(?: |$)(.*)")
async def _(d):
    ayiin = await d.edit("**Ayanggg 😖**")
    sleep(1)
    await ayiin.edit("**Aku Ange 😫**")
    sleep(1)
    await ayiin.edit("**Ayuukk Picies Yang 🤤**")


CMD_HELP.update(
    {
        "yinsubot2": f"**Plugin : **`Ayiin-Userbot`\
        \n\n  »  **Perintah :** `{cmd}lipkol`\
        \n  »  **Kegunaan : **Ngajakin ayang slipkol\
        \n\n  »  **Perintah :** `{cmd}nakal`\
        \n  »  **Kegunaan : **Ga like ayang nakal\
        \n\n  »  **Perintah :** `{cmd}favboy`\
        \n  »  **Kegunaan : **Cowo idaman\
        \n\n  »  **Perintah :** `{cmd}favgirl`\
        \n  »  **Kegunaan : **Cewe idaman\
        \n\n  »  **Perintah :** `{cmd}canlay`\
        \n  »  **Kegunaan : **Ngatain si cantik alay\
        \n\n  »  **Perintah :** `{cmd}ganlay`\
        \n  »  **Kegunaan : **Ngatain si ganteng alay\
        \n\n  »  **Perintah :** `{cmd}ange`\
        \n  »  **Kegunaan : **Minta jatah ke ayang\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
  )
