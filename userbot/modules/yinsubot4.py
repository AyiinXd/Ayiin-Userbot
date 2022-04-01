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

from userbot import BLACKLIST_CHAT
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import ayiin_cmd, edit_or_reply, edit_delete


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

@ayiin_cmd(pattern=r"ywc(?: |$)(.*)")
async def _(event):
    yins = await edit_or_reply(event, "**Ok Sama Sama**")
    await yins.edit("**Ok Sama Sama 😘**")


@ayiin_cmd(pattern=r"jamet(?: |$)(.*)")
async def _(event):
    ayiin = await edit_or_reply(event, "**WOII**")
    sleep(1.5)
    await ayiin.edit("**JAMET**")
    sleep(1.5)
    await ayiin.edit("**CUMA MAU BILANG**")
    sleep(1.5)
    await ayiin.edit("**GAUSAH SO ASIK**")
    sleep(1.5)
    await ayiin.edit("**EMANG KENAL?**")
    sleep(1.5)
    await ayiin.edit("**GAUSAH REPLY**")
    sleep(1.5)
    await ayiin.edit("**KITA BUKAN KAWAN**")
    sleep(1.5)
    await ayiin.edit("**GASUKA PC ANJING**")
    sleep(1.5)
    await ayiin.edit("**BOCAH KAMPUNG**")
    sleep(1.5)
    await ayiin.edit("**MENTAL TEMPE**")
    sleep(1.5)
    await ayiin.edit("**LEMBEK NGENTOT🔥**")


@ayiin_cmd(pattern=r"pp(?: |$)(.*)")
async def _(event):
    await edi_or_reply(event, "**PASANG PP DULU GOBLOK,BIAR ORANG-ORANG PADA TAU BETAPA HINA NYA MUKA LU 😆**")


@ayiin_cmd(pattern=r"dp(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**MUKA LU HINA, GAUSAH SOK KERAS YA ANJENGG!!**")


@ayiin_cmd(pattern=r"so(?: |$)(.*)")
async def _(event):
    await event.client.send_message(event, "**GAUSAH SOKAB SAMA GUA GOBLOK, LU BABU GA LEVEL!!**")


@ayiin_cmd(pattern=r"nb(?: |$)(.*)")
async def _(event):
    if event.chat_id in BLACKLIST_CHAT:
        return await edit_delete(event, "**Perintah ini Dilarang digunakan di Group ini**")
    await edit_or_reply(event, "**MAEN BOT MULU ALAY NGENTOTT, KESANNYA NORAK GOBLOK!!!**")
    await event.delete()


@ayiin_cmd(pattern=r"met(?: |$)(.*)")
async def _(event):
    await event.client.send_message(event, "**NAMANYA JUGA JAMET CAPER SANA SINI BUAT CARI NAMA**")


@ayiin_cmd(pattern=r"war(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**WAR WAR PALAK BAPAK KAU WAR, SOK KERAS BANGET GOBLOK, DI TONGKRONGAN JADI BABU, DI TELE SOK JAGOAN...**")
    await event.delete()


@ayiin_cmd(pattern=r"wartai(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**WAR WAR TAI ANJING, KETRIGGER MINTA SHARELOK LU KIRA MAU COD-AN GOBLOK, BACOTAN LU AJA KGA ADA KERAS KERASNYA GOBLOK**")
    await event.delete()


@ayiin_cmd(pattern=r"kismin(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**CUIHHHH, MAKAN AJA MASIH NGEMIS LO GOBLOK, JANGAN SO NINGGI YA KONTOL GA KEREN LU KEK GITU GOBLOK!!**")
    await event.delete()


@ayiin_cmd(pattern=r"ded(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**MATI AJA LU GOBLOK, GAGUNA LU HIDUP DI BUMI**")
    await event.delete()


@ayiin_cmd(pattern=r"sokab(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**SOKAB BET LU GOBLOK, KAGA ADA ISTILAH NYA BAWAHAN TEMENAN AMA BOS!!**")
    await event.delete()


@ayiin_cmd(pattern=r"gembel(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**MUKA BAPAK LU KEK KELAPA SAWIT ANJING, GA USAH NGATAIN ORANG, MUKA LU AJA KEK GEMBEL TEXAS GOBLOK!!**")
    await event.delete()


@ayiin_cmd(pattern=r"cuih(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**GAK KEREN LO KEK BEGITU GOBLOK, KELUARGA LU BAWA SINI GUA LUDAHIN SATU-SATU. CUIHH!!!**")
    await event.delete()


@ayiin_cmd(pattern=r"dih(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**DIHHH NAJISS ANAK HARAM LO GOBLOK, JANGAN BELAGU DIMARI KAGA KEREN LU KEK BGITU TOLOL!**")
    await event.delete()


@ayiin_cmd(pattern=r"gcs(?: |$)(.*)")
async def _(event):
    if event.chat_id in BLACKLIST_CHAT:
        return await edit_delete(event, "**Perintah ini Dilarang digunakan di Group ini**")
    await edit_or_reply(event, "**GC SAMPAH KAYA GINI, BUBARIN AJA GOBLOK!!**")
    await event.delete()


@ayiin_cmd(pattern=r"skb(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**EMANG KITA KENAL? KAGA GOBLOK SOKAB BANGET LU GOBLOK**")
    await event.delete()


@ayiin_cmd(pattern=r"virtual(?: |$)(.*)")
async def _(event):
    ayiin = await edit_or_reply(event, "**OOOO**")
    sleep(1.5)
    await ayiin.edit("**INI YANG VIRTUAL**")
    sleep(1.5)
    await ayiin.edit("**YANG KATANYA SAYANG BANGET**")
    sleep(1.5)
    await ayiin.edit("**TAPI TETEP AJA DI TINGGAL**")
    sleep(1.5)
    await ayiin.edit("**NI INGET**")
    sleep(1.5)
    await ayiin.edit("**TANGANNYA AJA GA BISA DI PEGANG**")
    sleep(1.5)
    await ayiin.edit("**APALAGI OMONGANNYA**")
    sleep(1.5)
    await ayiin.edit("**BHAHAHAHA**")
    sleep(1.5)
    await ayiin.edit("**KASIAN MANA MASIH MUDA**")


CMD_HELP.update(
    {
        "yinsubot4": f"**Plugin : **`war`\
        \n\n  •  **Syntax :** `{cmd}jamet`\
        \n  •  **Function : **Menghina Jamet telegram\
        \n\n  •  **Syntax :** `{cmd}pp`\
        \n  •  **Function : **Menghina Jamet telegram yang ga pake foto profil\
        \n\n  •  **Syntax :** `{cmd}dp`\
        \n  •  **Function : **Menghina Jamet muka hina!\
        \n\n  •  **Syntax :** `{cmd}so`\
        \n  •  **Function : **Ngeledek orang sokab\
        \n\n  •  **Syntax :** `{cmd}nb`\
        \n  •  **Function : **Ngeledek orang norak baru pake bot\
        \n\n  •  **Syntax :** `{cmd}skb`\
        \n  •  **Function : **Ngeledek orang sokab versi 2\
        \n\n  •  **Syntax :** `{cmd}met`\
        \n  •  **Function : **Ngeledek si jamet caper\
        \n\n  •  **Syntax :** `{cmd}war`\
        \n  •  **Function : **Ngeledek orang so keras ngajak war\
        \n\n  •  **Syntax :** `{cmd}wartai`\
        \n  •  **Function : **Ngeledek orang so ketrigger ngajak cod minta sharelok\
        \n\n  •  **Syntax :** `{cmd}kismin`\
        \n  •  **Function : **Ngeledek orang kismin so jagoan di tele\
        \n\n  •  **Syntax :** `{cmd}ded`\
        \n  •  **Function : **Nyuruh orang mati aja goblok wkwk\
        \n\n  •  **Syntax :** `{cmd}sokab`\
        \n  •  **Function : **Ngeledek orang so kenal so dekat padahal kga kenal goblok\
        \n\n  •  **Syntax :** `{cmd}gembel`\
        \n  •  **Function : **Ngeledek bapaknya si jamet\
        \n\n  •  **Syntax :** `{cmd}cuih`\
        \n  •  **Function : **Ngeludahin keluarganya satu satu wkwk\
        \n\n  •  **Syntax :** `{cmd}dih`\
        \n  •  **Function : **Ngeledek anak haram\
        \n\n  •  **Syntax :** `{cmd}gcs`\
        \n  •  **Function : **Ngeledek gc sampah\
        \n\n  •  **Syntax :** `{cmd}virtual`\
        \n  •  **Function : **Ngeledek orang pacaran virtual\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
)
