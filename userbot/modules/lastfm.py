# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
#

from asyncio import sleep
from os import environ
from re import sub
from sys import setrecursionlimit
from urllib import parse

from pylast import LastFMNetwork, MalformedResponseError, User, WSError, md5
from telethon.errors import AboutTooLongError
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.users import GetFullUserRequest

from userbot import BIO_PREFIX, BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import (
    CMD_HELP,
    DEFAULT_BIO,
    LASTFM_API,
    LASTFM_PASSWORD_PLAIN,
    LASTFM_SECRET,
    LASTFM_USERNAME,
    LOGS,
    bot,
    lastfm,
)
from userbot.utils import ayiin_cmd

LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)
if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS:
    lastfm = LastFMNetwork(
        api_key=LASTFM_API,
        api_secret=LASTFM_SECRET,
        username=LASTFM_USERNAME,
        password_hash=LASTFM_PASS,
    )
else:
    lastfm = None

# =================== CONSTANT ===================
LFM_BIO_ENABLED = "**last.fm current music to bio is now enabled.**"
LFM_BIO_DISABLED = (
    "**last.fm current music to bio is now disabled. Bio reverted to default.**"
)
LFM_BIO_RUNNING = "**last.fm current music to bio is already running.**"
LFM_BIO_ERR = "**No option specified.**"
LFM_LOG_ENABLED = "**last.fm logging to bot log is now enabled.**"
LFM_LOG_DISABLED = "**last.fm logging to bot log is now disabled.**"
LFM_LOG_ERR = "**No option specified.**"
ERROR_MSG = "**last.fm module halted, got an unexpected error.**"
# ================================================


class LASTFM:
    def __init__(self):
        self.ARTIST = 0
        self.SONG = 0
        self.USER_ID = 0
        self.LASTFMCHECK = False
        self.RUNNING = False
        self.LastLog = False


LASTFM_ = LASTFM()


async def gettags(track=None, isNowPlaying=None, playing=None):
    if isNowPlaying:
        tags = playing.get_top_tags()
        arg = playing
        if not tags:
            tags = playing.artist.get_top_tags()
    else:
        tags = track.track.get_top_tags()
        arg = track.track
    if not tags:
        tags = arg.artist.get_top_tags()
    tags = "".join(" #" + t.item.__str__() for t in tags[:5])
    tags = sub("^ ", "", tags)
    tags = sub(" ", "_", tags)
    tags = sub("_#", " #", tags)
    return tags


async def artist_and_song(track):
    return f"{track.track}"


async def get_curr_track(lfmbio):  # sourcery no-metrics
    oldartist = ""
    oldsong = ""
    while LASTFM_.LASTFMCHECK:
        try:
            if LASTFM_.USER_ID == 0:
                LASTFM_.USER_ID = (await lfmbio.client.get_me()).id
            user_info = await lfmbio.client(GetFullUserRequest(LASTFM_.USER_ID))
            LASTFM_.RUNNING = True
            playing = User(LASTFM_USERNAME, lastfm).get_now_playing()
            LASTFM_.SONG = playing.get_title()
            LASTFM_.ARTIST = playing.get_artist()
            oldsong = environ.get("oldsong", None)
            oldartist = environ.get("oldartist", None)
            if (
                playing is not None
                and LASTFM_.SONG != oldsong
                and LASTFM_.ARTIST != oldartist
            ):
                environ["oldsong"] = str(LASTFM_.SONG)
                environ["oldartist"] = str(LASTFM_.ARTIST)
                if BIO_PREFIX:
                    lfmbio = f"{BIO_PREFIX} 🎧: {LASTFM_.ARTIST} - {LASTFM_.SONG}"
                else:
                    lfmbio = f"🎧: {LASTFM_.ARTIST} - {LASTFM_.SONG}"
                try:
                    if BOTLOG_CHATID and LASTFM_.LastLog:
                        await lfmbio.client.send_message(
                            BOTLOG_CHATID, f"Attempted to change bio to\n{lfmbio}"
                        )
                    await lfmbio.client(UpdateProfileRequest(about=lfmbio))
                except AboutTooLongError:
                    short_bio = f"🎧: {LASTFM_.SONG}"
                    await lfmbio.client(UpdateProfileRequest(about=short_bio))
            if playing is None and user_info.about != DEFAULT_BIO:
                await sleep(6)
                await lfmbio.client(UpdateProfileRequest(about=DEFAULT_BIO))
                if BOTLOG_CHATID and LASTFM_.LastLog:
                    await lfmbio.client.send_message(
                        BOTLOG_CHATID, f"Reset bio back to\n{DEFAULT_BIO}"
                    )
        except AttributeError:
            try:
                if user_info.about != DEFAULT_BIO:
                    await sleep(6)
                    await bot(UpdateProfileRequest(about=DEFAULT_BIO))
                    if BOTLOG_CHATID and LASTFM_.LastLog:
                        await lfmbio.client.send_message(
                            BOTLOG_CHATID, f"Reset bio back to\n{DEFAULT_BIO}"
                        )
            except FloodWaitError as err:
                if BOTLOG_CHATID and LASTFM_.LastLog:
                    await lfmbio.client.send_message(
                        BOTLOG_CHATID, f"Error changing bio:\n{err}"
                    )
        except (
            FloodWaitError,
            WSError,
            MalformedResponseError,
            AboutTooLongError,
        ) as err:
            if BOTLOG_CHATID and LASTFM_.LastLog:
                await lfmbio.client.send_message(
                    BOTLOG_CHATID, f"Error changing bio:\n{err}"
                )
        await sleep(2)
    LASTFM_.RUNNING = False


@ayiin_cmd(pattern="lastfm$")
async def last_fm(lastFM):
    await lastFM.edit("Processing...")
    preview = None
    playing = User(LASTFM_USERNAME, lastfm).get_now_playing()
    username = f"https://www.last.fm/user/{LASTFM_USERNAME}"
    if playing is not None:
        try:
            image = User(LASTFM_USERNAME, lastfm).get_now_playing().get_cover_image()
        except IndexError:
            image = None
        tags = await gettags(isNowPlaying=True, playing=playing)
        rectrack = parse.quote(f"{playing}")
        rectrack = sub("^", "https://open.spotify.com/search/", rectrack)
        if image:
            output = f"[‎]({image})[{LASTFM_USERNAME}]({username}) __is now listening to:__\n\n• [{playing}]({rectrack})\n"
            preview = True
        else:
            output = f"[{LASTFM_USERNAME}]({username}) __is now listening to:__\n\n• [{playing}]({rectrack})\n"
    else:
        recent = User(LASTFM_USERNAME, lastfm).get_recent_tracks(limit=3)
        playing = User(LASTFM_USERNAME, lastfm).get_now_playing()
        output = f"[{LASTFM_USERNAME}]({username}) __was last listening to:__\n\n"
        for i, track in enumerate(recent):
            LOGS.info(i)
            printable = await artist_and_song(track)
            tags = await gettags(track)
            rectrack = parse.quote(str(printable))
            rectrack = sub("^", "https://open.spotify.com/search/", rectrack)
            output += f"• [{printable}]({rectrack})\n"
            if tags:
                output += f"`{tags}`\n\n"
    if preview is not None:
        await lastFM.edit(f"{output}", parse_mode="md", link_preview=True)
    else:
        await lastFM.edit(f"{output}", parse_mode="md")


@ayiin_cmd(pattern="lastbio (on|off)")
async def lastbio(lfmbio):
    arg = lfmbio.pattern_match.group(1).lower()
    if arg == "on":
        setrecursionlimit(700000)
        if not LASTFM_.LASTFMCHECK:
            LASTFM_.LASTFMCHECK = True
            environ["errorcheck"] = "0"
            await lfmbio.edit(LFM_BIO_ENABLED)
            await sleep(4)
            await get_curr_track(lfmbio)
        else:
            await lfmbio.edit(LFM_BIO_RUNNING)
    elif arg == "off":
        LASTFM_.LASTFMCHECK = False
        LASTFM_.RUNNING = False
        await lfmbio.client(UpdateProfileRequest(about=DEFAULT_BIO))
        await lfmbio.edit(LFM_BIO_DISABLED)
    else:
        await lfmbio.edit(LFM_BIO_ERR)


@ayiin_cmd(pattern="lastlog (on|off)")
async def lastlog(lstlog):
    arg = lstlog.pattern_match.group(1).lower()
    LASTFM_.LastLog = False
    if arg == "on":
        LASTFM_.LastLog = True
        await lstlog.edit(LFM_LOG_ENABLED)
    elif arg == "off":
        LASTFM_.LastLog = False
        await lstlog.edit(LFM_LOG_DISABLED)
    else:
        await lstlog.edit(LFM_LOG_ERR)


CMD_HELP.update(
    {
        "lastfm": f"**Plugin : **`lastfm`\
        \n\n  •  **Syntax :** `{cmd}lastfm`\
        \n  •  **Function : **Menampilkan trek scrobbling saat ini atau scrobble terbaru jika tidak ada yang diputar.\
        \n\n  •  **Syntax :** `{cmd}lastbio` <on/off>\
        \n  •  **Function : **Mengaktifkan / Menonaktifkan pemutaran last.fm saat ini ke bio.\
        \n\n  •  **Syntax :** `{cmd}lastlog` <on/off>\
        \n  •  **Function : **Mengaktifkan / Menonaktifkan bio logging last.fm di grup bot-log.\
    "
    }
)
