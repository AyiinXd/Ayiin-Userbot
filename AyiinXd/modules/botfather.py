# nyenyenyenye
# FROM skyzu-userbot <https://github.com/Skyzu/skyzu-userbot>
# port by koala🐨/@manusiarakitann

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest


from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd

from . import cmd

chat = "@BotFather"


@ayiin_cmd(pattern="buatbot(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text, username = event.pattern_match.group(1).split()

    else:
        await event.edit("**Yang Benerlah Kentod Biar Bisa Bikin Bot!!!**")
        return

    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/newbot")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await conv.send_message(username)
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete()
        except YouBlockedUserError:
            await event.client(UnblockRequest("93372553"))
            await conv.send_message("/newbot")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await conv.send_message(username)
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete()


CMD_HELP.update(
    {
        "botfather": f"**Plugin : **`botfather`\
        \n\n  »  **Perintah :** `{cmd}buatbot`\
        \n  »  **Kegunaan : **Buat Bot Baru Di Bot Father\
        \n\n**Untuk Membuat Bot Dari Bot Father, Ketik** `{cmd}buatbot < bot_name > < bot_username >`\
    "
    }
)
