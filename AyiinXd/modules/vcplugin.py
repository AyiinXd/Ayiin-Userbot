# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import asyncio, re, os

from telethon.tl import types
from telethon.errors.rpcerrorlist import ChatSendMediaForbiddenError, MessageIdInvalidError

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, LOGS, INLINE_PIC
from AyiinXd.ayiin import ayiin_cmd, bash, eod, eor
from AyiinXd.ayiin.pytgcalls import (
    add_to_queue,
    mediainfo,
    file_download,
    is_url_ok,
    vid_download,
    download,
    Ayiin,
    VC_QUEUE,
    list_queue,
)

from Stringyins import get_string

from .stats import inline_mention


@ayiin_cmd(pattern="vplay")
async def video_c(event):
    xx = await event.eor(get_string("com_1"))
    chat = event.chat_id
    from_user = inline_mention(event.sender)
    reply, song = None, None
    if event.reply_to:
        reply = await event.get_reply_message()
    if len(event.text.split()) > 1:
        input = event.text.split(maxsplit=1)[1]
        tiny_input = input.split()[0]
        if tiny_input[0] in ["@", "-"]:
            try:
                chat = await event.client.parse_id(tiny_input)
            except Exception as er:
                LOGS.exception(er)
                return await xx.edit(str(er))
            try:
                song = input.split(maxsplit=1)[1]
            except BaseException:
                pass
        else:
            song = input
    if not (reply or song):
        return await xx.eor("Silakan tentukan nama lagu atau balas file video!")
    await xx.eor("`Mengunduh dan mengonversi...`")
    if reply and reply.media and mediainfo(reply.media).startswith("video"):
        song, thumb, title, link, duration = await file_download(xx, reply)
    else:
        is_link = is_url_ok(song)
        if is_link is False:
            return await xx.eor(f"`{song}`\n\nNot a playable link.🥱")
        if is_link is None:
            song, thumb, title, link, duration = await vid_download(song)
        elif re.search("youtube", song) or re.search("youtu", song):
            song, thumb, title, link, duration = await vid_download(song)
        else:
            song, thumb, title, link, duration = (
                song,
                "https://telegra.ph/file/22bb2349da20c7524e4db.mp4",
                song,
                song,
                "♾",
            )
    Xd = Ayiin(chat, xx, True)
    if not (await Xd.vc_joiner()):
        return
    text = "🎸 **Now playing:** [{}]({})\n⏰ **Duration:** `{}`\n👥 **Chat:** `{}`\n🙋‍♂ **Requested by:** {}".format(
        title, link, duration, chat, from_user
    )
    try:
        await xx.reply(
            text,
            file=thumb,
            link_preview=False,
        )
    except ChatSendMediaForbiddenError:
        await xx.reply(text, link_preview=False)
    await asyncio.sleep(1)
    await Xd.group_call.start_video(song)
    await xx.delete()


@ayiin_cmd(pattern="play")
async def play_music_(event):
    if "playfrom" in event.text.split()[0]:
        return  # For PlayFrom Conflict
    try:
        xx = await event.eor(get_string("com_1"))
    except MessageIdInvalidError:
        # Changing the way, things work
        xx = event
        xx.out = False
    chat = event.chat_id
    from_user = inline_mention(event.sender)
    reply, song = None, None
    if event.reply_to:
        reply = await event.get_reply_message()
    if len(event.text.split()) > 1:
        input = event.text.split(maxsplit=1)[1]
        tiny_input = input.split()[0]
        if tiny_input[0] in ["@", "-"]:
            try:
                chat = await event.client.parse_id(tiny_input)
            except Exception as er:
                LOGS.exception(er)
                return await xx.edit(str(er))
            try:
                song = input.split(maxsplit=1)[1]
            except IndexError:
                pass
            except Exception as e:
                return await event.eor(str(e))
        else:
            song = input
    if not (reply or song):
        return await xx.eor("Please specify a song name or reply to a audio file !", time=5
        )
    await xx.eor("`Mengunduh dan mengonversi...`")
    if reply and reply.media and mediainfo(reply.media).startswith(("audio", "video")):
        song, thumb, song_name, link, duration = await file_download(xx, reply)
    else:
        song, thumb, song_name, link, duration = await download(song)
        if len(link.strip().split()) > 1:
            link = link.strip().split()
    Xd = Ayiin(chat, event)
    song_name = song_name[:30] + "..."
    if not Xd.group_call.is_connected:
        if not (await Xd.vc_joiner()):
            return
        await Xd.group_call.start_audio(song)
        if isinstance(link, list):
            for lin in link[1:]:
                add_to_queue(chat, song, lin, lin, None, from_user, duration)
            link = song_name = link[0]
        text = "🎸 <strong>Now playing: <a href={}>{}</a>\n⏰ Duration:</strong> <code>{}</code>\n👥 <strong>Chat:</strong> <code>{}</code>\n🙋‍♂ <strong>Requested by: {}</strong>".format(
            link, song_name, duration, chat, from_user
        )
        try:
            await xx.reply(
                text,
                file=thumb,
                link_preview=False,
                parse_mode="html",
            )
            await xx.delete()
        except ChatSendMediaForbiddenError:
            await xx.eor(text, link_preview=False)
        if thumb and os.path.exists(thumb):
            os.remove(thumb)
    else:
        if not (
            reply
            and reply.media
            and mediainfo(reply.media).startswith(("audio", "video"))
        ):
            song = None
        if isinstance(link, list):
            for lin in link[1:]:
                add_to_queue(chat, song, lin, lin, None, from_user, duration)
            link = song_name = link[0]
        add_to_queue(chat, song, song_name, link, thumb, from_user, duration)
        return await xx.eor(
            f"▶ Added 🎵 <a href={link}>{song_name}</a> to queue at #{list(VC_QUEUE[chat].keys())[-1]}.",
            parse_mode="html",
        )


@ayiin_cmd(pattern="playfrom")
async def play_music_(event):
    msg = await event.eor(get_string("com_1"))
    chat = event.chat_id
    limit = 10
    from_user = inline_mention(event)
    if len(event.text.split()) <= 1:
        return await msg.edit(
            "Use in Proper Format\n`.playfrom <channel username> ; <limit>`"
        )
    input = event.text.split(maxsplit=1)[1]
    if ";" in input:
        try:
            limit = input.split(";")
            input = limit[0].strip()
            limit = int(limit[1].strip()) if limit[1].strip().isdigit() else 10
            input = await event.client.parse_id(input)
        except (IndexError, ValueError):
            pass
    try:
        fromchat = (await event.client.get_entity(input)).id
    except Exception as er:
        return await msg.eor(str(er))
    await msg.eor("`• Started Playing from Channel....`")
    send_message = True
    Xd = Ayiin(chat, event)
    count = 0
    async for song in event.client.iter_messages(
        fromchat, limit=limit, wait_time=5, filter=types.InputMessagesFilterMusic
    ):
        count += 1
        song, thumb, song_name, link, duration = await file_download(
            msg, song, fast_download=False
        )
        song_name = song_name[:30] + "..."
        if not Xd.group_call.is_connected:
            if not (await Xd.vc_joiner()):
                return
            await Xd.group_call.start_audio(song)
            text = "🎸 <strong>Now playing: <a href={}>{}</a>\n⏰ Duration:</strong> <code>{}</code>\n👥 <strong>Chat:</strong> <code>{}</code>\n🙋‍♂ <strong>Requested by: {}</strong>".format(
                link, song_name, duration, chat, from_user
            )
            try:
                await msg.reply(
                    text,
                    file=thumb,
                    link_preview=False,
                    parse_mode="html",
                )
            except ChatSendMediaForbiddenError:
                await msg.reply(text, link_preview=False, parse_mode="html")
            if thumb and os.path.exists(thumb):
                os.remove(thumb)
        else:
            add_to_queue(chat, song, song_name, link, thumb, from_user, duration)
            if send_message and count == 1:
                await msg.eor(
                    f"▶ Added 🎵 <strong><a href={link}>{song_name}</a></strong> to queue at <strong>#{list(VC_QUEUE[chat].keys())[-1]}.</strong>",
                    parse_mode="html",
                )
                send_message = False


@ayiin_cmd(pattern="radio")
async def radio_mirchi(e):
    xx = await e.eor(get_string("com_1"))
    if len(e.text.split()) <= 1:
        return await xx.eor("Are You Kidding Me?\nWhat to Play?")
    input = e.text.split()
    if input[1][0] in ["-", "@"]:
        try:
            chat = await e.client.parse_id(input[1])
        except Exception as er:
            return await xx.edit(str(er))
        song = e.text.split(maxsplit=2)[2]
    else:
        song = e.text.split(maxsplit=1)[1]
        chat = e.chat_id
    if not is_url_ok(song):
        return await xx.eor(f"`{song}`\n\nNot a playable link.🥱")
    Xd = Ayiin(chat, e)
    if not Xd.group_call.is_connected and not (await Xd.vc_joiner()):
        return
    await Xd.group_call.start_audio(song)
    await xx.reply(
        f"• Started Radio 📻\n\n• Station : `{song}`",
        file=INLINE_PIC,
    )
    await xx.delete()


@ayiin_cmd(pattern="(live|ytlive)")
async def live_stream(e):
    xx = await e.eor(get_string("com_1"))
    if len(e.text.split()) <= 1:
        return await xx.eor("Are You Kidding Me?\nWhat to Play?")
    input = e.text.split()
    if input[1][0] in ["@", "-"]:
        chat = await e.client.parse_id(input[1])
        song = e.text.split(maxsplit=2)[2]
    else:
        song = e.text.split(maxsplit=1)[1]
        chat = e.chat_id
    if not is_url_ok(song):
        return await xx.eor(f"`{song}`\n\nNot a playable link.🥱")
    is_live_vid = False
    if re.search("youtu", song):
        is_live_vid = (await bash(f'youtube-dl -j "{song}" | jq ".is_live"'))[0]
    if is_live_vid != "true":
        return await xx.eor(f"Only Live Youtube Urls supported!\n{song}")
    file, thumb, title, link, duration = await download(song)
    Xd = Ayiin(chat, e)
    if not Xd.group_call.is_connected and not (await Xd.vc_joiner()):
        return
    from_user = inline_mention(e.sender)
    await xx.reply(
        "🎸 **Now playing:** [{}]({})\n⏰ **Duration:** `{}`\n👥 **Chat:** `{}`\n🙋‍♂ **Requested by:** {}".format(
            title, link, duration, chat, from_user
        ),
        file=thumb,
        link_preview=False,
    )
    await xx.delete()
    await Xd.group_call.start_audio(file)


@ayiin_cmd(pattern="end$")
async def mute(event):
    chat_id = event.chat_id
    if chat_id in VC_QUEUE:
        try:
            await Ayiin(chat_id).group_call.leave()
            VC_QUEUE.pop(chat_id)
            await event.reply("**Berhasil Menghentikan Streaming**")
        except Exception as e:
            await eor(event, get_string("error_1").format(e))
    else:
        await event.eor("Gak ada streaming yang diputar bego !")


@ayiin_cmd(pattern="mutevc$")
async def mute(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor(get_string("error_1").format(str(e)))
    else:
        chat = event.chat_id
    Xd = Ayiin(chat)
    await Xd.group_call.set_is_mute(True)
    await event.eor("`Muted playback in this chat.`")


@ayiin_cmd(pattern="unmutevc$")
async def unmute(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor(get_string("error_1").format(str(e)))
    else:
        chat = event.chat_id
    Xd = Ayiin(chat)
    await Xd.group_call.set_is_mute(False)
    await event.eor("`UnMuted playback in this chat.`")


@ayiin_cmd(pattern="pause$")
async def pauser(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor(get_string("error_1").format(str(e)))
    else:
        chat = event.chat_id
    Xd = Ayiin(chat)
    await Xd.group_call.set_pause(True)
    await event.eor(get_string("pplay_1"))


@ayiin_cmd(pattern="resume$")
async def resumer(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor(get_string("error_1").format(str(e)))
    else:
        chat = event.chat_id
    Xd = Ayiin(chat)
    await Xd.group_call.set_pause(False)
    await event.eor(get_string("rplay_1"))


@ayiin_cmd(pattern="replay$")
async def replayer(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor(get_string("error_1").format(str(e)))
    else:
        chat = event.chat_id
    Xd = Ayiin(chat)
    Xd.group_call.restart_playout()
    await event.eor("`Re-playing the current song.`")


@ayiin_cmd(pattern="playlist$")
async def lstqueue(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor(get_string("error_1").format(str(e)))
    else:
        chat = event.chat_id
    q = list_queue(chat)
    if not q:
        return await event.eor("Maaf Tidak Ada Playlist...")
    await event.eor("• <strong>Queue:</strong>\n\n{}".format(q), parse_mode="html")


@ayiin_cmd(pattern="delplaylist")
async def clean_queue(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor("**ERROR:**\n{}".format(str(e)))
    else:
        chat = event.chat_id
    if VC_QUEUE.get(chat):
        VC_QUEUE.pop(chat)
    await event.eor("Playlist Berhasil Dihapus", time=5)


CMD_HELP.update(
    {
        "vcplugin": f"**Plugin : **`vcplugin`\
        \n\n  »  **Perintah :** `{cmd}play` <Judul Lagu/Link YT>\
        \n  »  **Kegunaan : **Untuk Memutar Lagu di voice chat group dengan akun kamu\
        \n\n  »  **Perintah :** `{cmd}vplay` <Judul Video/Link YT>\
        \n  »  **Kegunaan : **Untuk Memutar Video di voice chat group dengan akun kamu\
        \n\n  »  **Perintah :** `{cmd}end`\
        \n  »  **Kegunaan : **Untuk Memberhentikan video/lagu yang sedang putar di voice chat group\
        \n\n  »  **Perintah :** `{cmd}skip`\
        \n  »  **Kegunaan : **Untuk Melewati video/lagu yang sedang di putar\
        \n\n  »  **Perintah :** `{cmd}unmutevc`\
        \n  »  **Kegunaan : **Untuk membunyikan video/lagu yang sedang dimute\
        \n\n  »  **Perintah :** `{cmd}mutevc`\
        \n  »  **Kegunaan : **Untuk membisukan pemutaran video/lagu yang sedang diputar\
        \n\n  »  **Perintah :** `{cmd}pause`\
        \n  »  **Kegunaan : **Untuk memberhentikan video/lagu yang sedang diputar\
        \n\n  »  **Perintah :** `{cmd}resume`\
        \n  »  **Kegunaan : **Untuk melanjutkan pemutaran video/lagu yang sedang diputar\
        \n\n  »  **Perintah :** `{cmd}volume` 1-200\
        \n  »  **Kegunaan : **Untuk mengubah volume (Membutuhkan Hak admin)\
        \n\n  »  **Perintah :** `{cmd}playlist`\
        \n  »  **Kegunaan : **Untuk menampilkan daftar putar Lagu/Video\
        \n\n  »  **Perintah :** `{cmd}delplaylist`\
        \n  »  **Kegunaan : **Untuk menghapus daftar putar Lagu/Video\
        \n\n  »  **Perintah :** `{cmd}replay`\
        \n  »  **Kegunaan : **Untuk memutar ulang video/lagu yang sedang diputar\
    "
    }
)
