# Copyright (C) 2021 Kyy - Userbot
# Created by Kyy
# Jangan hapus credit Anj!!!
#
# Recode by : @AyiinXd

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


from time import sleep

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eor
from Stringyins import get_string


@ayiin_cmd(pattern=r"sadboy(?: |$)(.*)")
async def _(a):
    ayiin = eor(a, get_string("yibot_1"))
    sleep(2)
    await ayiin.edit(get_string("yibot_2"))
    sleep(1)
    await ayiin.edit(get_string("yibot_3"))

# Create by myself @localheart


@ayiin_cmd(pattern=r"lah(?: |$)(.*)")
async def _(y):
    ayiin = await eor(y, get_string("yibot_4"))
    sleep(1)
    await ayiin.edit(get_string("yibot_5"))
    sleep(1)
    await ayiin.edit(get_string("yibot_6"))
    sleep(1)
    await ayiin.edit(get_string("yibot_7"))


@ayiin_cmd(pattern=r"sok(?: |$)(.*)")
async def _(i):
    ayiin = await eor(i, get_string("yibot_8"))
    sleep(2)
    await ayiin.edit(get_string("yibot_9"))
    sleep(2)
    await ayiin.edit(get_string("yibot_10"))
    sleep(2)
    await ayiin.edit(get_string("yibot_11"))
    sleep(2)
    await ayiin.edit(get_string("yibot_12"))


@ayiin_cmd(pattern=r"wah(?: |$)(.*)")
async def _(i):
    ayiin = await eor(i, get_string("yibot_13"))
    sleep(2)
    await ayiin.edit(get_string("yibot_14"))
    sleep(2)
    await ayiin.edit(get_string("yibot_15"))
    sleep(2)
    await ayiin.edit(get_string("yibot_16"))
    sleep(2)
    await ayiin.edit(get_string("yibot_17"))
    sleep(2)
    await ayiin.edit(get_string("yibot_18"))
    sleep(3)
    await ayiin.edit(get_string("yibot_19"))


@ayiin_cmd(pattern=r"alay(?: |$)(.*)")
async def _(n):
    ayiin = await eor(n, get_string("yibot_20"))
    sleep(2)
    await ayiin.edit(get_string("yibot_21"))
    sleep(2)
    await ayiin.edit(get_string("yibot_22"))
    sleep(2)
    await ayiin.edit(get_string("yibot_23"))
    sleep(2)
    await ayiin.edit(get_string("yibot_24"))


@ayiin_cmd(pattern=r"erpe(?: |$)(.*)")
async def _(x):
    ayiin = await eor(x, get_string("yibot_25"))
    sleep(1)
    await ayiin.edit(get_string("yibot_26"))
    sleep(1)
    await ayiin.edit(get_string("yibot_27"))
    sleep(1)
    await ayiin.edit(get_string("yibot_28"))
    sleep(1)
    await ayiin.edit(get_string("yibot_29"))
    sleep(1)
    await ayiin.edit(get_string("yibot_30"))
    sleep(1)
    await ayiin.edit(get_string("yibot_31"))
    sleep(1)
    await ayiin.edit(get_string("yibot_32"))
    sleep(1)
    await ayiin.edit(get_string("yibot_33"))


@ayiin_cmd(pattern=r"tittle(?: |$)(.*)")
async def _(d):
    ayiin = await eor(d, get_string("yibot_34"))
    sleep(2)
    await ayiin.edit(get_string("yibot_35"))
    sleep(2)
    await ayiin.edit(get_string("yibot_36"))
    sleep(2)
    await ayiin.edit(get_string("yibot_37"))
    sleep(2)
    await ayiin.edit(get_string("yibot_38"))
    sleep(2)
    await ayiin.edit(get_string("yibot_39"))
    sleep(2)
    await ayiin.edit(get_string("yibot_40"))
    sleep(2)
    await ayiin.edit(get_string("yibot_41"))
    sleep(2)
    await ayiin.edit(get_string("yibot_42"))
    sleep(2)
    await ayiin.edit(get_string("yibot_43"))
    sleep(2)
    await ayiin.edit(get_string("yibot_44"))
    sleep(2)
    await ayiin.edit(get_string("yibot_45"))
    sleep(2)
    await ayiin.edit(get_string("yibot_46"))
    sleep(4)
    await ayiin.edit(get_string("yibot_47"))
    sleep(2)
    await ayiin.edit(get_string("yibot_48"))
    sleep(3)
    await ayiin.edit(get_string("yibot_49"))
    sleep(3)
    await ayiin.edit(get_string("yibot_50"))


CMD_HELP.update(
    {
        "yinsubot": f"**Plugin : **`yinsubot`\
        \n\n  »  **Perintah :** `{cmd}sadboy`\
        \n  »  **Kegunaan : **Gombalan sad\
        \n\n  »  **Perintah :** `{cmd}wah`\
        \n  »  **Kegunaan : **Ngeledek orang sok war\
        \n\n  »  **Perintah :** `{cmd}sok`\
        \n  »  **Kegunaan : **Ngeledek orang sok keras\
        \n\n  »  **Perintah :** `{cmd}lah`\
        \n  »  **Kegunaan : **Engga ketrigger tod\
        \n\n  »  **Perintah :** `{cmd}alay`\
        \n  »  **Kegunaan : **Ngatain orang spam bot\
        \n\n  »  **Perintah :** `{cmd}erpe`\
        \n  »  **Kegunaan : **Ngatain anak erpe\
        \n\n  »  **Perintah :** `{cmd}tittle`\
        \n  »  **Kegunaan : **Ngatain jamet haus tittle\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
)
