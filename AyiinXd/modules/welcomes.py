# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#


from datetime import datetime

from pytz import timezone

from AyiinXd import BLACKLIST_CHAT, BOTLOG_CHATID, CLEAN_WELCOME
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, LOGS
from AyiinXd.ayiin import ayiin_cmd, chataction
from Stringyins import get_string


@chataction()
async def welcome_to_chat(event):
    try:
        from AyiinXd.modules.sql_helper.welcome_sql import (
            get_current_welcome_settings,
            update_previous_welcome,
        )
    except AttributeError:
        return
    if cws := get_current_welcome_settings(event.chat_id):
        if (event.user_joined or event.user_added) and not (await event.get_user()).bot:
            if CLEAN_WELCOME:
                try:
                    await event.client.delete_messages(
                        event.chat_id, cws.previous_welcome
                    )
                except Exception as e:
                    LOGS.warn(str(e))
            a_user = await event.get_user()
            chat = await event.get_chat()
            me = await event.client.get_me()

            # Current time in UTC
            now_utc = datetime.now(timezone("UTC"))

            # Convert to Jakarta time zone
            now_utc.astimezone(timezone("Asia/Jakarta"))
            title = chat.title or "Grup Ini"
            participants = await event.client.get_participants(chat)
            count = len(participants)
            mention = f"[{a_user.first_name}](tg://user?id={a_user.id})"
            my_mention = f"[{me.first_name}](tg://user?id={me.id})"
            first = a_user.first_name
            last = a_user.last_name
            fullname = f"{first} {last}" if last else first
            username = f"@{a_user.username}" if a_user.username else mention
            userid = a_user.id
            my_first = me.first_name
            my_last = me.last_name
            my_fullname = f"{my_first} {my_last}" if my_last else my_first
            my_username = f"@{me.username}" if me.username else my_mention
            file_media = None
            current_saved_welcome_message = None
            if cws:
                if cws.f_mesg_id:
                    msg_o = await event.client.get_messages(
                        entity=BOTLOG_CHATID, ids=int(cws.f_mesg_id)
                    )
                    file_media = msg_o.media
                    current_saved_welcome_message = msg_o.message
                elif cws.reply:
                    current_saved_welcome_message = cws.reply
            current_message = await event.reply(
                current_saved_welcome_message.format(
                    mention=mention,
                    title=title,
                    count=count,
                    first=first,
                    last=last,
                    fullname=fullname,
                    username=username,
                    userid=userid,
                    my_first=my_first,
                    my_last=my_last,
                    my_fullname=my_fullname,
                    my_username=my_username,
                    my_mention=my_mention,
                ),
                file=file_media,
            )
            update_previous_welcome(event.chat_id, current_message.id)


@ayiin_cmd(pattern="setwelcome(?: |$)(.*)")
async def save_welcome(event):
    if event.chat_id in BLACKLIST_CHAT:
        return await event.edit(get_string("ayiin_1"))
    try:
        from AyiinXd.modules.sql_helper.welcome_sql import add_welcome_setting
    except AttributeError:
        return await event.edit(get_string("not_sql"))
    msg = await event.get_reply_message()
    string = event.pattern_match.group(1)
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG_CHATID:
            await event.client.send_message(
                BOTLOG_CHATID, get_string("swel_1").format(event.chat_id)
            )
            msg_o = await event.client.forward_messages(
                entity=BOTLOG_CHATID, messages=msg, from_peer=event.chat_id, silent=True
            )
            msg_id = msg_o.id
        else:
            return await event.edit(get_string("swel_2")
            )
    elif event.reply_to_msg_id and not string:
        rep_msg = await event.get_reply_message()
        string = rep_msg.text
    if add_welcome_setting(event.chat_id, 0, string, msg_id) is True:
        await event.edit(get_string("swel_3"))
    else:
        await event.edit(get_string("swel_3"))


@ayiin_cmd(pattern="checkwelcome$")
async def show_welcome(event):
    try:
        from AyiinXd.modules.sql_helper.welcome_sql import get_current_welcome_settings
    except AttributeError:
        return await event.edit(get_string("not_sql"))
    cws = get_current_welcome_settings(event.chat_id)
    if not cws:
        return await event.edit(get_string("cwel_1"))
    if cws.f_mesg_id:
        msg_o = await event.client.get_messages(
            entity=BOTLOG_CHATID, ids=int(cws.f_mesg_id)
        )
        await event.edit(get_string("cwel_2"))
        await event.reply(msg_o.message, file=msg_o.media)
    elif cws.reply:
        await event.edit(get_string("cwel_2"))
        await event.reply(cws.reply)


@ayiin_cmd(pattern="rmwelcome$")
async def del_welcome(event):
    try:
        from AyiinXd.modules.sql_helper.welcome_sql import rm_welcome_setting
    except AttributeError:
        return await event.edit(get_string("not_sql"))
    if rm_welcome_setting(event.chat_id) is True:
        await event.edit(get_string("rwel_1"))
    else:
        await event.edit(get_string("cwel_1"))


CMD_HELP.update(
    {
        "welcome": f"**Plugin : **`welcome`\
        \n\n  »  **Perintah :** `{cmd}setwelcome` <pesan welcome> atau balas ke pesan ketik `{cmd}setwelcome`\
        \n  »  **Kegunaan : **Menyimpan pesan welcome digrup.\
        \n\n  »  **Perintah :** `{cmd}checkwelcome`\
        \n  »  **Kegunaan : **Check pesan welcome yang anda simpan.\
        \n\n  »  **Perintah :** `{cmd}rmwelcome`\
        \n  »  **Kegunaan : **Menghapus pesan welcome yang anda simpan."
        "\n\n  •  **Format Variabel yang bisa digunakan di setwelcome :**\
        `{mention}`, `{title}`, `{count}`, `{first}`, `{last}`, `{fullname}`, `{userid}`, `{username}`, `{my_first}`, `{my_fullname}`, `{my_last}`, `{my_mention}`, `{my_username}`\
    "
    }
)
