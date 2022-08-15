import asyncio

from telethon import events
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

import AyiinXd.modules.sql_helper.antiflood_sql as sql
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, bot
from AyiinXd.ayiin import eod, eor
from AyiinXd.events import ayiin_cmd
from AyiinXd.ayiin.tools import is_admin
from Stringyins import get_string

CHAT_FLOOD = sql.__load_flood_settings()
# warn mode for anti flood
ANTI_FLOOD_WARN_MODE = ChatBannedRights(
    until_date=None, view_messages=None, send_messages=True
)


@bot.on(events.NewMessage(incoming=True))
async def _(event):
    # logger.info(CHAT_FLOOD)
    if not CHAT_FLOOD:
        return
    admin_c = await is_admin(event.chat_id, event.message.sender_id)
    if admin_c:
        return
    if str(event.chat_id) not in CHAT_FLOOD:
        return
    should_ban = sql.update_flood(event.chat_id, event.message.sender_id)
    if not should_ban:
        return
    try:
        await event.client(
            EditBannedRequest(
                event.chat_id, event.message.sender_id, ANTI_FLOOD_WARN_MODE
            )
        )
    except Exception as e:
        no_admin_privilege_message = await event.client.send_message(
            entity=event.chat_id,
            message=get_string("antiflood_1").format(event.message.sender_id, str(e)),
            reply_to=event.message.id,
        )
        await asyncio.sleep(10)
        await no_admin_privilege_message.edit(get_string("antiflood_3"))
    else:
        await event.client.send_message(
            entity=event.chat_id,
            message=get_string("antiflood_2").format(event.message.sender_id),
            reply_to=event.message.id,
        )


@bot.on(ayiin_cmd(outgoing=True, pattern="setflood(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    try:
        sql.set_flood(event.chat_id, input_str)
        sql.__load_flood_settings()
        await eor(event, get_string("antiflood_4").format(input_str)
                  )
    except Exception as e:
        await eod(event, get_string("error_1").format(e), time=30)


CMD_HELP.update(
    {
        "antiflood": f"**Plugin : **`antiflood`\
        \n\n  »  **Perintah :** `{cmd}setflood` [jumlah pesan]\
        \n  »  **Kegunaan : **memperingatkan pengguna jika dia melakukan spam pada obrolan dan jika Anda adalah admin maka itu akan membisukan dia dalam grup itu.\
        \n\n  •  **NOTE :** Untuk mematikan setflood, atur jumlah pesan menjadi 0 » `.setflood 0`\
    "
    }
)
