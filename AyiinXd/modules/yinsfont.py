# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, edit_delete, edit_or_reply


def monospace(text):
    style = {
        'a': '𝚊',
        'b': '𝚋',
        'c': '𝚌',
        'd': '𝚍',
        'e': '𝚎',
        'f': '𝚏',
        'g': '𝚐',
        'h': '𝚑',
        'i': '𝚒',
        'j': '𝚓',
        'k': '𝚔',
        'l': '𝚕',
        'm': '𝚖',
        'n': '𝚗',
        'o': '𝚘',
        'p': '𝚙',
        'q': '𝚚',
        'r': '𝚛',
        's': '𝚜',
        't': '𝚝',
        'u': '𝚞',
        'v': '𝚟',
        'w': '𝚠',
        'x': '𝚡',
        'y': '𝚢',
        'z': '𝚣',
        'A': '𝙰',
        'B': '𝙱',
        'C': '𝙲',
        'D': '𝙳',
        'E': '𝙴',
        'F': '𝙵',
        'G': '𝙶',
        'H': '𝙷',
        'I': '𝙸',
        'J': '𝙹',
        'K': '𝙺',
        'L': '𝙻',
        'M': '𝙼',
        'N': '𝙽',
        'O': '𝙾',
        'P': '𝙿',
        'Q': '𝚀',
        'R': '𝚁',
        'S': '𝚂',
        'T': '𝚃',
        'U': '𝚄',
        'V': '𝚅',
        'W': '𝚆',
        'X': '𝚇',
        'Y': '𝚈',
        'Z': '𝚉'}
    for i, j in style.items():
        text = text.replace(i, j)
    return text


def smallcap(text):
    style = {
        'a': 'ᴀ',
        'b': 'ʙ',
        'c': 'ᴄ',
        'd': 'ᴅ',
        'e': 'ᴇ',
        'f': 'ғ',
        'g': 'ɢ',
        'h': 'ʜ',
        'i': 'ɪ',
        'j': 'ᴊ',
        'k': 'ᴋ',
        'l': 'ʟ',
        'm': 'ᴍ',
        'n': 'ɴ',
        'o': 'ᴏ',
        'p': 'ᴘ',
        'q': 'ǫ',
        'r': 'ʀ',
        's': 's',
        't': 'ᴛ',
        'u': 'ᴜ',
        'v': 'ᴠ',
        'w': 'ᴡ',
        'x': 'x',
        'y': 'ʏ',
        'z': 'ᴢ',
        'A': 'ᴀ',
        'B': 'ʙ',
        'C': 'ᴄ',
        'D': 'ᴅ',
        'E': 'ᴇ',
        'F': 'ғ',
        'G': 'ɢ',
        'H': 'ʜ',
        'I': 'ɪ',
        'J': 'ᴊ',
        'K': 'ᴋ',
        'L': 'ʟ',
        'M': 'ᴍ',
        'N': 'ɴ',
        'O': 'ᴏ',
        'P': 'ᴘ',
        'Q': 'ǫ',
        'R': 'ʀ',
        'S': 's',
        'T': 'ᴛ',
        'U': 'ᴜ',
        'V': 'ᴠ',
        'W': 'ᴡ',
        'X': 'x',
        'Y': 'ʏ',
        'Z': 'ᴢ',
    }
    for i, j in style.items():
        text = text.replace(i, j)
    return text


def outline(text):
    style = {
        'a': '𝕒',
        'b': '𝕓',
        'c': '𝕔',
        'd': '𝕕',
        'e': '𝕖',
        'f': '𝕗',
        'g': '𝕘',
        'h': '𝕙',
        'i': '𝕚',
        'j': '𝕛',
        'k': '𝕜',
        'l': '𝕝',
        'm': '𝕞',
        'n': '𝕟',
        'o': '𝕠',
        'p': '𝕡',
        'q': '𝕢',
        'r': '𝕣',
        's': '𝕤',
        't': '𝕥',
        'u': '𝕦',
        'v': '𝕧',
        'w': '𝕨',
        'x': '𝕩',
        'y': '𝕪',
        'z': '𝕫',
        'A': '𝔸',
        'B': '𝔹',
        'C': 'ℂ',
        'D': '𝔻',
        'E': '𝔼',
        'F': '𝔽',
        'G': '𝔾',
        'H': 'ℍ',
        'I': '𝕀',
        'J': '𝕁',
        'K': '𝕂',
        'L': '𝕃',
        'M': '𝕄',
        'N': 'ℕ',
        'O': '𝕆',
        'P': 'ℙ',
        'Q': 'ℚ',
        'R': 'ℝ',
        'S': '𝕊',
        'T': '𝕋',
        'U': '𝕌',
        'V': '𝕍',
        'W': '𝕎',
        'X': '𝕏',
        'Y': '𝕐',
        'Z': 'ℤ'}
    for i, j in style.items():
        text = text.replace(i, j)
    return text


def bold(text):
    style = {
        'a': '𝗮',
        'b': '𝗯',
        'c': '𝗰',
        'd': '𝗱',
        'e': '𝗲',
        'f': '𝗳',
        'g': '𝗴',
        'h': '𝗵',
        'i': '𝗶',
        'j': '𝗷',
        'k': '𝗸',
        'l': '𝗹',
        'm': '𝗺',
        'n': '𝗻',
        'o': '𝗼',
        'p': '𝗽',
        'q': '𝗾',
        'r': '𝗿',
        's': '𝘀',
        't': '𝘁',
        'u': '𝘂',
        'v': '𝘃',
        'w': '𝘄',
        'x': '𝘅',
        'y': '𝘆',
        'z': '𝘇',
        'A': '𝗔',
        'B': '𝗕',
        'C': '𝗖',
        'D': '𝗗',
        'E': '𝗘',
        'F': '𝗙',
        'G': '𝗚',
        'H': '𝗛',
        'I': '𝗜',
        'J': '𝗝',
        'K': '𝗞',
        'L': '𝗟',
        'M': '𝗠',
        'N': '𝗡',
        'O': '𝗢',
        'P': '𝗣',
        'Q': '𝗤',
        'R': '𝗥',
        'S': '𝗦',
        'T': '𝗧',
        'U': '𝗨',
        'V': '𝗩',
        'W': '𝗪',
        'X': '𝗫',
        'Y': '𝗬',
        'Z': '𝗭'}
    for i, j in style.items():
        text = text.replace(i, j)
    return text


def bolditalic(text):
    style = {
        'a': '𝙖',
        'b': '𝙗',
        'c': '𝙘',
        'd': '𝙙',
        'e': '𝙚',
        'f': '𝙛',
        'g': '𝙜',
        'h': '𝙝',
        'i': '𝙞',
        'j': '𝙟',
        'k': '𝙠',
        'l': '𝙡',
        'm': '𝙢',
        'n': '𝙣',
        'o': '𝙤',
        'p': '𝙥',
        'q': '𝙦',
        'r': '𝙧',
        's': '𝙨',
        't': '𝙩',
        'u': '𝙪',
        'v': '𝙫',
        'w': '𝙬',
        'x': '𝙭',
        'y': '𝙮',
        'z': '𝙯',
        'A': '𝘼',
        'B': '𝘽',
        'C': '𝘾',
        'D': '𝘿',
        'E': '𝙀',
        'F': '𝙁',
        'G': '𝙂',
        'H': '𝙃',
        'I': '𝙄',
        'J': '𝙅',
        'K': '𝙆',
        'L': '𝙇',
        'M': '𝙈',
        'N': '𝙉',
        'O': '𝙊',
        'P': '𝙋',
        'Q': '𝙌',
        'R': '𝙍',
        'S': '𝙎',
        'T': '𝙏',
        'U': '𝙐',
        'V': '𝙑',
        'W': '𝙒',
        'X': '𝙓',
        'Y': '𝙔',
        'Z': '𝙕'}
    for i, j in style.items():
        text = text.replace(i, j)
    return text


def script(text):
    style = {
        'a': '𝒶',
        'b': '𝒷',
        'c': '𝒸',
        'd': '𝒹',
        'e': 'ℯ',
        'f': '𝒻',
        'g': 'ℊ',
        'h': '𝒽',
        'i': '𝒾',
        'j': '𝒿',
        'k': '𝓀',
        'l': '𝓁',
        'm': '𝓂',
        'n': '𝓃',
        'o': 'ℴ',
        'p': '𝓅',
        'q': '𝓆',
        'r': '𝓇',
        's': '𝓈',
        't': '𝓉',
        'u': '𝓊',
        'v': '𝓋',
        'w': '𝓌',
        'x': '𝓍',
        'y': '𝓎',
        'z': '𝓏',
        'A': '𝒜',
        'B': 'ℬ',
        'C': '𝒞',
        'D': '𝒟',
        'E': 'ℰ',
        'F': 'ℱ',
        'G': '𝒢',
        'H': 'ℋ',
        'I': 'ℐ',
        'J': '𝒥',
        'K': '𝒦',
        'L': 'ℒ',
        'M': 'ℳ',
        'N': '𝒩',
        'O': '𝒪',
        'P': '𝒫',
        'Q': '𝒬',
        'R': 'ℛ',
        'S': '𝒮',
        'T': '𝒯',
        'U': '𝒰',
        'V': '𝒱',
        'W': '𝒲',
        'X': '𝒳',
        'Y': '𝒴',
        'Z': '𝒵'}
    for i, j in style.items():
        text = text.replace(i, j)
    return text


def bubbles(text):
    style = {
        'a': 'Ⓐ︎',
        'b': 'Ⓑ︎',
        'c': 'Ⓒ︎',
        'd': 'Ⓓ︎',
        'e': 'Ⓔ︎',
        'f': 'Ⓕ︎',
        'g': 'Ⓖ︎',
        'h': 'Ⓗ︎',
        'i': 'Ⓘ︎',
        'j': 'Ⓙ︎',
        'k': 'Ⓚ︎',
        'l': 'Ⓛ︎',
        'm': 'Ⓜ︎',
        'n': 'Ⓝ︎',
        'o': 'Ⓞ︎',
        'p': 'Ⓟ︎',
        'q': 'Ⓠ︎',
        'r': 'Ⓡ︎',
        's': 'Ⓢ︎',
        't': 'Ⓣ︎',
        'u': 'Ⓤ︎',
        'v': 'Ⓥ︎',
        'w': 'Ⓦ︎',
        'x': 'Ⓧ︎',
        'y': 'Ⓨ︎',
        'z': 'Ⓩ︎'}
    for i, j in style.items():
        text = text.replace(i, j)
    return text


def blackbubbles(text):
    style = {
        'a': '🅐︎',
        'b': '🅑︎',
        'c': '🅒︎',
        'd': '🅓︎',
        'e': '🅔︎',
        'f': '🅕︎',
        'g': '🅖︎',
        'h': '🅗︎',
        'i': '🅘︎',
        'j': '🅙︎',
        'k': '🅙︎',
        'l': '🅛︎',
        'm': '🅜︎',
        'n': '🅝︎',
        'o': '🅞︎',
        'p': '🅟︎',
        'q': '🅠︎',
        'r': '🅡︎',
        's': '🅢︎',
        't': '🅣︎',
        'u': '🅤︎',
        'v': '🅥︎',
        'w': '🅦︎',
        'x': '🅧︎',
        'y': '🅨︎',
        'z': '🅩︎'}
    for i, j in style.items():
        text = text.replace(i, j)
    return text


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


@ayiin_cmd(pattern=r"font (monospace|smallcap|outline|bold|bolditalic|script|bubbles|blackbubbles) (.*)")
async def font_yins(ayiin):
    if ayiin.pattern_match.group(1) == "monospace":
        xd = monospace
    if ayiin.pattern_match.group(1) == "smallcap":
        xd = smallcap
    if ayiin.pattern_match.group(1) == "outline":
        xd = outline
    if ayiin.pattern_match.group(1) == "bold":
        xd = bold
    if ayiin.pattern_match.group(1) == "bolditalic":
        xd = bolditalic
    if ayiin.pattern_match.group(1) == "script":
        xd = script
    if ayiin.pattern_match.group(1) == "bubbles":
        xd = bubbles
    if ayiin.pattern_match.group(1) == "blackbubbles":
        xd = blackbubbles
    kontol = xd(ayiin.pattern_match.group(2))
    if not kontol:
        return await edit_delete(ayiin, "`Ngetik Yang Bener Bego...`")

    await ayiin.edit(f"{kontol}")
    await ayiin.reply("**𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙚𝙙 𝘽𝙮 :** ✧ 𝙰𝚈𝙸𝙸𝙽-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ✧")


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

arguments = [
    "smallcap",
    "monospace",
    "outline",
    "script",
    "blackbubbles",
    "bubbles",
    "bold",
    "bolditalic"
]

fonts = [
    "smallcap",
    "monospace",
    "outline",
    "script",
    "blackbubbles",
    "bubbles",
    "bold",
    "bolditalic"
]

_default = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
_smallcap = "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘϙʀsᴛᴜᴠᴡxʏᴢABCDEFGHIJKLMNOPQRSTUVWXYZ"
_monospace = "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉"
_outline = "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ"
_script = "𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵"
_blackbubbles = "🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩"
_bubbles = "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ"
_bold = "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭"
_bolditalic = "𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕"


async def fonts(text):
    r = requests.get(
        f"{fonts}?type=fonts&text={text}"
    ).json()
    geng = r.get("message")
    kapak = url(geng)
    if not kapak:
        return "check syntax once more"
    with open("chat_id", "msg") as f:
        f.write(requests.get(geng).content)
    text = await event.send_message("fonts").convert("text")
    event.get_message("fonts", "text")
    return "fonts"


def gen_font(text, new_font):
    new_font = " ".join(new_font).split()
    for q in text:
        if q in _default:
            new = new_font[_default.index(q)]
            text = text.replace(q, new)
    return text


@ayiin_cmd(pattern="font(.*)(|$)")
async def _(ayiin):
    input = ayiin.pattern_match.group(1).strip()
    reply = await ayiin.get_reply_message()
    reply_to_id = ayiin.message
    if ayiin.reply_to_msg_id:
        reply_to_id = await ayiin.get_reply_message()

    if not reply:
        try:
            _ = input.split(":", maxsplit=1)
            font = _[0][:-1]
            text = _[0]
        except IndexError:
            return await edit_delete(ayiin, reply_to_id)
    elif not input:
        return await edit_delete(ayiin, "`Kasih Font Dong Bego :/`")

    else:
        font = input
        text = reply.message
    if not font:
        return await edit_delete(ayiin, f"`{font} Tidak Ada Dalam Daftar Font Kentod...`", time=5)
    if font == "smallcap":
        yins = gen_font(text, _smallcap)
    elif font == "monospace":
        yins = gen_font(text, _monospace)
    elif font == "outline":
        yins = gen_font(text, _outline)
    elif font == "script":
        yins = gen_font(text, _script)
    elif font == "blackbubbles":
        yins = gen_font(text, _blackbubbles)
    elif font == "bubbles":
        yins = gen_font(text, _bubbles)
    elif font == "bold":
        yins = gen_font(text, _bold)
    elif font == "bolditalic":
        yins = gen_font(text, _bolditalic)
    await edit_or_reply(ayiin, yins)
    await ayiin.reply("**𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙚𝙙 𝘽𝙮 :** ✧ 𝙰𝚈𝙸𝙸𝙽-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ✧")
    if not yins:
        await ayiin.reply("Ketik Yang Bener Bego!!!")


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


@ayiin_cmd(pattern="lf(.*)(|$)")
async def fonts(yins):
    ayiin = await edit_or_reply(yins,
                                "**»» ᴅᴀғᴛᴀʀ ғᴏɴᴛs ««**\n"
                                "**         ☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎**\n\n\n"
                                "**• smallcap » ᴀʏɪɪɴ**\n"
                                "**• monospace » 𝙰𝚈𝙸𝙸𝙽**\n"
                                "**• outline » 𝔸𝕐𝕀𝕀ℕ**\n"
                                "**• script » 𝒜𝒴ℐℐ𝒩**\n"
                                "**• blackbubbles » 🅐︎🅨︎🅘︎🅘︎🅝︎**\n"
                                "**• bubbles » Ⓐ︎Ⓨ︎Ⓘ︎Ⓘ︎Ⓝ︎**\n"
                                "**• bold » 𝗔𝗬𝗜𝗜𝗡**\n"
                                "**• bolditalic » 𝘼𝙔𝙄𝙄𝙉**\n\n"
                                "**   ✧ 𝙰𝚈𝙸𝙸𝙽-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ✧**")


CMD_HELP.update(
    {
        "yinsfont": f"**Plugin : **`yinsfont`\
        \n\n  »  **Perintah :** `{cmd}font` `<nama font>` `<teks/balas ke pesan>`\
        \n  »  **Kegunaan : **Membuat Text dengan Fonts Style.\
        \n\n  »  **Perintah :** `{cmd}lf`\
        \n  »  **Kegunaan : **Untuk Melihat Daftar Font.\
    "
    }
)
