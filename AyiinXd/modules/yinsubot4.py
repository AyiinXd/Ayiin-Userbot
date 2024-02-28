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

from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd

from import cmd


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

@ayiin_cmd(pattern=r"ywc(?: |$)(.*)")
async def _(a):
    await a.edit("**Oke Sama-sama**")


@ayiin_cmd(pattern=r"jamet(?: |$)(.*)")
async def _(y):
    ayiin = await y.edit("**WOIII**")
    sleep(1.5)
    await ayiin.edit("**JAMETTT**")
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
async def _(i):
    await i.edit("**PASANG PP DULU GOBLOK,BIAR ORANG-ORANG PADA TAU BETAPA HINA NYA MUKA LU 😆**")


@ayiin_cmd(pattern=r"dp(?: |$)(.*)")
async def _(i):
    await i.edit("**MUKA LU HINA, GAUSAH SOK KERAS YA ANJENGG!!**")


@ayiin_cmd(pattern=r"so(?: |$)(.*)")
async def _(n):
    await n.edit("**GAUSAH SOKAB SAMA GUA GOBLOK, LU BABU GA LEVEL!!**")


@ayiin_cmd(pattern=r"met(?: |$)(.*)")
async def _(d):
    await d.edit("**NAMANYA JUGA JAMET CAPER SANA SINI BUAT CARI NAMA**")
  

@ayiin_cmd(pattern=r"war(?: |$)(.*)")
async def _(a):
    await a.edit("**WAR WAR PALAK BAPAK KAU WAR, SOK KERAS BANGET GOBLOK, DI TONGKRONGAN JADI BABU, DI TELE SOK JAGOAN...**")


@ayiin_cmd(pattern=r"wartai(?: |$)(.*)")
async def _(y):
    await y.edit("**WAR WAR TAI ANJING, KETRIGGER MINTA SHARELOK LU KIRA MAU COD-AN GOBLOK, BACOTAN LU AJA KGA ADA KERAS KERASNYA GOBLOK**")


@ayiin_cmd(pattern=r"kismin(?: |$)(.*)")
async def _(i):
    await i.edit("**CUIHHHH, MAKAN AJA MASIH NGEMIS LO GOBLOK, JANGAN SO NINGGI YA KONTOL GA KEREN LU KEK GITU GOBLOK!!**")
  

@ayiin_cmd(pattern=r"ded(?: |$)(.*)")
async def _(i):
    await i.edit("**MATI AJA LU GOBLOK, GAGUNA LU HIDUP DI BUMI**")


@ayiin_cmd(pattern=r"sokab(?: |$)(.*)")
async def _(n):
    await n.edit("**SOKAB BET LU GOBLOK, KAGA ADA ISTILAH NYA BAWAHAN TEMENAN AMA BOS!!**")


@ayiin_cmd(pattern=r"gembel(?: |$)(.*)")
async def _(x):
    await x.edit("**MUKA BAPAK LU KEK KELAPA SAWIT ANJING, GA USAH NGATAIN ORANG, MUKA LU AJA KEK GEMBEL TEXAS GOBLOK!!**")


@ayiin_cmd(pattern=r"cuih(?: |$)(.*)")
async def _(d):
    await await d.edit("**GAK KEREN LO KEK BEGITU GOBLOK, KELUARGA LU BAWA SINI GUA LUDAHIN SATU-SATU. CUIHH!!!**")


@ayiin_cmd(pattern=r"dih(?: |$)(.*)")
async def _(y):
    await y.edit("**DIHHH NAJISS ANAK HARAM LO GOBLOK, JANGAN BELAGU DIMARI KAGA KEREN LU KEK BGITU TOLOL!**"))


@ayiin_cmd(pattern=r"skb(?: |$)(.*)")
async def _(n):
    await n.edit("**EMANG KITA KENAL? KAGA GOBLOK SOKAB BANGET LU GOBLOK**")


@ayiin_cmd(pattern=r"virtual(?: |$)(.*)")
async def _(s):
    ayiin = await s.edit("**OOOO... INI YANG VIRTUAL**")
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
        "yinsubot4": f"**Plugin : **`Ayiin-Userbot`\
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
