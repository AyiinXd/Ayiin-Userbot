import random
import re

from telethon import Button
from telethon.sync import custom, events
from telethon.tl.types import InputWebDocument

from config import var
from AyiinXd import Ayiin, CMD_HELP, bot, ibuild_keyboard, paginate_help
from AyiinXd.ayiin import HOSTED_ON



BTN_URL_REGEX = re.compile(r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)")
dugmeler = CMD_HELP
logo = var.ALIVE_LOGO
logoyins = random.choice(
        [
            "https://telegra.ph/file/9f8e73d387f25b7f27ce5.jpg",
            "https://telegra.ph/file/c935d34b48e45fba22b03.jpg",
            "https://telegra.ph/file/392f69c8717c91b1e8a3b.jpg",
            "https://telegra.ph/file/4c5b756dd13d7a88c866b.jpg",
        ]
)
main_help_button = [
    [
        Button.inline("•• Pʟᴜɢɪɴ ••", data="reopen"),
        Button.inline("Mᴇɴᴜ Vᴄ ••", data="inline_yins"),
    ],
    [
        Button.inline("⚙️ Aʟᴀᴛ Pᴇᴍɪʟɪᴋ", data="yins_langs"),
        Button.url("Pᴇɴɢᴀᴛᴜʀᴀɴ ⚙️", url=f"t.me/{var.BOT_USERNAME}?start="),
    ],
    [Button.inline("•• Kᴇᴍʙᴀʟɪ ••", data="close")],
]


@bot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(rb"reopen")
    )
)
async def on_plug_in_callback_query_handler(event):
    user = await Ayiin.get_me()
    uid = user.id
    owner = user.first_name
    if event.query.user_id == uid or event.query.user_id in var.SUDO_USERS:
        buttons = paginate_help(0, dugmeler, "helpme")
        text = f"**✨ ᴀʏɪɪɴ-ᴜsᴇʀʙᴏᴛ ɪɴʟɪɴᴇ ᴍᴇɴᴜ ✨**\n\n⍟ **ᴅᴇᴘʟᴏʏ :** •[{HOSTED_ON}]•\n⍟ **ᴏᴡɴᴇʀ** {user.first_name}\n⍟ **ᴊᴜᴍʟᴀʜ :** {len(dugmeler)} **Modules**"
        await event.edit(
            text,
            file=logoyins,
            buttons=buttons,
            link_preview=False,
        )
    else:
        reply_pop_up_alert = f"Kamu Tidak diizinkan, ini Userbot Milik {owner}"
        await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


@bot.on(events.InlineQuery)
async def inline_handler(event):
    builder = event.builder
    result = None
    query = event.text
    user = await Ayiin.get_me()
    uid = user.id
    botusername = (await event.client.get_me()).username
    if event.query.user_id == uid and query.startswith(
            "@AyiinChats"):
        buttons = paginate_help(0, dugmeler, "helpme")
        result = await event.builder.photo(
            file=logoyins,
            link_preview=False,
            text=f"**✨ ᴀʏɪɪɴ-ᴜsᴇʀʙᴏᴛ ɪɴʟɪɴᴇ ᴍᴇɴᴜ ✨**\n\n⍟ **ᴅᴇᴘʟᴏʏ :** •[{HOSTED_ON}]•\n⍟ **ᴏᴡɴᴇʀ :** {user.first_name}\n⍟ **ᴊᴜᴍʟᴀʜ :** {len(dugmeler)} **Modules**",
            buttons=main_help_button,
        )
    elif query.startswith("repo"):
        result = builder.article(
            title="Repository",
            description="Repository Ayiin - Userbot",
            url="https://t.me/AyiinChats",
            thumb=InputWebDocument(
                var.INLINE_PIC,
                0,
                "image/jpeg",
                []),
            text="**Ayiin-Userbot**\n➖➖➖➖➖➖➖➖➖➖\n✧  **ʀᴇᴘᴏ :** [AyiinXd](https://t.me/AyiinXd)\n✧ **sᴜᴘᴘᴏʀᴛ :** @AyiinChats\n✧ **ʀᴇᴘᴏsɪᴛᴏʀʏ :** [Ayiin-Userbot](https://github.com/AyiinXd/Ayiin-Userbot)\n➖➖➖➖➖➖➖➖➖➖",
            buttons=[
                [
                    custom.Button.url(
                        "ɢʀᴏᴜᴘ",
                        "https://t.me/AyiinChats"),
                    custom.Button.url(
                        "ʀᴇᴘᴏ",
                        "https://github.com/AyiinXd/Ayiin-Userbot"),
                ],
            ],
            link_preview=False,
        )
    elif query.startswith("Inline buttons"):
        markdown_note = query[14:]
        prev = 0
        note_data = ""
        buttons = []
        for match in BTN_URL_REGEX.finditer(markdown_note):
            n_escapes = 0
            to_check = match.start(1) - 1
            while to_check > 0 and markdown_note[to_check] == "\\":
                n_escapes += 1
                to_check -= 1
            if n_escapes % 2 == 0:
                buttons.append(
                    (match.group(2), match.group(3), bool(
                        match.group(4))))
                note_data += markdown_note[prev: match.start(1)]
                prev = match.end(1)
            elif n_escapes % 2 == 1:
                note_data += markdown_note[prev:to_check]
                prev = match.start(1) - 1
            else:
                break
        else:
            note_data += markdown_note[prev:]
        message_text = note_data.strip()
        tl_ib_buttons = ibuild_keyboard(buttons)
        result = builder.article(
            title="Inline creator",
            text=message_text,
            buttons=tl_ib_buttons,
            link_preview=False,
        )
    else:
        result = builder.article(
            title="✨ ᴀʏɪɪɴ-ᴜsᴇʀʙᴏᴛ ✨",
            description="Ayiin - Userbot | Telethon",
            url="https://t.me/AyiinChannel",
            thumb=InputWebDocument(
                var.INLINE_PIC,
                0,
                "image/jpeg",
                []),
            text=f"**Ayiin-Userbot**\n➖➖➖➖➖➖➖➖➖➖\n✧ **ᴏᴡɴᴇʀ :** [{user.first_name}](tg://user?id={user.id})\n✧ **ᴀssɪsᴛᴀɴᴛ:** {botusername}\n➖➖➖➖➖➖➖➖➖➖\n**ᴜᴘᴅᴀᴛᴇs :** @AyiinChannel\n➖➖➖➖➖➖➖➖➖➖",
            buttons=[
                [
                    custom.Button.url(
                        "ɢʀᴏᴜᴘ",
                        "https://t.me/AyiinChats"),
                    custom.Button.url(
                        "ʀᴇᴘᴏ",
                        "https://github.com/AyiinXd/Ayiin-Userbot"),
                ],
            ],
            link_preview=False,
        )
    await event.answer(
        [result], switch_pm="👥 USERBOT PORTAL", switch_pm_param="start"
    )

@bot.on(
    events.callbackquery.CallbackQuery(
        data=re.compile(rb"helpme_next\((.+?)\)")
    )
)
async def on_plug_in_callback_query_handler(event):
    user = await Ayiin.get_me()
    uid = user.id
    owner = user.first_name
    if event.query.user_id == uid or event.query.user_id in var.SUDO_USERS:
        current_page_number = int(
            event.data_match.group(1).decode("UTF-8"))
        buttons = paginate_help(
            current_page_number + 1, dugmeler, "helpme")
        await event.edit(buttons=buttons)
    else:
        reply_pop_up_alert = (
            f"Kamu Tidak diizinkan, ini Userbot Milik {owner}"
        )
        await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

@bot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(rb"helpme_close\((.+?)\)")
    )
)
async def on_plug_in_callback_query_handler(event):
    user = await Ayiin.get_me()
    uid = user.id
    owner = user.first_name
    if event.query.user_id == uid or event.query.user_id in var.SUDO_USERS:  # @Kyy-Userbot
        # https://t.me/TelethonChat/115200
        await event.edit(
            file=logoyins,
            link_preview=True,
            buttons=main_help_button)

@bot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(rb"gcback")
    )
)
async def gback_handler(event):
    user = await Ayiin.get_me()
    uid = user.id
    owner = user.first_name
    if event.query.user_id == uid or event.query.user_id in var.SUDO_USERS:  # @Ayiin-Userbot
        # https://t.me/TelethonChat/115200
        text = (
            f"**✨ ᴀʏɪɪɴ-ᴜsᴇʀʙᴏᴛ ɪɴʟɪɴᴇ ᴍᴇɴᴜ ✨**\n\n✧ **ᴏᴡɴᴇʀ :** [{user.first_name}](tg://user?id={user.id})\n✧ **ᴊᴜᴍʟᴀʜ :** {len(dugmeler)} **Modules**")
        await event.edit(
            text,
            file=logoyins,
            link_preview=True,
            buttons=main_help_button)


@bot.on(events.CallbackQuery(data=b"inline_yins"))
async def about(event):
    user = await Ayiin.get_me()
    uid = user.id
    owner = user.first_name
    if event.query.user_id == uid or event.query.user_id in var.SUDO_USERS:
        await event.edit(f"""
•Menu• - Voice chat group untuk [{user.first_name}](tg://user?id={user.id})
""",
                            buttons=[
                                [
                                    Button.inline("⍟ ᴠᴄ ᴘʟᴜɢɪɴ ⍟",
                                                data="vcplugin"),
                                    Button.inline("⍟ ᴠᴄ ᴛᴏᴏʟs ⍟",
                                                data="vctools")],
                                [custom.Button.inline(
                                    "ʙᴀᴄᴋ", data="gcback")],
                            ]
                            )
    else:
        reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
        await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

@bot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(rb"vcplugin")
    )
)
async def on_plug_in_callback_query_handler(event):
    user = await Ayiin.get_me()
    uid = user.id
    owner = user.first_name
    cmd = var.CMD_HANDLER
    if event.query.user_id == uid or event.query.user_id in var.SUDO_USERS:
        text = (
            f"""
✘ **Perintah yang tersedia di vcplugin** ✘

»  **Perintah : **`{cmd}play` <Judul Lagu/Link YT>
»  **Kegunaan :** __Untuk Memutar Lagu di voice chat group dengan akun kamu.__

»  **Perintah : **`{cmd}vplay` <Judul Video/Link YT>
»  **Kegunaan :** __Untuk Memutar Video di voice chat group dengan akun kamu.__

»  **Perintah : **`{cmd}end`
»  **Kegunaan :** __Untuk Memberhentikan video/lagu yang sedang putar di voice chat group.__

»  **Perintah : **`{cmd}skip`
»  **Kegunaan :** __Untuk Melewati video/lagu yang sedang di putar.__

»  **Perintah : **`{cmd}pause`
»  **Kegunaan :** __Untuk memberhentikan video/lagu yang sedang diputar.__

»  **Perintah : **`{cmd}resume`
»  **Kegunaan :** __Untuk melanjutkan pemutaran video/lagu yang sedang diputar.__

»  **Perintah : **`{cmd}volume` 1-200
»  **Kegunaan :** __Untuk mengubah volume (Membutuhkan Hak admin).__

»  **Perintah : **`{cmd}playlist`
»  **Kegunaan :** __Untuk menampilkan daftar putar Lagu/Video.__
""")
        await event.edit(
            text,
            file=logoyins,
            link_preview=True,
            buttons=[Button.inline("ʙᴀᴄᴋ", data="inline_yins")])
    else:
        reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
        await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

@bot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(rb"vctools")
    )
)
async def on_plug_in_callback_query_handler(event):
    user = await Ayiin.get_me()
    uid = user.id
    owner = user.first_name
    cmd = var.CMD_HANDLER
    if event.query.user_id == uid or event.query.user_id in var.SUDO_USERS:
        text = (
            f"""
✘ **Perintah yang tersedia di vctools** ✘

»  **Perintah : **`{cmd}startvc`
»  **Kegunaan :** __Untuk Memulai voice chat group.__

»  **Perintah : **`{cmd}stopvc`
»  **Kegunaan :** __Untuk Memberhentikan voice chat group.__

»  **Perintah :** `{cmd}joinvc` atau `{cmd}joinvc` <chatid/username gc>
»  **Kegunaan :** __Untuk Bergabung ke voice chat group.__

»  **Perintah : **`{cmd}leavevc` atau `{cmd}leavevc` <chatid/username gc>
»  **Kegunaan :** __Untuk Turun dari voice chat group.__

»  **Perintah : **`{cmd}vctitle` <title vcg>
»  **Kegunaan :** __Untuk Mengubah title/judul voice chat group.__

»  **Perintah : **`{cmd}vcinvite`
»  **Kegunaan :** __Mengundang Member group ke voice chat group.__
""")
        await event.edit(
            text,
            file=logoyins,
            link_preview=True,
            buttons=[Button.inline("ʙᴀᴄᴋ", data="inline_yins")])
    else:
        reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
        await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


@bot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(rb"yins_langs")
    )
)
async def on_plug_in_callback_query_handler(event):
    user = await Ayiin.get_me()
    uid = user.id
    owner = user.first_name
    cmd = var.CMD_HANDLER
    if event.query.user_id == uid or event.query.user_id in var.SUDO_USERS:
        text = (
            f"""
✘ **Perintah yang tersedia di tools** ✘

»  **Perintah :** `{cmd}lang`
»  **Kegunaan : **Untuk Mengubah Bahasa.

»  **Perintah :** `{cmd}string`
»  **Kegunaan : **Untuk Membuat String Session.
""")
        await event.edit(
            text,
            file=logoyins,
            link_preview=True,
            buttons=[Button.inline("ʙᴀᴄᴋ", data="gcback")])
    else:
        reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
        await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

@bot.on(events.CallbackQuery(data=b"close"))
async def close(event):
    buttons = [
        (custom.Button.inline("ᴍᴀɪɴ ᴍᴇɴᴜ", data="gcback"),),
    ]
    await event.edit("**ᴍᴇɴᴜ ᴅɪᴛᴜᴛᴜᴘ**", file=logoyins, buttons=buttons)

@bot.on(
    events.callbackquery.CallbackQuery(
        data=re.compile(rb"helpme_prev\((.+?)\)")
    )
)
async def on_plug_in_callback_query_handler(event):
    user = await Ayiin.get_me()
    uid = user.id
    owner = user.first_name
    if event.query.user_id == uid or event.query.user_id in var.SUDO_USERS:
        current_page_number = int(
            event.data_match.group(1).decode("UTF-8"))
        buttons = paginate_help(
            current_page_number - 1, dugmeler, "helpme")
        await event.edit(buttons=buttons)
    else:
        reply_pop_up_alert = f"Kamu Tidak diizinkan, ini Userbot Milik {owner}"
        await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ub_modul_(.*)")))
async def on_plug_in_callback_query_handler(event):
    user = await Ayiin.get_me()
    uid = user.id
    owner = user.first_name
    cmd = var.CMD_HANDLER
    if event.query.user_id == uid or event.query.user_id in var.SUDO_USERS:
        modul_name = event.data_match.group(1).decode("UTF-8")

        cmdhel = str(CMD_HELP[modul_name])
        if len(cmdhel) > 950:
            help_string = (
                str(CMD_HELP[modul_name])
                .replace("`", "")
                .replace("**", "")[:950]
                + "..."
                + f"\n\nBaca Teks Berikutnya Ketik {cmd}help "
                + modul_name
                + " "
            )
        else:
            help_string = (str(CMD_HELP[modul_name]).replace(
                "`", "").replace("**", ""))

        reply_pop_up_alert = (
            help_string
            if help_string is not None
            else "{} Tidak ada dokumen yang telah ditulis untuk modul.".format(
                modul_name
            )
        )
        await event.edit(
            reply_pop_up_alert, buttons=[
                Button.inline("ʙᴀᴄᴋ", data="reopen")]
        )

    else:
        reply_pop_up_alert = f"Kamu Tidak diizinkan, ini Userbot Milik {owner}"
        await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
