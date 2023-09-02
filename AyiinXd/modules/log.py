# Credits: mrconfused
# Recode by @mrismanaziz
# t.me/SharingUserbot

import asyncio

from telethon import events
from telethon.tl.custom import Message

from AyiinXd import CMD_HELP, LOGS, Ayiin
from AyiinXd.ayiin import _format, ayiin_cmd, edit_delete, edit_or_reply
from AyiinXd.ayiin.tools import media_type
from AyiinXd.database.log import approve_log, disapprove_log, is_approved_log
from AyiinXd.database.variable import get_var, set_var

from . import cmd, var
from .carbon import vcmention


class LOG_CHATS:
    def __init__(self):
        self.RECENT_USER = None
        self.NEWPM = None
        self.COUNT = 0


LOG_CHATS_ = LOG_CHATS()


@Ayiin.on(events.ChatAction)
async def logaddjoin(yins):
    user = await yins.get_user()
    chat = await yins.get_chat()
    if not (user and user.is_self):
        return
    if hasattr(chat, "username") and chat.username:
        chat = f"[{chat.title}](https://t.me/{chat.username}/{yins.action_message.id})"
    else:
        chat = f"[{chat.title}](https://t.me/c/{chat.id}/{yins.action_message.id})"
    if yins.user_added:
        tmp = yins.added_by
        text = f"📩 **#TAMBAH_LOG\n •** {vcmention(tmp)} **Menambahkan** {vcmention(user)}\n **• Ke Group** {chat}"
    elif yins.user_joined:
        text = f"📨 **#LOG_GABUNG\n •** [{user.first_name}](tg://user?id={user.id}) **Bergabung\n • Ke Group** {chat}"
    else:
        return
    await yins.client.send_message(var.BOTLOG_CHATID, text)


@Ayiin.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
@Ayiin.on(events.MessageEdited(incoming=True, func=lambda e: e.is_private))
async def monito_p_m_s(yins: Message):
    if var.BOTLOG_CHATID == -100:
        return
    if not get_var("PMLOG"):
        return
    sender = await yins.get_sender()
    await asyncio.sleep(0.5)
    if not sender.bot:
        chat = await yins.get_chat()
        if not is_approved_log(chat.id) and chat.id != 777000:
            if LOG_CHATS_.RECENT_USER != chat.id:
                LOG_CHATS_.RECENT_USER = chat.id
                if LOG_CHATS_.NEWPM:
                    await LOG_CHATS_.NEWPM.edit(
                        LOG_CHATS_.NEWPM.text.replace(
                            "**💌 #PESAN_BARU**",
                            f" • `{LOG_CHATS_.COUNT}` **Pesan**",
                        )
                    )
                    LOG_CHATS_.COUNT = 0
                LOG_CHATS_.NEWPM = await yins.client.send_message(
                    var.BOTLOG_CHATID,
                    f"**💌 #MENERUSKAN #PESAN_BARU**\n** • Dari : **{_format.mentionuser(sender.first_name , sender.id)}\n** • User ID:** `{chat.id}`",
                )
            try:
                if yins.message:
                    await yins.client.forward_messages(
                        var.BOTLOG_CHATID, yins.message, silent=True
                    )
                LOG_CHATS_.COUNT += 1
            except Exception as e:
                LOGS.warn(str(e))


@Ayiin.on(events.NewMessage(incoming=True, func=lambda e: e.mentioned))
@Ayiin.on(events.MessageEdited(incoming=True, func=lambda e: e.mentioned))
async def log_tagged_messages(event: Message):
    if var.BOTLOG_CHATID == -100:
        return
    xnxx = await event.get_chat()

    if not get_var("GRUPLOG"):
        return
    if (
        (is_approved_log(xnxx.id))
        or (var.BOTLOG_CHATID == -100)
        or (await event.get_sender() and (await event.get_sender()).bot)
    ):
        return
    full = None
    try:
        full = await event.client.get_entity(event.message.from_id)
        nameyins = full.first_name
        idyins = full.id
    except Exception as e:
        LOGS.info(str(e))
    messaget = media_type(event)
    resalt = f"<b>📨 #TAGS #MESSAGE</b>\n<b> • Dari : </b>{_format.htmlmentionuser(nameyins, idyins)}"
    if full is not None:
        resalt += f"\n<b> • Grup : </b><code>{xnxx.title}</code>"
    if messaget is not None:
        resalt += f"\n<b> • Jenis Pesan : </b><code>{messaget}</code>"
    else:
        resalt += f"\n<b> • 👀 </b><a href = 'https://t.me/c/{xnxx.id}/{event.message.id}'>Lihat Pesan</a>"
    resalt += f"\n<b> • Message : </b>{event.message.message}"
    await asyncio.sleep(0.5)
    if not event.is_private:
        await event.client.send_message(
            var.BOTLOG_CHATID,
            resalt,
            parse_mode="html",
            link_preview=False,
        )


@ayiin_cmd(pattern="savelog(?: |$)(.*)")
async def log(log_text):
    if var.BOTLOG_CHATID:
        if log_text.reply_to_msg_id:
            reply_msg = await log_text.get_reply_message()
            await reply_msg.forward_to(var.BOTLOG_CHATID)
        elif log_text.pattern_match.group(1):
            user = f"**#LOG / Chat ID:** {log_text.chat_id}\n\n"
            textx = user + log_text.pattern_match.group(1)
            await log_text.client.send_message(var.BOTLOG_CHATID, textx)
        else:
            await edit_delete(log_text, "**Apa yang harus saya simpan?**")
            return
        await edit_delete(log_text, "**Berhasil disimpan di Grup Log**")
    else:
        await edit_delete(
            log_text,
            "**Untuk Menggunakan Module ini, Anda Harus Mengatur** `BOTLOG_CHATID` **di Config Vars**",
            30,
        )


@ayiin_cmd(pattern="log$")
async def set_no_log_p_m(event):
    if var.BOTLOG_CHATID != -100:
        chat = await event.get_chat()
        if is_approved_log(chat.id):
            approve_log(chat.id)
            await edit_delete(
                event, "**LOG Chat dari Grup ini Berhasil Diaktifkan**", 15
            )


@ayiin_cmd(pattern="nolog$")
async def set_no_log_p_m(event):
    if var.BOTLOG_CHATID != -100:
        chat = await event.get_chat()
        if not is_approved_log(chat.id):
            disapprove_log(chat.id)
            await edit_delete(
                event, "**LOG Chat dari Grup ini Berhasil Dimatikan**", 15
            )


@ayiin_cmd(pattern="pmlog (on|off)$")
async def set_pmlog(event):
    if var.BOTLOG_CHATID == -100:
        return await edit_delete(
            event,
            "**Untuk Menggunakan Module ini, Anda Harus Mengatur** `BOTLOG_CHATID` **di Config Vars**",
            30,
        )
    input_str = event.pattern_match.group(1)
    if input_str == "off":
        h_type = False
    elif input_str == "on":
        h_type = True
    if not get_var("PMLOG"):
        PMLOG = False
    else:
        PMLOG = True
    if PMLOG:
        if h_type:
            await edit_or_reply(event, "**PM LOG Sudah Diaktifkan**")
        else:
            set_var("PMLOG", h_type)
            await edit_or_reply(event, "**PM LOG Berhasil Dimatikan**")
    elif h_type:
        set_var("PMLOG", h_type)
        await edit_or_reply(event, "**PM LOG Berhasil Diaktifkan**")
    else:
        await edit_or_reply(event, "**PM LOG Sudah Dimatikan**")


@ayiin_cmd(pattern="gruplog (on|off)$")
async def set_gruplog(event):
    if var.BOTLOG_CHATID == -100:
        return await edit_delete(
            event,
            "**Untuk Menggunakan Module ini, Anda Harus Mengatur** `BOTLOG_CHATID` **di Config Vars**",
            30,
        )
    input_str = event.pattern_match.group(1)
    if input_str == "off":
        h_type = False
    elif input_str == "on":
        h_type = True
    if not get_var("GRUPLOG"):
        GRUPLOG = False
    else:
        GRUPLOG = True
    if GRUPLOG:
        if h_type:
            await edit_or_reply(event, "**Group Log Sudah Diaktifkan**")
        else:
            set_var("GRUPLOG", h_type)
            await edit_or_reply(event, "**Group Log Berhasil Dimatikan**")
    elif h_type:
        set_var("GRUPLOG", h_type)
        await edit_or_reply(event, "**Group Log Berhasil Diaktifkan**")
    else:
        await edit_or_reply(event, "**Group Log Sudah Dimatikan**")


CMD_HELP.update(
    {
        "log": f"**Plugin : **`log`\
        \n\n  »  **Perintah :** `{cmd}savelog`\
        \n  »  **Kegunaan : **__Untuk Menyimpan pesan yang ditandai ke grup pribadi.__\
        \n\n  »  **Perintah :** `{cmd}log`\
        \n  »  **Kegunaan : **__Untuk mengaktifkan Log Chat dari obrolan/grup itu.__\
        \n\n  »  **Perintah :** `{cmd}nolog`\
        \n  »  **Kegunaan : **__Untuk menonaktifkan Log Chat dari obrolan/grup itu.__\
        \n\n  »  **Perintah :** `{cmd}pmlog on/off`\
        \n  »  **Kegunaan : **__Untuk mengaktifkan atau menonaktifkan pencatatan pesan pribadi__\
        \n\n  »  **Perintah :** `{cmd}gruplog on/off`\
        \n  »  **Kegunaan : **__Untuk mengaktifkan atau menonaktifkan tag grup, yang akan masuk ke grup pmlogger.__"
    }
)
