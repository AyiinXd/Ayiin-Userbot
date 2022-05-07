# Copyright (C) 2020 Aidil Aryanto.
# All rights reserved.

import asyncio
import glob
import os
import shutil
import time

import deezloader
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from pylast import User
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import DocumentAttributeAudio, DocumentAttributeVideo

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import (
    CMD_HELP,
    DEEZER_ARL_TOKEN,
    LASTFM_USERNAME,
    TEMP_DOWNLOAD_DIRECTORY,
    lastfm,
)
from AyiinXd.ayiin import ayiin_cmd, bash, chrome, eor, progress
from AyiinXd.ayiin.FastTelethon import upload_file
from Stringyins import get_string


async def getmusic(cat):
    video_link = ""
    search = cat
    driver = await chrome()
    driver.get("https://www.youtube.com/results?search_query=" + search)
    user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
    for i in user_data:
        video_link = i.get_attribute("href")
        break
    command = f"yt-dlp -x --add-metadata --embed-thumbnail --no-progress --audio-format mp3 {video_link}"
    await bash(command)
    return video_link


async def getmusicvideo(cat):
    video_link = ""
    search = cat
    driver = await chrome()
    driver.get("https://www.youtube.com/results?search_query=" + search)
    user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
    for i in user_data:
        video_link = i.get_attribute("href")
        break
    command = (
        'yt-dlp -f "[filesize<50M]" --no-progress --merge-output-format mp4 '
        + video_link
    )
    await bash(command)


@ayiin_cmd(pattern="song (.*)")
async def _(event):
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
        xx = await eor(event, get_string("com_1"))
    elif reply.message:
        query = reply.message
        await xx.edit(get_string("getm_1").format("lagu"))
    else:
        await xx.edit(get_string("getm_2"))
        return

    await getmusic(str(query))
    loa = glob.glob("*.mp3")[0]
    await xx.edit(get_string("getm_3"))
    c_time = time.time()
    with open(loa, "rb") as f:
        result = await upload_file(
            client=event.client,
            file=f,
            name=loa,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, event, c_time, "[UPLOAD]", loa)
            ),
        )
    await event.client.send_file(
        event.chat_id,
        result,
        allow_cache=False,
    )
    await event.delete()
    await bash("rm -rf *.mp3")


@ayiin_cmd(pattern="vsong(?: |$)(.*)")
async def _(event):
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
        xx = await eor(event, get_string("com_1"))
    elif reply:
        query = str(reply.message)
        await xx.edit(get_string("getm_1").format("lagu video"))
    else:
        await xx.edit(get_string("getm_2"))
        return
    await getmusicvideo(query)
    l = glob.glob(("*.mp4")) + glob.glob(("*.mkv")) + glob.glob(("*.webm"))
    if l:
        await xx.edit(get_string("vsng_1"))
    else:
        await xx.edit(get_string("vsng_2").format(query)
                      )
        return
    try:
        loa = l[0]
        metadata = extractMetadata(createParser(loa))
        duration = metadata.get(
            "duration").seconds if metadata.has("duration") else 0
        width = metadata.get("width") if metadata.has("width") else 0
        height = metadata.get("height") if metadata.has("height") else 0
        await bash("cp *mp4 thumb.mp4")
        await bash("ffmpeg -i thumb.mp4 -vframes 1 -an -s 480x360 -ss 5 thumb.jpg")
        thumb_image = "thumb.jpg"
        c_time = time.time()
        with open(loa, "rb") as f:
            result = await upload_file(
                client=event.client,
                file=f,
                name=loa,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, event, c_time, "[UPLOAD]", loa)
                ),
            )
        await event.client.send_file(
            event.chat_id,
            result,
            force_document=False,
            thumb=thumb_image,
            allow_cache=False,
            caption=query,
            supports_streaming=True,
            attributes=[
                DocumentAttributeVideo(
                    duration=duration,
                    w=width,
                    h=height,
                    round_message=False,
                    supports_streaming=True,
                )
            ],
        )
        await xx.edit(get_string("vsng_3").format(query))
        os.remove(thumb_image)
        await bash("rm *.mkv *.mp4 *.webm")
    except BaseException:
        os.remove(thumb_image)
        await bash("rm *.mkv *.mp4 *.webm")
        return


@ayiin_cmd(pattern="smd (?:(now)|(.*) - (.*))")
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1) == "now":
        playing = User(LASTFM_USERNAME, lastfm).get_now_playing()
        if playing is None:
            return await event.edit(
                get_string("smdn_1").format("data scrobbling")
            )
        artist = playing.get_artist()
        song = playing.get_title()
    else:
        artist = event.pattern_match.group(2)
        song = event.pattern_match.group(3)
    track = str(artist) + " - " + str(song)
    chat = "@SpotifyMusicDownloaderBot"
    try:
        await event.edit(get_string("smdn_2").format("Mendapatkan"))
        async with event.client.conversation(chat) as conv:
            await asyncio.sleep(2)
            await event.edit(get_string("com_5"))
            try:
                response = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=752979930)
                )
                msg = await event.client.send_message(chat, track)
                respond = await response
                res = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=752979930)
                )
                r = await res
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.reply(
                    get_string("smdn_3").format("@SpotifyMusicDownloaderBot")
                )
                return
            await event.client.forward_messages(event.chat_id, respond.message)
        await event.client.delete_messages(conv.chat_id, [msg.id, r.id, respond.id])
        await event.delete()
    except TimeoutError:
        return await event.edit(
            get_string("smdn_4").format("@SpotifyMusicDownloaderBot")
        )


@ayiin_cmd(pattern="net (?:(now)|(.*) - (.*))")
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1) == "now":
        playing = User(LASTFM_USERNAME, lastfm).get_now_playing()
        if playing is None:
            return await event.edit(get_string("smdn_1").format("scrobble saat ini")
                                    )
        artist = playing.get_artist()
        song = playing.get_title()
    else:
        artist = event.pattern_match.group(2)
        song = event.pattern_match.group(3)
    track = str(artist) + " - " + str(song)
    chat = "@WooMaiBot"
    link = f"/netease {track}"
    await event.edit(get_string("com_2"))
    try:
        async with event.client.conversation(chat) as conv:
            await asyncio.sleep(2)
            await event.edit(get_string("com_1"))
            try:
                msg = await conv.send_message(link)
                response = await conv.get_response()
                respond = await conv.get_response()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.reply(get_string("smdn_3").format("@WooMaiBot"))
                return
            await event.edit(get_string("smdn_2").format("Mengirim"))
            await asyncio.sleep(3)
            await event.client.send_file(event.chat_id, respond)
        await event.client.delete_messages(
            conv.chat_id, [msg.id, response.id, respond.id]
        )
        await event.delete()
    except TimeoutError:
        return await event.edit(get_string("smdn_4").format("@WooMaiBot")
                                )


@ayiin_cmd(pattern="mhb(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit(get_string("mhbb_1"))
    else:
        await event.edit(get_string("com_1"))
    chat = "@MusicsHunterBot"
    try:
        async with event.client.conversation(chat) as conv:
            try:
                msg_start = await conv.send_message("/start")
                response = await conv.get_response()
                msg = await conv.send_message(d_link)
                details = await conv.get_response()
                song = await conv.get_response()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit(get_string("smdn_3").format("@MusicsHunterBot"))
                return
            await event.client.send_file(event.chat_id, song, caption=details.text)
            await event.client.delete_messages(
                conv.chat_id, [msg_start.id, response.id, msg.id, details.id, song.id]
            )
            await event.delete()
    except TimeoutError:
        return await event.edit(get_string("smdn_4").format("@MusicsHunterBot")
                                )


@ayiin_cmd(pattern="deez (.+?|) (FLAC|MP3\\_320|MP3\\_256|MP3\\_128)")
async def _(event):
    """DeezLoader by @An0nimia. Ported for UniBorg by @SpEcHlDe"""
    if event.fwd_from:
        return

    ARL_TOKEN = DEEZER_ARL_TOKEN

    if ARL_TOKEN is None:
        await event.edit(get_string("inar_1"))
        return

    try:
        loader = deezloader.Login(ARL_TOKEN)
    except Exception as er:
        await event.edit(str(er))
        return

    temp_dl_path = os.path.join(TEMP_DOWNLOAD_DIRECTORY, str(time.time()))
    if not os.path.exists(temp_dl_path):
        os.makedirs(temp_dl_path)

    required_link = event.pattern_match.group(1)
    required_qty = event.pattern_match.group(2)

    await event.edit(get_string("com_1"))

    if "spotify" in required_link:
        if "track" in required_link:
            required_track = loader.download_trackspo(
                required_link,
                output=temp_dl_path,
                quality=required_qty,
                recursive_quality=True,
                recursive_download=True,
                not_interface=True,
            )
            await event.edit(get_string("com_6"))
            await upload_track(required_track, event)
            shutil.rmtree(temp_dl_path)
            await event.delete()

        elif "album" in required_link:
            reqd_albums = loader.download_albumspo(
                required_link,
                output=temp_dl_path,
                quality=required_qty,
                recursive_quality=True,
                recursive_download=True,
                not_interface=True,
                zips=False,
            )
            await event.edit(get_string("com_6"))
            for required_track in reqd_albums:
                await upload_track(required_track, event)
            shutil.rmtree(temp_dl_path)
            await event.delete()

    elif "deezer" in required_link:
        if "track" in required_link:
            required_track = loader.download_trackdee(
                required_link,
                output=temp_dl_path,
                quality=required_qty,
                recursive_quality=True,
                recursive_download=True,
                not_interface=True,
            )
            await event.edit(get_string("com_6"))
            await upload_track(required_track, event)
            shutil.rmtree(temp_dl_path)
            await event.delete()

        elif "album" in required_link:
            reqd_albums = loader.download_albumdee(
                required_link,
                output=temp_dl_path,
                quality=required_qty,
                recursive_quality=True,
                recursive_download=True,
                not_interface=True,
                zips=False,
            )
            await event.edit(get_string("com_6"))
            for required_track in reqd_albums:
                await upload_track(required_track, event)
            shutil.rmtree(temp_dl_path)
            await event.delete()

    else:
        await event.edit(get_string("wrong1"))


async def upload_track(track_location, message):
    metadata = extractMetadata(createParser(track_location))
    duration = metadata.get(
        "duration").seconds if metadata.has("duration") else 0
    title = metadata.get("title") if metadata.has("title") else ""
    performer = metadata.get("artist") if metadata.has("artist") else ""
    document_attributes = [
        DocumentAttributeAudio(
            duration=duration,
            voice=False,
            title=title,
            performer=performer,
            waveform=None,
        )
    ]
    supports_streaming = True
    force_document = False
    caption_rts = os.path.basename(track_location)
    c_time = time.time()
    with open(track_location, "rb") as f:
        result = await upload_file(
            client=message.client,
            file=f,
            name=track_location,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, message, c_time, "[UPLOAD]", track_location)
            ),
        )
    await message.client.send_file(
        message.chat_id,
        result,
        caption=caption_rts,
        force_document=force_document,
        supports_streaming=supports_streaming,
        allow_cache=False,
        attributes=document_attributes,
    )
    os.remove(track_location)


CMD_HELP.update(
    {
        "getmusic": f"**Plugin : **`getmusic`\
        \n\n  »  **Perintah :** `{cmd}smd` <nama lagu>\
        \n  »  **Kegunaan : **Mendowload lagu dari bot @SpotifyMusicDownloaderBot\
        \n\n  »  **Perintah :** `{cmd}smd now`\
        \n  »  **Kegunaan : **Unduh penggunaan scrobble LastFM saat ini dari bot @SpotifyMusicDownloaderBot\
        \n\n  »  **Perintah :** `{cmd}net` <nama lagu>\
        \n  »  **Kegunaan : **Mendowload lagu dari bot @WooMaiBot\
        \n\n  »  **Perintah :** `{cmd}net now`\
        \n  »  **Kegunaan : **Unduh penggunaan scrobble LastFM saat ini dari bot @WooMaiBot\
        \n\n  »  **Perintah :** `{cmd}mhb` <Link Spotify/Deezer>\
        \n  »  **Kegunaan : **Mendowload lagu dari Spotify atau Deezer dari bot @MusicsHunterBot\
        \n\n  »  **Perintah :** `{cmd}deez` <link spotify/deezer> FORMAT\
        \n  »  **Kegunaan : **Mendowload lagu dari deezer atau spotify.\
        \n  •  **Format   : ** `FLAC`, `MP3_320`, `MP3_256`, `MP3_128`.\
    "
    }
)
