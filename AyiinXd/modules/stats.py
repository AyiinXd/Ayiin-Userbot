# Copyright (C) 2020 Catuserbot <https://github.com/sandy1709/catuserbot>
# Ported by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
#

"""Count the Number of Dialogs you have in your Telegram Account
Syntax: .stats & .ustat"""
import time

from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.functions.contacts import GetBlockedRequest
from telethon.tl.functions.messages import GetAllStickersRequest
from telethon.tl.types import Channel, Chat, User

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from Stringyins import get_string


# Functions
def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    return " ".join(names)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


@ayiin_cmd(pattern="stats$")
async def stats(
    event: NewMessage.Event,
) -> None:
    stat = await eor(event, get_string("stats_1"))
    start_time = time.time()
    private_chats = 0
    bots = 0
    groups = 0
    broadcast_channels = 0
    admin_in_groups = 0
    creator_in_groups = 0
    admin_in_broadcast_channels = 0
    creator_in_channels = 0
    unread_mentions = 0
    unread = 0
    dialog: Dialog
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            broadcast_channels += 1
            if entity.creator or entity.admin_rights:
                admin_in_broadcast_channels += 1
            if entity.creator:
                creator_in_channels += 1
        elif (
            isinstance(entity, Channel)
            and entity.megagroup
            or not isinstance(entity, Channel)
            and not isinstance(entity, User)
            and isinstance(entity, Chat)
        ):
            groups += 1
            if entity.creator or entity.admin_rights:
                admin_in_groups += 1
            if entity.creator:
                creator_in_groups += 1
        elif not isinstance(entity, Channel) and isinstance(entity, User):
            private_chats += 1
            if entity.bot:
                bots += 1
        unread_mentions += dialog.unread_mentions_count
        unread += dialog.unread_count
    stop_time = time.time() - start_time
    try:
        ct = (await event.client(GetBlockedRequest(1, 0))).count
    except AttributeError:
        ct = 0
    try:
        sp = await event.client(GetAllStickersRequest(0))
        sp_count = len(sp.sets)
    except BaseException:
        sp_count = 0
    full_name = inline_mention(await event.client.get_me())
    response = get_string("stats_2").format(full_name)
    response += get_string("stats_3").format(private_chats)
    response += get_string("stats_4").format(private_chats - bots)
    response += get_string("stats_5").format(bots)
    response += get_string("stats_6").format(groups)
    response += get_string("stats_7").format(broadcast_channels)
    response += get_string("stats_8").format(admin_in_groups)
    response += get_string("stats_9").format(creator_in_groups)
    response += get_string("stats_10").format(admin_in_groups - creator_in_groups)
    response += get_string("stats_11").format(admin_in_broadcast_channels)
    response += get_string("stats_12").format(creator_in_channels)
    response += get_string("stats_13").format(admin_in_broadcast_channels - creator_in_channels)
    response += get_string("stats_14").format(unread)
    response += get_string("stats_15").format(unread_mentions)
    response += get_string("stats_16").format(ct)
    response += get_string("stats_17").format(sp_count)
    response += f"⏱ **__It Took:__** {stop_time:.02f}s \n"
    await stat.edit(response)


@ayiin_cmd(pattern=r"(ustat|deteksi|ustats)(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply_message = await event.get_reply_message()
    if not input_str and not reply_message:
        await eod(
            event, get_string("ustat_1")
        )
    if input_str:
        try:
            uid = int(input_str)
        except ValueError:
            try:
                u = await event.client.get_entity(input_str)
            except ValueError:
                await eod(
                    event, get_string("ustat_2")
                )
            uid = u.id
    else:
        uid = reply_message.sender_id
    chat = "@tgscanrobot"
    sevent = await eor(event, get_string("com_1"))
    async with event.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(f"{uid}")
        except Exception:
            await eod(sevent, get_string("ustat_3"))
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await sevent.edit(response.text)
        """Cleanup after completed"""
        await event.client.delete_messages(conv.chat_id, [msg.id, response.id])


CMD_HELP.update(
    {
        "stats": f"**Plugin : **`stats`\
        \n\n  »  **Perintah :** `{cmd}stats`\
        \n  »  **Kegunaan : **Untuk memeriksa statistik pengguna\
        \n\n  »  **Perintah :** `{cmd}ustat` atau `{cmd}ustats`\
        \n  »  **Kegunaan : **Untuk memeriksa orang tersebut bergabung ke grup mana aja\
    "
    }
)


CMD_HELP.update(
    {
        "deteksi": f"**Plugin : **`deteksi`\
        \n\n  »  **Perintah :** `{cmd}deteksi`\
        \n  »  **Kegunaan : **Untuk memeriksa orang tersebut bergabung ke grup mana aja\
    "
    }
)
