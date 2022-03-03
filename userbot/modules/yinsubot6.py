# 🍀 © @tofik_dn
# ⚠️ Do not remove credits


from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import ayiin_cmd
import random
from userbot import owner
from telethon.tl.types import InputMessagesFilterVideo


@ayiin_cmd(pattern="bokp$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@YinsAsuCache", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"Kena Tipu Ya Tod [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("**Maaf tod tidak bisa menemukan video asupan.**")


CMD_HELP.update(
    {
        "yinsubot6": f"**Plugin : **yinsubot6\
        \n\n  •  **Syntax :** {cmd}bokp\
        \n  •  **Function : **Untuk Mengirim bokp secara random.\
    "
    }
)