import random
import re

from telethon import Button
from telethon.sync import custom, events
from telethon.tl.types import InputWebDocument

from config import var
from AyiinXd import Ayiin, CMD_HELP, bot, ibuild_keyboard, paginate_help
from AyiinXd.ayiin import HOSTED_ON


BTN_URL_REGEX = re.compile(r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)")
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
logoyins = random.choice(
    [
        "https://telegra.ph/file/9f8e73d387f25b7f27ce5.jpg",
        "https://telegra.ph/file/c935d34b48e45fba22b03.jpg",
        "https://telegra.ph/file/392f69c8717c91b1e8a3b.jpg",
        "https://telegra.ph/file/4c5b756dd13d7a88c866b.jpg",
    ]
)



@bot.on(events.InlineQuery)
async def inline_handler(event):
    builder = event.builder
    result = None
    query = event.text
    user = await Ayiin.get_me()
    uid = user.id
    if event.query.user_id == user.id and query.startswith(
            "@AyiinChats"):
        buttons = paginate_help(0, CMD_HELP, "helpme")
        result = await event.builder.photo(
            file=logoyins,
            link_preview=False,
            text=f"**✨ ᴀʏɪɪɴ-ᴜsᴇʀʙᴏᴛ ɪɴʟɪɴᴇ ᴍᴇɴᴜ ✨**\n\n⍟ **ᴅᴇᴘʟᴏʏ :** •[{HOSTED_ON}]•\n⍟ **ᴏᴡɴᴇʀ :** {user.first_name}\n⍟ **ᴊᴜᴍʟᴀʜ :** {len(CMD_HELP)} **Modules**",
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
            text=f"**Ayiin-Userbot**\n➖➖➖➖➖➖➖➖➖➖\n✧ **ᴏᴡɴᴇʀ :** [{user.first_name}](tg://user?id={user.id})\n✧ **ᴀssɪsᴛᴀɴᴛ:** {var.BOT_USERNAME}\n➖➖➖➖➖➖➖➖➖➖\n**ᴜᴘᴅᴀᴛᴇs :** @AyiinChannel\n➖➖➖➖➖➖➖➖➖➖",
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
