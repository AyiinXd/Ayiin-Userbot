# Copyright (C) 2021 Kyy - Userbot
# Credit by kyy
# Recode by @AyiinXd


from time import sleep

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eor
from Stringyins import get_string


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


@ayiin_cmd(pattern=r"lipkol(?: |$)(.*)")
async def _(a):
    ayiin = await eor(a, get_string("yibot_51"))
    sleep(2)
    await ayiin.edit(get_string("yibot_52"))
    sleep(1)
    await ayiin.edit(get_string("yibot_53"))


# Create by myself @localheart


@ayiin_cmd(pattern=r"nakal(?: |$)(.*)")
async def _(y):
    ayiin = await eor(y, get_string("yibot_54"))
    sleep(1)
    await ayiin.edit(get_string("yibot_55"))
    sleep(1)
    await ayiin.edit(get_string("yibot_56"))
    sleep(1)
    await ayiin.edit(get_string("yibot_57"))


@ayiin_cmd(pattern=r"favboy(?: |$)(.*)")
async def _(i):
    ayiin = await eor(i, get_string("yibot_58"))
    sleep(1.5)
    await ayiin.edit(get_string("yibot_59"))
    sleep(1.5)
    await ayiin.edit(get_string("yibot_60"))
    sleep(1.5)
    await ayiin.edit(get_string("yibot_61"))
    sleep(1.5)
    await ayiin.edit(get_string("yibot_62"))


@ayiin_cmd(pattern=r"favgirl(?: |$)(.*)")
async def _(i):
    ayiin = await eor(i, get_string("yibot_63"))
    sleep(2)
    await ayiin.edit(get_string("yibot_64"))
    sleep(2)
    await ayiin.edit(get_string("yibot_65"))
    sleep(2)
    await ayiin.edit(get_string("yibot_66"))
    sleep(2)
    await ayiin.edit(get_string("yibot_67"))


@ayiin_cmd(pattern=r"canlay(?: |$)(.*)")
async def _(n):
    ayiin = await eor(n, get_string("yibot_68"))
    sleep(2)
    await ayiin.edit(get_string("yibot_69"))
    sleep(2)
    await ayiin.edit(get_string("yibot_70"))
    sleep(2)
    await ayiin.edit(get_string("yibot_71"))
    sleep(2)
    await ayiin.edit(get_string("yibot_72"))


@ayiin_cmd(pattern=r"ganlay(?: |$)(.*)")
async def _(x):
    ayiin = await eor(x, get_string("yibot_73"))
    sleep(2)
    await ayiin.edit(get_string("yibot_69"))
    sleep(2)
    await ayiin.edit(get_string("yibot_70"))
    sleep(2)
    await ayiin.edit(get_string("yibot_71"))
    sleep(2)
    await ayiin.edit(get_string("yibot_72"))


@ayiin_cmd(pattern=r"ange(?: |$)(.*)")
async def _(d):
    ayiin = await eor(d, get_string("yibot_74"))
    sleep(1)
    await ayiin.edit(get_string("yibot_75"))
    sleep(1)
    await ayiin.edit(get_string("yibot_76"))


CMD_HELP.update(
    {
        "yinsubot2": f"**Plugin : **`yinsubot2`\
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
