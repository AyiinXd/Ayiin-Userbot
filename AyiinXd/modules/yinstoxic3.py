# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


from time import sleep

from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd

from . import cmd


@ayiin_cmd(pattern="ceking(?: |$)(.*)")
async def _(mnghna):
    Ayiin = await mnghna.edit("**GIGI KUNING MATA MERAH BADAN KURUS CEKING EMANG PANTES...**")
    sleep(3)
    await Ayiin.edit("**DI KENCINGIN JAHANAM**")
    sleep(3)
    await Ayiin.edit("**ORANG KAYA LUH ITU...**")
    sleep(3)
    await Ayiin.edit("**CUMAN SEMPIT SEMPITIN ISI DUNIA DOANG KONTOL SEMPAK**")
    sleep(3)
    await Ayiin.edit("**GUA KASIH TAU NIH YAH USUS LUH TUH UDAH MELINTIR KONTOL**")
    sleep(3)
    await Ayiin.edit("**KERONGKONGAN LUH ITU UDAH RUSAK TOLOL...**")
    sleep(3)
    await Ayiin.edit("**MASIH AJA MAKSAIN BUAT ADU ROASTING AMA GUA BEGO BANGET SIH LUH...**")


@ayiin_cmd(pattern="hina(?: |$)(.*)")
async def _(war):
    Kon = await war.edit("**IZIN PANTUN BANG...**")
    sleep(3)
    await Kon.edit("**KETEMU SI MAMAS DIAJAKIN KE CIBINONG...**")
    sleep(3)
    await Kon.edit("**PULANG NYE DIANTERIN MAKE KOPAJA...**")
    sleep(3)
    await Kon.edit("**EH BOCAH AMPAS TITISAN DAJJAL...**")
    sleep(3)
    await Kon.edit("**MUKA HINA KEK ODONG ODONG**")
    sleep(3)
    await Kon.edit("**GA USAH SO KERAS DEH LU KALO MENTAL BLOM SEKERAS BAJA...**")
    sleep(3)
    await Kon.edit("**LUH ITU MANUSIA...**")
    sleep(3)
    await Kon.edit("**MANUSIA HINA YANG DI CIPTAKAN DENGAN SECARA HINA**")
    sleep(3)
    await Kon.edit("**MANUSIA HINA YANG DI CIPTAKAN DENGAN SECARA HINA EMANG PANTES UNTUK DI HINA HINA...**")


@ayiin_cmd(pattern="ngaca(?: |$)(.*)")
async def _(mikir):
    Yins = await mikir.edit("**IZIN NUMPANG PANTUN BANG...**")
    sleep(3)
    await Yins.edit("**BELI SEPATU KACA KE CHINA...**")
    sleep(3)
    await Yins.edit("**ASEEEKKKK 🤪**")
    sleep(3)
    await Yins.edit("**NGACA DULU BARU NGEHINA KONTOL...**")
    sleep(3)
    await Yins.edit("**UDAH BULUK ITEM PENDEK BERPONI BAJU KEGEDEAN KAYAK JAMET**")
    sleep(3)
    await Yins.edit("**UDAH BULUK ITEM PENDEK BERPONI BAJU KEGEDEAN KAYAK JAMET SOK-SOK AN MAU NGEHINA GUA KONTOL**")
    sleep(3)
    await Yins.edit("**KENA KAN MENTAL LU...**")


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "yinstoxic3": f"**Plugin : **`yinstoxic3`\
        \n\n  »  **Perintah :** `{cmd}ceking`\
        \n  »  **Kegunaan : **Cobain Sendiri Dah Tod.\
        \n\n  »  **Perintah :** `{cmd}hina`\
        \n  »  **Kegunaan : **Cobain Sendiri Dah Tod.\
        \n\n  »  **Perintah :** `{cmd}ngaca`\
        \n  »  **Kegunaan : **Cobain Sendiri Dah Tod.\
    "
    }
  )
