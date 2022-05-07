# Ported by Fariz (Flicks-Userbot)

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, bot
from AyiinXd.ayiin import ayiin_cmd, edit_or_reply, edit_delete


@ayiin_cmd(pattern="truth(?: |$)(.*)")
async def _(event):
    ayiin = await edit_or_reply(event, "Mengirim pesan truth...")
    async with bot.conversation("@truthordares_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1335899453)
            )
            await conv.send_message("/truth")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await edit_delete(ayiin, "Harap unblock `@truthordares_bot` dan coba lagi")
            return
        await ayiin.edit(f"**Pesan truth**\n\n{response.message.message}")


@ayiin_cmd(pattern="dare(?: |$)(.*)")
async def _(event):
    ayiin = await edit_or_reply(event, "Mengirim pesan dare...")
    async with bot.conversation("@truthordares_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1335899453)
            )
            await conv.send_message("/dare")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await edit_delete(ayiin, "Harap unblock `@truthordares_bot` dan coba lagi")
            return
        await ayiin.edit(f"**Pesan dare**\n\n{response.message.message}")


@ayiin_cmd(pattern="spill(?: |$)(.*)")
async def _(event):
    xd = await edit_or_reply(event, "Mengirim pesan spill...")
    async with bot.conversation("@Spillgame_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1361222893)
            )
            await conv.send_message("/spill")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await edit_delete(event, "Harap unblock `@Spillgame_bot` dan coba lagi")
            return
        await xd.edit(f"**Pesan spill**\n\n{response.message.message}")


CMD_HELP.update(
    {
        "truth_dare": f"**Plugin :** truth_dare\
        \n\n  »  **Perintah :** `{cmd}truth`\
        \n  »  **Kegunaan : **Untuk mengirim pesan truth.\
        \n\n  »  **Perintah :** `{cmd}dare`\
        \n  »  **Kegunaan : **Untuk mengirim pesan dare.\
        \n\n  »  **Perintah :** `{cmd}spill`\
        \n  »  **Kegunaan : **Untuk Pertanyaan.\
    "
    }
)
