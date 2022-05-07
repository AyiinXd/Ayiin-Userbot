from telethon.utils import pack_bot_file_id

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, LOGS
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from AyiinXd.ayiin.logger import logging
from Stringyins import get_string

LOGS = logging.getLogger(__name__)


@ayiin_cmd(pattern="(get_id|id)(?:\\s|$)([\\s\\S]*)")
async def _(event):
    input_str = event.pattern_match.group(2)
    if input_str:
        try:
            p = await event.client.get_entity(input_str)
        except Exception as e:
            return await eod(event, get_string("error_1").format(e), time=10)
        try:
            if p.first_name:
                return await eor(
                    event, get_string("getid_1").format("User", input_str, p.id)
                )
        except Exception:
            try:
                if p.title:
                    return await eor(
                        event, get_string("getid_1").format("Name", p.title, p.id)
                    )
            except Exception as e:
                LOGS.info(str(e))
        await eor(event, get_string("getid_2"))
    elif event.reply_to_msg_id:
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await eor(
                event, get_string("getid_3").format(str(r_msg.id), str(r_msg.sender_id), bot_api_file_id)
            )

        else:
            await eor(
                event, get_string("getid_4").format(str(event.chat_id), str(r_msg.id), str(r_msg.sender_id))
            )

    else:
        await eor(event, get_string("getid_5").format(event.chat_id))


CMD_HELP.update(
    {
        "id": f"**Plugin : **`id`\
        \n\n  »  **Perintah :** `{cmd}id` <username/reply>\
        \n  »  **Kegunaan : **Untuk Mengambil Chat ID obrolan saat ini\
        \n\n  »  **Perintah :** `{cmd}userid` <username/reply>\
        \n  »  **Kegunaan : **Untuk Mengambil ID & Username obrolan saat ini\
    "
    }
)
