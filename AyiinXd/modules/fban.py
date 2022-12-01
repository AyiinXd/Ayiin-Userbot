# Copyright (C) 2020 KenHV

from sqlalchemy.exc import IntegrityError

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, bot
from AyiinXd.ayiin import ayiin_cmd
from Stringyins import get_string

fban_replies = [
    "New FedBan",
    "Starting a federation ban",
    "Start a federation ban",
    "FedBan Reason update",
    "FedBan reason updated",
    "has already been fbanned, with the exact same reason.",
]

unfban_replies = ["New un-FedBan", "I'll give", "Un-FedBan"]


@ayiin_cmd(pattern="(d)?fban(?: |$)(.*)")
async def fban(event):
    """Bans a user from connected federations."""
    try:
        from AyiinXd.modules.sql_helper.fban_sql import get_flist
    except IntegrityError:
        return await event.edit(get_string("not_sql"))

    match = event.pattern_match.group(2)

    if event.is_reply:
        reply_msg = await event.get_reply_message()
        fban_id = reply_msg.sender_id

        if event.pattern_match.group(1) == "d":
            await reply_msg.delete()

        reason = match
    else:
        pattern = match.split()
        fban_id = pattern[0]
        reason = " ".join(pattern[1:])

    try:
        fban_id = await event.client.get_peer_id(fban_id)
    except BaseException:
        pass

    if event.sender_id == fban_id:
        return await event.edit(get_string("fban_1")
                                )

    fed_list = get_flist()
    if len(fed_list) == 0:
        return await event.edit(get_string("fban_2"))

    user_link = f"[{fban_id}](tg://user?id={fban_id})"

    await event.edit(f"**Fbanning** {user_link}...")
    failed = []
    total = 0

    for i in fed_list:
        total += 1
        chat = int(i.chat_id)
        try:
            async with bot.conversation(chat) as conv:
                await conv.send_message(f"/fban {user_link} {reason}")
                reply = await conv.get_response()
                await bot.send_read_acknowledge(
                    conv.chat_id, message=reply, clear_mentions=True
                )

                if all(i not in reply.text for i in fban_replies):
                    failed.append(i.fed_name)
        except Exception:
            failed.append(i.fed_name)

    reason = reason or "Not specified."

    if failed:
        status = get_string("fban_3").format(len(failed), total)
        for i in failed:
            status += f"• {i}\n"
    else:
        status = get_string("fban_4").format(total)

    await event.edit(get_string("fban_5").format(user_link, reason, status)
                     )


@ayiin_cmd(pattern="unfban(?: |$)(.*)")
async def unfban(event):
    """Unbans a user from connected federations."""
    try:
        from AyiinXd.modules.sql_helper.fban_sql import get_flist
    except IntegrityError:
        return await event.edit(get_string("not_sql"))

    match = event.pattern_match.group(1)
    if event.is_reply:
        unfban_id = (await event.get_reply_message()).sender_id
        reason = match
    else:
        pattern = match.split()
        unfban_id = pattern[0]
        reason = " ".join(pattern[1:])

    try:
        unfban_id = await event.client.get_peer_id(unfban_id)
    except BaseException:
        pass

    if event.sender_id == unfban_id:
        return await event.edit(get_string("ufbn_1"))

    fed_list = get_flist()
    if len(fed_list) == 0:
        return await event.edit(get_string("fban_2"))

    user_link = f"[{unfban_id}](tg://user?id={unfban_id})"

    await event.edit(f"**Un-fbanning **{user_link}**...**")
    failed = []
    total = 0

    for i in fed_list:
        total += 1
        chat = int(i.chat_id)
        try:
            async with bot.conversation(chat) as conv:
                await conv.send_message(f"/unfban {user_link} {reason}")
                reply = await conv.get_response()
                await bot.send_read_acknowledge(
                    conv.chat_id, message=reply, clear_mentions=True
                )

                if all(i not in reply.text for i in unfban_replies):
                    failed.append(i.fed_name)
        except BaseException:
            failed.append(i.fed_name)

    reason = reason or "Not specified."

    if failed:
        status = get_string("ufbn_4").format(len(failed), total)
        for i in failed:
            status += f"• {i}\n"
    else:
        status = get_string("ufbn_2").format(total)

    reason = reason or "Not specified."
    await event.edit(get_string("ufbn_3").format(user_link, reason, status)
                     )


@ayiin_cmd(pattern="addf(?: |$)(.*)")
async def addf(event):
    """Adds current chat to connected federations."""
    try:
        from AyiinXd.modules.sql_helper.fban_sql import add_flist
    except IntegrityError:
        return await event.edit(get_string("not_sql"))

    fed_name = event.pattern_match.group(1)
    if not fed_name:
        return await event.edit(get_string("afbn_1"))

    try:
        add_flist(event.chat_id, fed_name)
    except IntegrityError:
        return await event.edit(get_string("afbn_2"))

    await event.edit(get_string("afbn_3"))


@ayiin_cmd(pattern="delf$")
async def delf(event):
    """Removes current chat from connected federations."""
    try:
        from AyiinXd.modules.sql_helper.fban_sql import del_flist
    except IntegrityError:
        return await event.edit(get_string("not_sql"))

    del_flist(event.chat_id)
    await event.edit(get_string("dfbn_1"))


@ayiin_cmd(pattern="listf$")
async def listf(event):
    """List all connected federations."""
    try:
        from AyiinXd.modules.sql_helper.fban_sql import get_flist
    except IntegrityError:
        return await event.edit(get_string("not_sql"))

    fed_list = get_flist()
    if len(fed_list) == 0:
        return await event.edit(get_string("fban_2"))

    msg = get_string("lfbn_1")

    for i in fed_list:
        msg += f"• {i.fed_name}\n"

    await event.edit(msg)


@ayiin_cmd(pattern="clearf$")
async def clearf(event):
    """Removes all chats from connected federations."""
    try:
        from AyiinXd.modules.sql_helper.fban_sql import del_flist_all
    except IntegrityError:
        return await event.edit(get_string("not_sql"))

    del_flist_all()
    await event.edit(get_string("dfbn_2"))


CMD_HELP.update(
    {
        "fban": f"**Plugin : **`Federations Banned`\
        \n\n  »  **Perintah :** `{cmd}fban` <id/username/reply> <reason>\
        \n  »  **Kegunaan : **Membanned user dari federasi yang terhubung.\
        \n\n  »  **Perintah :** `{cmd}dfban` <id/username/reply> <reason>\
        \n  »  **Kegunaan : **Membanned user dari federasi yang terhubung dengan menghapus pesan yang dibalas.\
        \n\n  »  **Perintah :** `{cmd}unfban` <id/username/reply> <reason>\
        \n  »  **Kegunaan : **Membatalkan Federations Banned\
        \n\n  »  **Perintah :** `{cmd}addf` <nama>\
        \n  »  **Kegunaan : **Menambahkan grup saat ini dan menyimpannya sebagai <nama> di federasi yang terhubung. Menambahkan satu grup sudah cukup untuk satu federasi.\
        \n\n  »  **Perintah :** `{cmd}delf`\
        \n  »  **Kegunaan : **Menghapus grup saat ini dari federasi yang terhubung\
        \n\n  »  **Perintah :** `{cmd}listf`\
        \n  »  **Kegunaan : **Mencantumkan semua federasi yang terhubung dengan nama yang ditentukan.\
        \n\n  »  **Perintah :** `{cmd}clearf`\
        \n  »  **Kegunaan : **Menghapus dari semua federasi yang terhubung. Gunakan dengan hati-hati.\
    "
    }
)
