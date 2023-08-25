import logging

from telethon.utils import pack_bot_file_id

from AyiinXd import CMD_HELP, LOGS
from AyiinXd.ayiin import ayiin_cmd, eod, eor

from . import cmd

LOGS = logging.getLogger(__name__)


@ayiin_cmd(pattern="(get_id|id)(?:\\s|$)([\\s\\S]*)")
async def _(event):
    input_str = event.pattern_match.group(2)
    if input_str:
        try:
            p = await event.client.get_entity(input_str)
        except Exception as e:
            return await eod(event, f"**KESALAHAN : **`{str(e)}`", time=10)
        try:
            if p.first_name:
                return await eor(
                    event,
                    f"**User :** {p.first_name}\n**ID** » `{p.id}`"
                )
        except Exception:
            try:
                if p.title:
                    return await eor(
                        event,
                        f"**Name :** {p.title}\n**ID** » `{p.id}`"
                    )
            except Exception as e:
                LOGS.info(str(e))
        await eor(event, "**Berikan Username atau Reply ke pesan pengguna**")
    elif event.reply_to_msg_id:
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await eor(
                event,
                f"**💬 ID Pesan :** `{str(r_msg.id)}`\n**🙋‍♂️ Dari ID Pengguna :** `{str(r_msg.sender_id)}`\n**💎 Bot API File ID:** `{bot_api_file_id}`"
            )

        else:
            await eor(
                event,
                f"**👥 ID Obrolan :** `{str(event.chat_id)}`\n**💬 ID Pesan :** `{str(r_msg.id)}`\n**🙋‍♂️ Dari ID Pengguna :** `{str(r_msg.sender_id)}`"
            )

    else:
        await eor(
            event,
            f"**👥 ID Obrolan : **`{event.chat_id}`"
        )


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
