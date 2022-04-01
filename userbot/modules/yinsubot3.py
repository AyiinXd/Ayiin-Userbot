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

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, ayiin_cmd


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


@ayiin_cmd(pattern=r"yins(?: |$)(.*)")
async def _(event):
    ayiin = await edit_or_reply(event, "𝙃𝙖𝙞 𝙋𝙚𝙧𝙠𝙚𝙣𝙖𝙡𝙠𝙖𝙣 𝙉𝙖𝙢𝙖 𝙂𝙪𝙖 𝘼𝙮𝙞𝙞𝙣")
    sleep(3)
    await ayiin.edit("23 𝙏𝙖𝙝𝙪𝙣")
    sleep(2)
    await ayiin.edit("𝙏𝙞𝙣𝙜𝙜𝙖𝙡 𝘿𝙞 𝘽𝙖𝙡𝙞...")
    sleep(3)
    await ayiin.edit("𝙊𝙬𝙣𝙚𝙧 𝘿𝙖𝙧𝙞 𝘼𝙮𝙞𝙞𝙣-𝙐𝙨𝙚𝙧𝙗𝙤𝙩, 𝙎𝙖𝙡𝙖𝙢 𝙆𝙚𝙣𝙖𝙡 😁")
# Create by myself @AyiinXd


@ayiin_cmd(pattern=r"sayang(?: |$)(.*)")
async def _(event):
    ayiin = await edit_or_reply(event, "𝘼𝙠𝙪 𝘾𝙪𝙢𝙖 𝙈𝙖𝙪 𝘽𝙞𝙡𝙖𝙣𝙜 👉👈")
    sleep(3)
    await ayiin.edit("𝘼𝙠𝙪 𝙎𝙖𝙮𝙖𝙣𝙜 𝙆𝙖𝙢𝙪 😘")
    sleep(1)
    await ayiin.edit("𝙈𝙪𝙖𝙖𝙘𝙘𝙝𝙝𝙝 😘💕")
# Create by myself @AyiinXd


@ayiin_cmd(pattern=r"semangat(?: |$)(.*)")
async def _(event):
    ayiin = await edit_or_reply(event, "𝘼𝙥𝙖𝙥𝙪𝙣 𝙔𝙖𝙣𝙜 𝙏𝙚𝙧𝙟𝙖𝙙𝙞")
    sleep(3)
    await ayiin.edit("𝙏𝙚𝙩𝙖𝙥𝙡𝙖𝙝 𝘽𝙚𝙧𝙣𝙖𝙥𝙖𝙨")
    sleep(1)
    await ayiin.edit("𝘿𝙖𝙣 𝙎𝙚𝙡𝙖𝙡𝙪 𝘽𝙚𝙧𝙨𝙮𝙪𝙠𝙪𝙧")
# Create by myself @AyiinXd


@ayiin_cmd(pattern=r"mengeluh(?: |$)(.*)")
async def _(event):
    ayiin = await edit_or_reply(event, "𝘼𝙥𝙖𝙥𝙪𝙣 𝙔𝙖𝙣𝙜 𝙏𝙚𝙧𝙟𝙖𝙙𝙞")
    sleep(3)
    await ayiin.edit("𝙏𝙚𝙩𝙖𝙥𝙡𝙖𝙝 𝙈𝙚𝙣𝙜𝙚𝙡𝙪𝙝")
    sleep(1)
    await ayiin.edit("𝘿𝙖𝙣 𝙎𝙚𝙡𝙖𝙡𝙪 𝙋𝙪𝙩𝙪𝙨 𝘼𝙨𝙖")
# Create by myself @AyiinXd


CMD_HELP.update(
    {
        "yinsubot3": f"**Plugin : **`yinsubot3`\
        \n\n  •  **Syntax :** `{cmd}yins`\
        \n  •  **Function : **Perkenalan diri Yins\
        \n\n  •  **Syntax :** `{cmd}sayang`\
        \n  •  **Function : **Bucin\
        \n\n  •  **Syntax :** `{cmd}semangat`\
        \n  •  **Function : **Memberikan semangat!\
        \n\n  •  **Syntax :** `{cmd}mengeluh`\
        \n  •  **Function : **Ngeledek\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
)
