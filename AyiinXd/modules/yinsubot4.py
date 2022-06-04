# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport

from time import sleep

from AyiinXd import BLACKLIST_CHAT
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from Stringyins import get_string


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

@ayiin_cmd(pattern=r"ywc(?: |$)(.*)")
async def _(a):
    await a.edit(get_string("yins_1"))


@ayiin_cmd(pattern=r"jamet(?: |$)(.*)")
async def _(y):
    ayiin = await eor(y, get_string("yins_2"))
    sleep(1.5)
    await ayiin.edit(get_string("yins_3"))
    sleep(1.5)
    await ayiin.edit(get_string("yins_4"))
    sleep(1.5)
    await ayiin.edit(get_string("yins_5"))
    sleep(1.5)
    await ayiin.edit(get_string("yins_6"))
    sleep(1.5)
    await ayiin.edit(get_string("yins_7"))
    sleep(1.5)
    await ayiin.edit(get_string("yins_8"))
    sleep(1.5)
    await ayiin.edit(get_string("yins_9"))
    sleep(1.5)
    await ayiin.edit(get_string("yins_10"))
    sleep(1.5)
    await ayiin.edit(get_string("yins_11"))
    sleep(1.5)
    await ayiin.edit(get_string("yins_12"))


@ayiin_cmd(pattern=r"pp(?: |$)(.*)")
async def _(i):
    await eor(i, get_string("yins_13"))


@ayiin_cmd(pattern=r"dp(?: |$)(.*)")
async def _(i):
    await eor(i, get_string("yins_14"))


@ayiin_cmd(pattern=r"so(?: |$)(.*)")
async def _(n):
    await eor(n, get_string("yins_15"))


@ayiin_cmd(pattern=r"nb(?: |$)(.*)")
async def _(x):
    if event.chat_id in BLACKLIST_CHAT:
        return await eod(x, get_string("ayiin_1"), time=50)
    await eor(x, get_string("yins_16"))
    await x.delete()


@ayiin_cmd(pattern=r"met(?: |$)(.*)")
async def _(d):
    await eor(d, get_string("yins_17"))


@ayiin_cmd(pattern=r"war(?: |$)(.*)")
async def _(a):
    await eor(a, get_string("yins_18"))
    await a.delete()


@ayiin_cmd(pattern=r"wartai(?: |$)(.*)")
async def _(y):
    await eor(y, get_string("yins_19"))
    await y.delete()


@ayiin_cmd(pattern=r"kismin(?: |$)(.*)")
async def _(i):
    await eor(i, get_string("yins_20"))
    await i.delete()


@ayiin_cmd(pattern=r"ded(?: |$)(.*)")
async def _(i):
    await eor(i, get_string("yins_21"))
    await i.delete()


@ayiin_cmd(pattern=r"sokab(?: |$)(.*)")
async def _(n):
    await eor(n, get_string("yins_22"))
    await n.delete()


@ayiin_cmd(pattern=r"gembel(?: |$)(.*)")
async def _(x):
    await eor(x, get_string("yins_23"))
    await x.delete()


@ayiin_cmd(pattern=r"cuih(?: |$)(.*)")
async def _(d):
    await eor(d, get_string("yins_24"))
    await d.delete()


@ayiin_cmd(pattern=r"dih(?: |$)(.*)")
async def _(y):
    await eor(y, get_string("yins_25"))
    await y.delete()


@ayiin_cmd(pattern=r"gcs(?: |$)(.*)")
async def _(i):
    if i.chat_id in BLACKLIST_CHAT:
        return await eod(i, get_string("ayiin_1"))
    await eor(i, get_string("yins_26"))
    await i.delete()


@ayiin_cmd(pattern=r"skb(?: |$)(.*)")
async def _(n):
    await eor(n, get_string("yins_27"))
    await n.delete()


@ayiin_cmd(pattern=r"virtual(?: |$)(.*)")
async def _(s):
    ayiin = await eor(s, get_string("yins_28"))
    sleep(1.5)
    await ayiin.edit(get_string("yins_29"))
    sleep(1.5)
    await ayiin.edit(get_string("yins_30"))
    sleep(1.5)
    await ayiin.edit(get_string("yins_31"))
    sleep(1.5)
    await ayiin.edit(get_string("yins_32"))
    sleep(1.5)
    await ayiin.edit(get_string("yins_33"))
    sleep(1.5)
    await ayiin.edit(get_string("yins_34"))
    sleep(1.5)
    await ayiin.edit(get_string("yins_35"))


CMD_HELP.update(
    {
        "yinsubot4": f"**Plugin : **`war`\
        \n\n  »  **Perintah :** `{cmd}jamet`\
        \n  »  **Kegunaan : **Menghina Jamet telegram\
        \n\n  »  **Perintah :** `{cmd}pp`\
        \n  »  **Kegunaan : **Menghina Jamet telegram yang ga pake foto profil\
        \n\n  »  **Perintah :** `{cmd}dp`\
        \n  »  **Kegunaan : **Menghina Jamet muka hina!\
        \n\n  »  **Perintah :** `{cmd}so`\
        \n  »  **Kegunaan : **Ngeledek orang sokab\
        \n\n  »  **Perintah :** `{cmd}nb`\
        \n  »  **Kegunaan : **Ngeledek orang norak baru pake bot\
        \n\n  »  **Perintah :** `{cmd}skb`\
        \n  »  **Kegunaan : **Ngeledek orang sokab versi 2\
        \n\n  »  **Perintah :** `{cmd}met`\
        \n  »  **Kegunaan : **Ngeledek si jamet caper\
        \n\n  »  **Perintah :** `{cmd}war`\
        \n  »  **Kegunaan : **Ngeledek orang so keras ngajak war\
        \n\n  »  **Perintah :** `{cmd}wartai`\
        \n  »  **Kegunaan : **Ngeledek orang so ketrigger ngajak cod minta sharelok\
        \n\n  »  **Perintah :** `{cmd}kismin`\
        \n  »  **Kegunaan : **Ngeledek orang kismin so jagoan di tele\
        \n\n  »  **Perintah :** `{cmd}ded`\
        \n  »  **Kegunaan : **Nyuruh orang mati aja goblok wkwk\
        \n\n  »  **Perintah :** `{cmd}sokab`\
        \n  »  **Kegunaan : **Ngeledek orang so kenal so dekat padahal kga kenal goblok\
        \n\n  »  **Perintah :** `{cmd}gembel`\
        \n  »  **Kegunaan : **Ngeledek bapaknya si jamet\
        \n\n  »  **Perintah :** `{cmd}cuih`\
        \n  »  **Kegunaan : **Ngeludahin keluarganya satu satu wkwk\
        \n\n  »  **Perintah :** `{cmd}dih`\
        \n  »  **Kegunaan : **Ngeledek anak haram\
        \n\n  »  **Perintah :** `{cmd}gcs`\
        \n  »  **Kegunaan : **Ngeledek gc sampah\
        \n\n  »  **Perintah :** `{cmd}virtual`\
        \n  »  **Kegunaan : **Ngeledek orang pacaran virtual\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
)
