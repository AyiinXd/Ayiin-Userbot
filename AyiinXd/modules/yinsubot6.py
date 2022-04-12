# 🍀 © @tofik_dn
# ⚠️ Do not remove credits
# Recode by : @AyiinXd


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

import random

from telethon.tl.types import InputMessagesFilterVideo

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, owner
from AyiinXd.utils import ayiin_cmd


@ayiin_cmd(pattern="bokp$")
async def _(ayiin):
    try:
        asuyins = [
            asupan
            async for asupan in ayiin.client.iter_messages(
                "@bokep_yins_xd", filter=InputMessagesFilterVideo
            )
        ]
        awake = await ayiin.client.get_me()
        await ayiin.client.send_file(
            ayiin.chat_id,
            file=random.choice(asuyins),
            caption=f"Kena Tipu Ya Tod [{owner}](tg://user?id={awake.id})",
        )
        await ayiin.delete()
    except Exception:
        await ayiin.edit("**Maaf tod tidak bisa menemukan video asupan.**")


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "yinsubot6": f"**Plugin : **yinsubot6\
        \n\n  »  **Perintah :** {cmd}bokp\
        \n  »  **Kegunaan : **Untuk Mengirim bokp tiktok secara random.\
    "
    }
)
