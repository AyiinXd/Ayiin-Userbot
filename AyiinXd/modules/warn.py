# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# Recode by @AyiinXd
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport

from telethon.tl import types
from telethon.utils import get_display_name

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eor
from AyiinXd.ayiin._baseyins import AyiinDB
from AyiinXd.modules.sql_helper.warn_db import add_warn, reset_warn, warns
from Stringyins import get_string

def inline_mention(user, custom=None, html=False):
    mention_text = get_display_name(user) or user if not custom else custom
    if isinstance(user, types.User):
        if html:
            return f"<a href=tg://user?id={user.id}>{mention_text}</a>"
        return f"[{mention_text}](tg://user?id={user.id})"
    if isinstance(user, types.Channel) and user.username:
        if html:
            return f"<a href=https://t.me/{user.username}>{mention_text}</a>"
        return f"[{mention_text}](https://t.me/{user.username})"
    return mention_text


adB = AyiinDB()


@ayiin_cmd(
    pattern="warn( (.*)|$)",
    group_only=True,
    admins_only=True,
)
async def warn(e):
    ayiin_bot = e.client
    reply = await e.get_reply_message()
    if len(e.text) > 5 and " " not in e.text[5]:
        return
    if reply:
        user = reply.sender_id
        reason = e.text[5:] if e.pattern_match.group(1).strip() else "unknown"
    else:
        try:
            user = e.text.split()[1]
            if user.startswith("@"):
                ok = await ayiin_bot.get_entity(user)
                user = ok.id
            else:
                user = int(user)
        except BaseException:
            return await e.eor("Balas ke pesan Pengguna", time=5)
        try:
            reason = e.text.split(maxsplit=2)[-1]
        except BaseException:
            reason = "unknown"
    count, r = warns(e.chat_id, user)
    r = reason if not r else r + "|$|" + reason
    try:
        x = adB.get_key("SETWARN")
        number, action = int(x.split()[0]), x.split()[1]
    except BaseException:
        number, action = 3, "kick"
    if ("ban" or "kick" or "mute") not in action:
        action = "kick"
    if count + 1 >= number:
        if "ban" in action:
            try:
                await ayiin_bot.edit_permissions(e.chat_id, user, view_messages=False)
            except BaseException:
                return await e.eor("`Something Went Wrong.`", time=5)
        elif "kick" in action:
            try:
                await ayiin_bot.kick_participant(e.chat_id, user)
            except BaseException:
                return await e.eor("`Ada yang salah.`", time=5)
        elif "mute" in action:
            try:
                await ayiin_bot.edit_permissions(
                    e.chat_id, user, until_date=None, send_messages=False
                )
            except BaseException:
                return await e.eor("`Ada yang salah.`", time=5)
        add_warn(e.chat_id, user, count + 1, r)
        c, r = warns(e.chat_id, user)
        ok = await ayiin_bot.get_entity(user)
        user = inline_mention(ok)
        r = r.split("|$|")
        text = f"Pengguna {user} Telah mendapatkan {action} Karena {count+1} Peringatan.\n\n"
        for x in range(c):
            text += f"•**{x+1}.** {r[x]}\n"
        await e.eor(text)
        return reset_warn(e.chat_id, ok.id)
    add_warn(e.chat_id, user, count + 1, r)
    ok = await ayiin_bot.get_entity(user)
    user = inline_mention(ok)
    await eor(
        e,
        f"**PERINGATAN :** {count+1}/{number}\n**Ke :**{user}\n**Hati-hati !!!**\n\n**Alasan** : {reason}",
    )


@ayiin_cmd(
    pattern="resetwarn( (.*)|$)",
    group_only=True,
    admins_only=True,
)
async def rwarn(e):
    reply = await e.get_reply_message()
    if reply:
        user = reply.sender_id
    else:
        try:
            user = e.text.split()[1]
            if user.startswith("@"):
                ok = await e.client.get_entity(user)
                user = ok.id
            else:
                user = int(user)
        except BaseException:
            return await e.eor("Balas ke pesan pengguna")
    reset_warn(e.chat_id, user)
    ok = await e.client.get_entity(user)
    user = inline_mention(ok)
    await e.eor(f"Menghapus Semua Peringatan untuk {user}.")


@ayiin_cmd(
    pattern="warns( (.*)|$)",
    group_only=True,
    admins_only=True,
)
async def twarns(e):
    reply = await e.get_reply_message()
    if reply:
        user = reply.from_id.user_id
    else:
        try:
            user = e.text.split()[1]
            if user.startswith("@"):
                ok = await e.client.get_entity(user)
                user = ok.id
            else:
                user = int(user)
        except BaseException:
            return await e.eor("Balas ke pesan Pengguna", time=5)
    c, r = warns(e.chat_id, user)
    if c and r:
        ok = await e.client.get_entity(user)
        user = inline_mention(ok)
        r = r.split("|$|")
        text = f"Pengguna {user} Telah mendapatkan {c} Peringatan.\n\n"
        for x in range(c):
            text += f"•**{x+1}.** {r[x]}\n"
        await e.eor(text)
    else:
        await e.eor("`Tidak Ada Peringatan`")


@ayiin_cmd(pattern="setwarn( (.*)|$)")
async def warnset(e):
    ok = e.pattern_match.group(1).strip()
    if not ok:
        return await e.eor("stuff")
    if "|" in ok:
        try:
            number, action = int(ok.split()[0]), ok.split()[1]
        except BaseException:
            return await e.eor("`Format Salah`", time=5)
        if ("ban" or "kick" or "mute") not in action:
            return await e.eor("`Hanya mute / ban / kick Opsi yang didukung`", time=5)
        adB.set_key("SETWARN", f"{number} {action}")
        await e.eor(f"Selesai!!! Hitungan Peringatan Anda sekarang {number} Dan Aksi adalah {action}")
    else:
        await e.eor("`Format Salah`", time=5)


CMD_HELP.update(
    {
        "warn": f"**Plugin : **`warn`\
        \n\n  »  **Perintah :** `{cmd}warn`\
        \n  »  **Kegunaan : **Untuk memberikan Peringatan ke member dalam grup\
        \n\n  »  **Perintah :** `{cmd}warns`\
        \n  »  **Kegunaan : **Untuk Melihat Daftar anggota yg di Peringati.\
        \n\n  »  **Perintah :** `{cmd}resetwarn`\
        \n  »  **Kegunaan : **Untuk mereset Peringatan member.\
        \n\n  »  **Perintah :** `{cmd}setwarn`\
        \n  »  **Kegunaan : **Untuk Mengatur Peringatan.\
    "
    }
)
