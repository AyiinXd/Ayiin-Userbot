# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport

import random
from telethon.tl.types import InputMessagesFilterPhotos

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, owner
from userbot.utils import ayiin_cmd, edit_or_reply


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


@ayiin_cmd(pattern="couple(?: |$)(.*)")
async def couple(bucin):
    await edit_or_reply(bucin, "`Processing Tod...`")
    try:
        bucinan = [
            coupl
            async for coupl in bucin.client.iter_messages(
                "@ppayiinuserbot", filter=InputMessagesFilterPhotos
            )
        ]
        cang = await bucin.client.get_me()
        await bucin.client.send_file(
            bucin.chat_id,
            file=random.choice(bucinan),
            caption=f" Ambil Ni Pp Bucin Lu [{owner}](tg://user?id={cang.id})",
        )
        await bucin.delete()
    except Exception:
        await bucin.edit("**[ᴇʀʀᴏʀ]** Maaf Tod Gagal Dikarenakan Lu Jomblo...")


CMD_HELP.update(
    {
        "yinscouple": f"**Plugin :** `yinscouple`\
        \n\n • **Perintah :** `{cmd}couple`\
        \n • **Kegunaan :** __Untuk Mendapatkan Foto Couple Secara Random.__\
    "
    }
)
