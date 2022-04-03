
from telethon import events
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, bot
from AyiinXd.utils import edit_or_reply, ayiin_cmd
from telethon.errors.rpcerrorlist import YouBlockedUserError
import asyncio


@ayiin_cmd(pattern=r"tm(?: |$)(.*)")
async def _(event):
    chat = "@TempMailBot"
    yins = await edit_or_reply(event, "Sabar Tod Sedang Memprosess...")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(
                incoming=True,
                from_users=220112646
            )
            )
            await conv.send_message("/start")
            await asyncio.sleep(1)
            await conv.send_message("/create")
            response = await response
            ayiinuserbot = ((response).reply_markup.rows[2].buttons[0].url)
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await yins.edit("`Mohon Maaf, Silahkan Buka` @TempMailBot `Lalu Tekan Start dan Coba Lagi.`")
            return
        await event.edit(f"**YINS TEMPMAIL** ~ `{response.message.message}`\n\n[KLIK DISINI UNTUK VERIFIKASI]({ayiinuserbot})")

CMD_HELP.update(
    {
        "tempmail": f"**Plugin : **`tempmail`\
        \n\n  »  **Perintah :** `{cmd}tm`\
        \n  »  **Kegunaan : Mendapatkan Email Gratis Dari Temp Mail"}
)
