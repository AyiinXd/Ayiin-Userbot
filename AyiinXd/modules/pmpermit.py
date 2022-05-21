# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# Recode by @mrismanaziz
# @SharingUserbot
""" Userbot module for keeping control who PM you. """

from sqlalchemy.exc import IntegrityError
from telethon import events
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.functions.messages import ReportSpamRequest
from telethon.tl.types import User

from AyiinXd import BOTLOG_CHATID
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, COUNT_PM, DEVS, LASTMSG, LOGS, PM_AUTO_BAN, PM_LIMIT, bot
from AyiinXd.events import ayiin_cmd
from AyiinXd.ayiin import eod, eor
from Stringyins import get_string

DEF_UNAPPROVED_MSG = (get_string("prmt_1"))


@bot.on(events.NewMessage(incoming=True))
async def permitpm(event):
    """ Prohibits people from PMing you without approval. \
        Will block retarded nibbas automatically. """
    if not PM_AUTO_BAN:
        return
    self_user = await event.client.get_me()
    sender = await event.get_sender()
    if (
        event.is_private
        and event.chat_id != 777000
        and event.chat_id != self_user.id
        and not sender.bot
        and not sender.contact
    ):
        try:
            from AyiinXd.modules.sql_helper.globals import gvarstatus
            from AyiinXd.modules.sql_helper.pm_permit_sql import is_approved
        except AttributeError:
            return
        apprv = is_approved(event.chat_id)
        notifsoff = gvarstatus("NOTIF_OFF")

        # Use user custom unapproved message
        getmsg = gvarstatus("unapproved_msg")
        UNAPPROVED_MSG = getmsg if getmsg is not None else DEF_UNAPPROVED_MSG
        # This part basically is a sanity check
        # If the message that sent before is Unapproved Message
        # then stop sending it again to prevent FloodHit
        if not apprv and event.text != UNAPPROVED_MSG:
            if event.chat_id in LASTMSG:
                prevmsg = LASTMSG[event.chat_id]
                # If the message doesn't same as previous one
                # Send the Unapproved Message again
                if event.text != prevmsg:
                    async for message in event.client.iter_messages(
                        event.chat_id, from_user="me", search=UNAPPROVED_MSG
                    ):
                        await message.delete()
                    await event.reply(f"{UNAPPROVED_MSG}")
            else:
                await event.reply(f"{UNAPPROVED_MSG}")
            LASTMSG.update({event.chat_id: event.text})
            if notifsoff:
                await event.client.send_read_acknowledge(event.chat_id)
            if event.chat_id not in COUNT_PM:
                COUNT_PM.update({event.chat_id: 1})
            else:
                COUNT_PM[event.chat_id] = COUNT_PM[event.chat_id] + 1

            if COUNT_PM[event.chat_id] > PM_LIMIT:
                await event.respond(get_string("prmt_2")
                )

                try:
                    del COUNT_PM[event.chat_id]
                    del LASTMSG[event.chat_id]
                except KeyError:
                    if BOTLOG_CHATID:
                        await event.client.send_message(
                            BOTLOG_CHATID, get_string("prmt_3")
                        )
                    return LOGS.info(get_string("prmt_4"))

                await event.client(BlockRequest(event.chat_id))
                await event.client(ReportSpamRequest(peer=event.chat_id))

                if BOTLOG_CHATID:
                    name = await event.client.get_entity(event.chat_id)
                    name0 = str(name.first_name)
                    await event.client.send_message(
                        BOTLOG_CHATID, get_string("prmt_5").format(name0, str(event.chat_id))
                    )


@bot.on(events.NewMessage(outgoing=True))
async def auto_accept(event):
    """Will approve automatically if you texted them first."""
    if not PM_AUTO_BAN:
        return
    self_user = await event.client.get_me()
    sender = await event.get_sender()
    if (
        event.is_private
        and event.chat_id != 777000
        and event.chat_id != self_user.id
        and not sender.bot
        and not sender.contact
    ):
        try:
            from AyiinXd.modules.sql_helper.globals import gvarstatus
            from AyiinXd.modules.sql_helper.pm_permit_sql import approve, is_approved
        except AttributeError:
            return

        # Use user custom unapproved message
        get_message = gvarstatus("unapproved_msg")
        UNAPPROVED_MSG = get_message if get_message is not None else DEF_UNAPPROVED_MSG
        chat = await event.get_chat()
        if isinstance(chat, User):
            if is_approved(event.chat_id) or chat.bot:
                return
            async for message in event.client.iter_messages(
                event.chat_id, reverse=True, limit=1
            ):
                if (
                    message.text is not UNAPPROVED_MSG
                    and message.sender_id == self_user.id
                ):
                    try:
                        approve(event.chat_id)
                    except IntegrityError:
                        return

                if is_approved(event.chat_id) and BOTLOG_CHATID:
                    await event.client.send_message(
                        BOTLOG_CHATID,
                        "**#AUTO_APPROVED**\n"
                        + "👤 **User:** "
                        + f"[{chat.first_name}](tg://user?id={chat.id})",
                    )


@bot.on(ayiin_cmd(outgoing=True, pattern=r"notifoff$"))
async def notifoff(noff_event):
    """For .notifoff command, stop getting notifications from unapproved PMs."""
    try:
        from AyiinXd.modules.sql_helper.globals import addgvar
    except AttributeError:
        return await noff_event.edit(get_string("not_sql"))
    addgvar("NOTIF_OFF", True)
    await noff_event.edit(get_string("prmt_6")
    )


@bot.on(ayiin_cmd(outgoing=True, pattern=r"notifon$"))
async def notifon(non_event):
    """For .notifoff command, get notifications from unapproved PMs."""
    try:
        from AyiinXd.modules.sql_helper.globals import delgvar
    except AttributeError:
        return await non_event.edit(get_string("not_sql"))
    delgvar("NOTIF_OFF")
    await non_event.edit(get_string("prmt_7")
    )


@bot.on(ayiin_cmd(outgoing=True, pattern=r"(?:setuju|ok)\s?(.)?"))
async def approvepm(apprvpm):
    """For .ok command, give someone the permissions to PM you."""
    try:
        from AyiinXd.modules.sql_helper.globals import gvarstatus
        from AyiinXd.modules.sql_helper.pm_permit_sql import approve
    except AttributeError:
        return await eod(apprvpm, get_string("not_sql"))

    if apprvpm.reply_to_msg_id:
        reply = await apprvpm.get_reply_message()
        replied_user = await apprvpm.client.get_entity(reply.sender_id)
        uid = replied_user.id
        name0 = str(replied_user.first_name)

    elif apprvpm.pattern_match.group(1):
        inputArgs = apprvpm.pattern_match.group(1)

        try:
            inputArgs = int(inputArgs)
        except ValueError:
            pass

        try:
            user = await apprvpm.client.get_entity(inputArgs)
        except BaseException:
            return await eod(apprvpm, "**Invalid username/ID.**")

        if not isinstance(user, User):
            return await eod(apprvpm, get_string("prmt_8")
            )

        uid = user.id
        name0 = str(user.first_name)

    else:
        aname = await apprvpm.client.get_entity(apprvpm.chat_id)
        if not isinstance(aname, User):
            return await eod(apprvpm, get_string("prmt_8")
            )
        name0 = str(aname.first_name)
        uid = apprvpm.chat_id

    # Get user custom msg
    getmsg = gvarstatus("unapproved_msg")
    UNAPPROVED_MSG = getmsg if getmsg is not None else DEF_UNAPPROVED_MSG
    async for message in apprvpm.client.iter_messages(
        apprvpm.chat_id, from_user="me", search=UNAPPROVED_MSG
    ):
        await message.delete()

    try:
        approve(uid)
    except IntegrityError:
        return await eod(apprvpm, get_string("prmt_9"))

    await eod(
        apprvpm, get_string("prmt_10").format(name0, uid), time=5
    )


@bot.on(ayiin_cmd(outgoing=True, pattern=r"(?:tolak|nopm)\s?(.)?"))
async def disapprovepm(disapprvpm):
    try:
        from AyiinXd.modules.sql_helper.pm_permit_sql import dissprove
    except BaseException:
        return await eod(disapprvpm, get_string("not_sql"))

    if disapprvpm.reply_to_msg_id:
        reply = await disapprvpm.get_reply_message()
        replied_user = await disapprvpm.client.get_entity(reply.sender_id)
        aname = replied_user.id
        name0 = str(replied_user.first_name)
        dissprove(aname)

    elif disapprvpm.pattern_match.group(1):
        inputArgs = disapprvpm.pattern_match.group(1)

        try:
            inputArgs = int(inputArgs)
        except ValueError:
            pass

        try:
            user = await disapprvpm.client.get_entity(inputArgs)
        except BaseException:
            return await eod(
                disapprvpm, get_string("prmt_11")
            )

        if not isinstance(user, User):
            return await eod(
                disapprvpm, get_string("prmt_11")
            )

        aname = user.id
        dissprove(aname)
        name0 = str(user.first_name)

    else:
        dissprove(disapprvpm.chat_id)
        aname = await disapprvpm.client.get_entity(disapprvpm.chat_id)
        if not isinstance(aname, User):
            return await eod(
                disapprvpm, get_string("prmt_12")
            )
        name0 = str(aname.first_name)
        aname = aname.id

    await eor(
        disapprvpm, get_string("prmt_13").format(name0, aname)
    )


@bot.on(ayiin_cmd(outgoing=True, pattern=r"block$"))
async def blockpm(block):
    """For .block command, block people from PMing you!"""
    if block.reply_to_msg_id:
        reply = await block.get_reply_message()
        replied_user = await block.client.get_entity(reply.sender_id)
        aname = replied_user.id
        await block.client(BlockRequest(aname))
        await block.edit(get_string("prmt_14"))
        uid = replied_user.id
    else:
        await block.client(BlockRequest(block.chat_id))
        aname = await block.client.get_entity(block.chat_id)
        if not isinstance(aname, User):
            return await block.edit(get_string("prmt_12"))
        await block.edit(get_string("prmt_14"))
        uid = block.chat_id

    try:
        from AyiinXd.modules.sql_helper.pm_permit_sql import dissprove

        dissprove(uid)
    except AttributeError:
        pass


@bot.on(ayiin_cmd(outgoing=True, pattern=r"unblock$"))
async def unblockpm(unblock):
    """For .unblock command, let people PMing you again!"""
    if unblock.reply_to_msg_id:
        reply = await unblock.get_reply_message()
        replied_user = await unblock.client.get_entity(reply.sender_id)
        await unblock.client(UnblockRequest(replied_user.id))
        await unblock.edit(get_string("prmt_15"))


@bot.on(ayiin_cmd(outgoing=True, pattern=r"(set|get|reset) pmpermit(?: |$)(\w*)"))
async def add_pmsg(cust_msg):
    """Set your own Unapproved message"""
    if not PM_AUTO_BAN:
        return await cust_msg.edit(get_string("prmt_16").format(cmd)
        )
    try:
        import AyiinXd.modules.sql_helper.globals as sql
    except AttributeError:
        await cust_msg.edit(get_string("not_sql"))
        return

    await cust_msg.edit(get_string("com_1"))
    conf = cust_msg.pattern_match.group(1)

    custom_message = sql.gvarstatus("unapproved_msg")

    if conf.lower() == "set":
        message = await cust_msg.get_reply_message()
        status = "Pesan"

        # check and clear user unapproved message first
        if custom_message is not None:
            sql.delgvar("unapproved_msg")
            status = "Pesan"

        if not message:
            return await cust_msg.edit(get_string("prmt_23"))

        # TODO: allow user to have a custom text formatting
        # eg: bold, underline, striketrough, link
        # for now all text are in monoscape
        msg = message.message  # get the plain text
        sql.addgvar("unapproved_msg", msg)
        await cust_msg.edit(get_string("prmt_17"))

        if BOTLOG_CHATID:
            await cust_msg.client.send_message(
                BOTLOG_CHATID, get_string("prmt_18").format(status, msg)
            )

    if conf.lower() == "reset":
        if custom_message is None:
            await cust_msg.edit(get_string("prmt_19")
            )

        else:
            sql.delgvar("unapproved_msg")
            await cust_msg.edit(get_string("prmt_20"))
    if conf.lower() == "get":
        if custom_message is not None:
            await cust_msg.edit(get_string("prmt_21").format(custom_message)
            )
        else:
            await cust_msg.edit(get_string("prmt_22").format(DEF_UNAPPROVED_MSG)
            )


@bot.on(events.NewMessage(incoming=True, from_users=(DEVS)))
async def pmdevs(event):
    if event.fwd_from:
        return
    try:
        from AyiinXd.modules.sql_helper.globals import gvarstatus
        from AyiinXd.modules.sql_helper import pm_permit_sql as yins_sql
    except AttributeError:
        return await eod(event, get_string("not_sql"))
    devs = await event.get_chat()
    if event.is_private:
        # Get user custom msg
        getmsg = gvarstatus("unapproved_msg")
        UNAPPROVED_MSG = getmsg if getmsg is not None else DEF_UNAPPROVED_MSG
        async for message in event.client.iter_messages(
            devs.id, from_user="me", search=UNAPPROVED_MSG
        ):
            await message.delete()

        if not yins_sql.is_approved(devs.id):
            try:
                yins_sql.approve(devs.id)
                await bot.send_message(BOTLOG_CHATID, f"**#AUTO_APPROVED_DEVELOPER**\n\n👑 **Developer:** [{devs.first_name}](tg://user?id={devs.id})\n💬 `Developer Ayiin-Userbot Telah Mengirimi Anda Pesan...`")
                await bot.send_message(
                    devs, f"**Menerima Pesan!!!**\n**Terdeteksi [{devs.first_name}](tg://user?id={devs.id}) Adalah Developer Ayiin-Userbot**"
                )
            except BaseException as e:
                return await eor(event, get_string("error_1").format(e))


CMD_HELP.update(
    {
        "pmpermit": f"**Plugin : **`pmpermit`\
        \n\n  »  **Perintah :** `{cmd}setuju` atau `{cmd}ok`\
        \n  »  **Kegunaan : **Menerima pesan seseorang dengan cara balas pesannya atau tag dan juga untuk dilakukan di pm.\
        \n\n  »  **Perintah :** `{cmd}tolak` atau `{cmd}nopm`\
        \n  »  **Kegunaan : **Menolak pesan seseorang dengan cara balas pesannya atau tag dan juga untuk dilakukan di pm.\
        \n\n  »  **Perintah :** `{cmd}block`\
        \n  »  **Kegunaan : **Memblokir Orang Di PM.\
        \n\n  »  **Perintah :** `{cmd}unblock`\
        \n  »  **Kegunaan : **Membuka Blokir.\
        \n\n  »  **Perintah :** `{cmd}notifoff`\
        \n  »  **Kegunaan : **Menghidupkan notifikasi pesan yang belum diterima.\
        \n\n  »  **Perintah :** `{cmd}notifon`\
        \n  »  **Kegunaan : **Menghidupkan notifikasi pesan yang belum diterima.\
        \n\n  »  **Perintah :** `{cmd}set pmpermit` <balas ke pesan>\
        \n  »  **Kegunaan : **Menyetel Pesan Pribadimu untuk orang yang pesannya belum diterima.\
        \n\n  »  **Perintah :** `{cmd}get pmpermit`\
        \n  »  **Kegunaan : **Mendapatkan Custom pesan PM mu.\
        \n\n  »  **Perintah :** `{cmd}reset pmpermit`\
        \n  »  **Kegunaan : **Menghapus pesan PM ke default.\
        \n\n  •  **Pesan Pribadi yang belum diterima saat ini tidak dapat disetel ke teks format kaya bold, underline, link, dll. Pesan akan terkirim normal saja**\
        \n\n**NOTE: Bila ingin Mengaktifkan PMPERMIT Silahkan Ketik:** `{cmd}set var PM_AUTO_BAN True`\
    "
    }
)
