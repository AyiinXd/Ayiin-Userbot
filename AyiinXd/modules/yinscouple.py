# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport

from secrets import choice
from telethon.tl.types import InputMessagesFilterPhotos

from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eor

from . import cmd

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


@ayiin_cmd(pattern="couple(?: |$)(.*)")
async def couple(bucin):
    copl = await eor(bucin, '**Memproses...**')
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
            file=choice(bucinan),
            caption=f"Ambil Ni Pp Bucin Lu [{cang.first_name}](tg://user?id={cang.id})"
        )
        await copl.delete()
    except Exception:
        await copl.edit("**[ᴇʀʀᴏʀ]** Maaf Tod Gagal Dikarenakan Lu Jomblo...")


CMD_HELP.update(
    {
        "yinscouple": f"**Plugin :** `yinscouple`\
        \n\n  »  **Perintah :** `{cmd}couple`\
        \n  »  **Kegunaan :** __Untuk Mendapatkan Foto Couple Secara Random.__\
    "
    }
)
