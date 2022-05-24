# Credits: @mrismanaziz
# Thanks To @tofik_dn || https://github.com/tofikdn
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

from pytgcalls import StreamType
from pytgcalls.types import Update
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import (
    HighQualityAudio,
    HighQualityVideo,
    LowQualityVideo,
    MediumQualityVideo,
)
from telethon.tl import types
from telethon.utils import get_display_name
from youtubesearchpython import VideosSearch

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd import PLAY_PIC as fotoplay
from AyiinXd import QUEUE_PIC as ngantri
from AyiinXd import call_py
from AyiinXd.ayiin import ayiin_cmd, bash, eod, eor
from AyiinXd.ayiin.chattitle import CHAT_TITLE
from AyiinXd.ayiin.queues.queues import (
    QUEUE,
    add_to_queue,
    clear_queue,
    get_queue,
    pop_an_item,
)
from AyiinXd.ayiin.thumbnail import gen_thumb
from Stringyins import get_string


def vcmention(user):
    full_name = get_display_name(user)
    if not isinstance(user, types.User):
        return full_name
    return f"[{full_name}](tg://user?id={user.id})"


def ytsearch(query: str):
    try:
        search = VideosSearch(query, limit=1).result()
        data = search["result"][0]
        songname = data["title"]
        url = data["link"]
        duration = data["duration"]
        thumbnail = data["thumbnails"][0]["url"]
        videoid = data["id"]
        return [songname, url, duration, thumbnail, videoid]
    except Exception as e:
        print(e)
        return 0


async def ytdl(link: str):
    stdout, stderr = await bash(
        f'yt-dlp -g -f "best[height<=?720][width<=?1280]" {link}'
    )
    if stdout:
        return 1, stdout.split("\n")[0]
    return 0, stderr


async def skip_item(chat_id: int, x: int):
    if chat_id not in QUEUE:
        return 0
    chat_queue = get_queue(chat_id)
    try:
        songname = chat_queue[x][0]
        chat_queue.pop(x)
        return songname
    except Exception as e:
        print(e)
        return 0


async def skip_current_song(chat_id: int):
    if chat_id not in QUEUE:
        return 0
    chat_queue = get_queue(chat_id)
    if len(chat_queue) == 1:
        await call_py.leave_group_call(chat_id)
        clear_queue(chat_id)
        return 1
    songname = chat_queue[1][0]
    url = chat_queue[1][1]
    link = chat_queue[1][2]
    type = chat_queue[1][3]
    RESOLUSI = chat_queue[1][4]
    if type == "Audio":
        await call_py.change_stream(
            chat_id,
            AudioPiped(
                url,
                HighQualityAudio(),
            ),
        )
    elif type == "Video":
        if RESOLUSI == 720:
            hm = HighQualityVideo()
        elif RESOLUSI == 480:
            hm = MediumQualityVideo()
        elif RESOLUSI == 360:
            hm = LowQualityVideo()
        await call_py.change_stream(
            chat_id, AudioVideoPiped(url, HighQualityAudio(), hm)
        )
    pop_an_item(chat_id)
    return [songname, link, type]


@ayiin_cmd(pattern="play(?:\\s|$)([\\s\\S]*)", group_only=True)
async def vc_play(event):
    title = event.pattern_match.group(1)
    replied = await event.get_reply_message()
    chat = await event.get_chat()
    titlegc = chat.title
    chat_id = event.chat_id
    from_user = vcmention(event.sender)
    if (
        replied
        and not replied.audio
        and not replied.voice
        and not title
        or not replied
        and not title
    ):
        return await eor(event, get_string("play_1"))
    elif replied and not replied.audio and not replied.voice or not replied:
        botyins = await eor(event, get_string("com_1"))
        query = event.text.split(maxsplit=1)[1]
        search = ytsearch(query)
        if search == 0:
            await botyins.edit(get_string("play_2")
            )
        else:
            songname = search[0]
            title = search[0]
            url = search[1]
            duration = search[2]
            thumbnail = search[3]
            videoid = search[4]
            titlegc = chat.title
            ctitle = await CHAT_TITLE(titlegc)
            thumb = await gen_thumb(thumbnail, title, videoid, ctitle)
            hm, ytlink = await ytdl(url)
            if hm == 0:
                await botyins.edit(f"`{ytlink}`")
            elif chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                caption = get_string("play_3").format(pos, songname, url, duration, from_user)
                await botyins.delete()
                await event.client.send_file(
                    chat_id, thumb, caption=caption, reply_to=event.reply_to_msg_id
                )
            else:
                try:
                    await call_py.join_group_call(
                        chat_id,
                        AudioPiped(
                            ytlink,
                            HighQualityAudio(),
                        ),
                        stream_type=StreamType().pulse_stream,
                    )
                    add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                    caption = get_string("play_4").format(songname, url, duration, from_user)
                    await botyins.delete()
                    await event.client.send_file(
                        chat_id, thumb, caption=caption, reply_to=event.reply_to_msg_id
                    )
                except Exception as ep:
                    clear_queue(chat_id)
                    await botyins.edit(f"`{ep}`")

    else:
        botyins = await eor(event, get_string("com_5"))
        dl = await replied.download_media()
        link = f"https://t.me/c/{chat.id}/{event.reply_to_msg_id}"
        if replied.audio:
            songname = "Telegram Music Player"
        elif replied.voice:
            songname = "Voice Note"
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            caption = get_string("play_5").format(pos, songname, link, chat_id, from_user)
            await event.client.send_file(
                chat_id, ngantri, caption=caption, reply_to=event.reply_to_msg_id
            )
            await botyins.delete()
        else:
            try:
                await call_py.join_group_call(
                    chat_id,
                    AudioPiped(
                        dl,
                        HighQualityAudio(),
                    ),
                    stream_type=StreamType().pulse_stream,
                )
                add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                caption = get_string("play_6").format(songname, link, chat_id, from_user)
                await event.client.send_file(
                    chat_id, fotoplay, caption=caption, reply_to=event.reply_to_msg_id
                )
                await botyins.delete()
            except Exception as ep:
                clear_queue(chat_id)
                await botyins.edit(f"`{ep}`")


@ayiin_cmd(pattern="vplay(?:\\s|$)([\\s\\S]*)", group_only=True)
async def vc_vplay(event):
    title = event.pattern_match.group(1)
    replied = await event.get_reply_message()
    chat = await event.get_chat()
    titlegc = chat.title
    chat_id = event.chat_id
    from_user = vcmention(event.sender)
    if (
        replied
        and not replied.video
        and not replied.document
        and not title
        or not replied
        and not title
    ):
        return await eor(event, get_string("vplay_1"))
    if replied and not replied.video and not replied.document:
        xnxx = await eor(event, get_string("com_"))
        query = event.text.split(maxsplit=1)[1]
        search = ytsearch(query)
        RESOLUSI = 720
        hmmm = HighQualityVideo()
        if search == 0:
            await xnxx.edit(get_string("vplay_2")
            )
        else:
            songname = search[0]
            title = search[0]
            url = search[1]
            duration = search[2]
            thumbnail = search[3]
            videoid = search[4]
            ctitle = await CHAT_TITLE(titlegc)
            thumb = await gen_thumb(thumbnail, title, videoid, ctitle)
            hm, ytlink = await ytdl(url)
            if hm == 0:
                await xnxx.edit(f"`{ytlink}`")
            elif chat_id in QUEUE:
                pos = add_to_queue(
                    chat_id, songname, ytlink, url, "Video", RESOLUSI)
                caption = get_string("vplay_3").format(pos, songname, url, duration, from_user)
                await xnxx.delete()
                await event.client.send_file(
                    chat_id, thumb, caption=caption, reply_to=event.reply_to_msg_id
                )
            else:
                try:
                    await call_py.join_group_call(
                        chat_id,
                        AudioVideoPiped(
                            ytlink,
                            HighQualityAudio(),
                            hmmm,
                        ),
                        stream_type=StreamType().pulse_stream,
                    )
                    add_to_queue(
                        chat_id,
                        songname,
                        ytlink,
                        url,
                        "Video",
                        RESOLUSI)
                    await xnxx.edit(get_string("vplay_4").format(songname, url, duration, from_user),
                        link_preview=False,
                    )
                except Exception as ep:
                    clear_queue(chat_id)
                    await xnxx.edit(get_string("error_1").format(ep))

    elif replied:
        xnxx = await eor(event, get_string("com_5"))
        dl = await replied.download_media()
        link = f"https://t.me/c/{chat.id}/{event.reply_to_msg_id}"
        if len(event.text.split()) < 2:
            RESOLUSI = 720
        else:
            pq = event.text.split(maxsplit=1)[1]
            RESOLUSI = int(pq)
        if replied.video or replied.document:
            songname = "Telegram Video Player"
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Video", RESOLUSI)
            caption = get_string("vplay_5").format(pos, songname, link, chat_id, from_user)
            await event.client.send_file(
                chat_id, ngantri, caption=caption, reply_to=event.reply_to_msg_id
            )
            await xnxx.delete()
        else:
            if RESOLUSI == 360:
                hmmm = LowQualityVideo()
            elif RESOLUSI == 480:
                hmmm = MediumQualityVideo()
            elif RESOLUSI == 720:
                hmmm = HighQualityVideo()
            try:
                await call_py.join_group_call(
                    chat_id,
                    AudioVideoPiped(
                        dl,
                        HighQualityAudio(),
                        hmmm,
                    ),
                    stream_type=StreamType().pulse_stream,
                )
                add_to_queue(chat_id, songname, dl, link, "Video", RESOLUSI)
                caption = get_string("vplay_6").format(songname, link, chat_id, from_user)
                await xnxx.delete()
                await event.client.send_file(
                    chat_id, fotoplay, caption=caption, reply_to=event.reply_to_msg_id
                )
            except Exception as ep:
                clear_queue(chat_id)
                await xnxx.edit(get_string("error_1").format(ep))
    else:
        xnxx = await eor(event, get_string("com_2"))
        query = event.text.split(maxsplit=1)[1]
        search = ytsearch(query)
        RESOLUSI = 720
        hmmm = HighQualityVideo()
        if search == 0:
            await xnxx.edit(get_string("vplay_7"))
        else:
            songname = search[0]
            title = search[0]
            url = search[1]
            duration = search[2]
            thumbnail = search[3]
            videoid = search[4]
            ctitle = await CHAT_TITLE(titlegc)
            thumb = await gen_thumb(thumbnail, title, videoid, ctitle)
            hm, ytlink = await ytdl(url)
            if hm == 0:
                await xnxx.edit(f"`{ytlink}`")
            elif chat_id in QUEUE:
                pos = add_to_queue(
                    chat_id, songname, ytlink, url, "Video", RESOLUSI)
                caption = get_string("vplay_8").format(pos, songname, url, duration, from_user)
                await xnxx.delete()
                await event.client.send_file(
                    chat_id, thumb, caption=caption, reply_to=event.reply_to_msg_id
                )
            else:
                try:
                    await call_py.join_group_call(
                        chat_id,
                        AudioVideoPiped(
                            ytlink,
                            HighQualityAudio(),
                            hmmm,
                        ),
                        stream_type=StreamType().pulse_stream,
                    )
                    add_to_queue(
                        chat_id,
                        songname,
                        ytlink,
                        url,
                        "Video",
                        RESOLUSI)
                    caption = get_string().format(songname, url, duration, from_user)
                    await xnxx.delete()
                    await event.client.send_file(
                        chat_id, thumb, caption=caption, reply_to=event.reply_to_msg_id
                    )
                except Exception as ep:
                    clear_queue(chat_id)
                    await xnxx.edit(get_string("error_1").format(ep))


@ayiin_cmd(pattern="end$", group_only=True)
async def vc_end(event):
    chat_id = event.chat_id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await eor(event, get_string("eplay_1"))
        except Exception as e:
            await eod(event, get_string("error_1").format(e))
    else:
        await eod(event, get_string("eplay_2"))


@ayiin_cmd(pattern="skip(?:\\s|$)([\\s\\S]*)", group_only=True)
async def vc_skip(event):
    chat_id = event.chat_id
    if len(event.text.split()) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await eod(event, get_string("eplay_2"))
        elif op == 1:
            await eod(event, get_string("splay_1"), time=10)
        else:
            await eor(
                event, get_string("splay_2").format(op[0], op[1]),
                link_preview=False,
            )
    else:
        skip = event.text.split(maxsplit=1)[1]
        DELQUE = get_string("splay_3")
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x != 0:
                    hm = await skip_item(chat_id, x)
                    if hm != 0:
                        DELQUE = DELQUE + "\n" + f"**#{x}** - {hm}"
            await event.edit(DELQUE)


@ayiin_cmd(pattern="pause$", group_only=True)
async def vc_pause(event):
    chat_id = event.chat_id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await eor(event, get_string("pplay_1"))
        except Exception as e:
            await eod(event, get_string("error_1").format(e))
    else:
        await eor(event, get_string("eplay_2"))


@ayiin_cmd(pattern="resume$", group_only=True)
async def vc_resume(event):
    chat_id = event.chat_id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await eor(event, get_string("rplay_1"))
        except Exception as e:
            await eor(event, get_string("error_1").format(e))
    else:
        await eod(event, get_string("eplay_2"))


@ayiin_cmd(pattern=r"volume(?: |$)(.*)", group_only=True)
async def vc_volume(event):
    query = event.pattern_match.group(1)
    me = await event.client.get_me()
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    chat_id = event.chat_id
    if not admin and not creator:
        return await eod(event, get_string("stvc_1").format(me.first_name), time=30)

    if chat_id in QUEUE:
        try:
            await call_py.change_volume_call(chat_id, volume=int(query))
            await eor(event, get_string("volmp_1").format(query)
            )
        except Exception as e:
            await eod(event, get_string("error_1").format(e), time=30)
    else:
        await eod(event, get_string("eplay_2"))


@ayiin_cmd(pattern="playlist$", group_only=True)
async def vc_playlist(event):
    chat_id = event.chat_id
    if chat_id in QUEUE:
        chat_queue = get_queue(chat_id)
        if len(chat_queue) == 1:
            await eor(
                event, get_string("playl_1").format(chat_queue[0][0], chat_queue[0][2], chat_queue[0][3]),
                link_preview=False,
            )
        else:
            PLAYLIST = get_string("play_2").format(chat_queue[0][0], chat_queue[0][2], chat_queue[0][3])
            l = len(chat_queue)
            for x in range(1, l):
                hmm = chat_queue[x][0]
                hmmm = chat_queue[x][2]
                hmmmm = chat_queue[x][3]
                PLAYLIST = PLAYLIST + "\n" + \
                    f"**#{x}** - [{hmm}]({hmmm}) | `{hmmmm}`"
            await edit_or_reply(event, PLAYLIST, link_preview=False)
    else:
        await eod(event, get_string("eplay_2"))


@call_py.on_stream_end()
async def stream_end_handler(_, u: Update):
    chat_id = u.chat_id
    print(chat_id)
    await skip_current_song(chat_id)


@call_py.on_closed_voice_chat()
async def closedvc(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)


@call_py.on_left()
async def leftvc(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)


@call_py.on_kicked()
async def kickedvc(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)


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
        \n\n  »  **Perintah :** `{cmd}pause`\
        \n  »  **Kegunaan : **Untuk memberhentikan video/lagu yang sedang diputar\
        \n\n  »  **Perintah :** `{cmd}resume`\
        \n  »  **Kegunaan : **Untuk melanjutkan pemutaran video/lagu yang sedang diputar\
        \n\n  »  **Perintah :** `{cmd}volume` 1-200\
        \n  »  **Kegunaan : **Untuk mengubah volume (Membutuhkan Hak admin)\
        \n\n  »  **Perintah :** `{cmd}playlist`\
        \n  »  **Kegunaan : **Untuk menampilkan daftar putar Lagu/Video\
    "
    }
)
