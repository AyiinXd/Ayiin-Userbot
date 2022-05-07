# This is a troll indeed ffs *facepalm*
# Ported from xtra-telegram by @heyworld
import asyncio

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, DEVS
from AyiinXd.ayiin import ayiin_cmd, eor
from Stringyins import get_string


@ayiin_cmd(pattern="fgban(?: |$)(.*)")
async def gbun(event):
    if event.fwd_from:
        return
    gbunVar = event.text
    gbunVar = gbunVar[6:]
    me = await event.client.get_me()
    mentions = get_string("fake_2").format(me.first_name)
    await eor(event, get_string("band_1"))
    asyncio.sleep(3.5)
    chat = await event.get_input_chat()
    async for _ in event.client.iter_participants(
        chat, filter=ChannelParticipantsAdmins
    ):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.sender_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.sender_id
        # make meself invulnerable cuz why not xD
        if idd == DEVS:
            await reply_message.reply(get_string("fake_3")
                                      )
        else:
            jnl = get_string("fake_4").format(me.first_name, firstname, idd)
            if usname is None:
                jnl += get_string("fake_9")
            elif usname != "None":
                jnl += get_string("fake_8").format(usname)
            if len(gbunVar) > 0:
                gbunm = "`{}`".format(gbunVar)
                gbunr = get_string("fake_5").format(gbunm)
                jnl += gbunr
            else:
                no_reason = get_string("fake_7")
                jnl += no_reason
            await reply_message.reply(jnl)
    else:
        mention = get_string("fake_6").format(me.first_name)
        await event.reply(mention)
    await event.delete()


CMD_HELP.update(
    {
        "fakegban": f"**Plugin : **`fakegban`\
        \n\n  »  **Perintah :** `{cmd}fgban` <reply> <reason>\
        \n  »  **Kegunaan : **Untuk melakukan aksi Fake global banned , just for fun\
    "
    }
)
