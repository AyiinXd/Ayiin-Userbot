# nyenyenyenye
# FROM skyzu-userbot <https://github.com/Skyzu/skyzu-userbot>
# port by koala🐨/@manusiarakitann

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest

from userbot import CMD_HELP
from userbot.events import register

chat = "@BotFather"

@register(outgoing=True, pattern="^.botbaru ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text, username = event.pattern_match.group(1).split()

else:
        await event.edit("`Masukan Yang Benar Cok Biar Bisa Bikin Bot!!`")
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
        "botfather": ".botbaru\
    \nUntuk Membuat Bot Dari Botfather, .botbaru  < bot_name > <bot_username >  ."
    }
)
