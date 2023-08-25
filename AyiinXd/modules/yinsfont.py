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

from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, edit_delete, edit_or_reply

from . import cmd

_default = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
_smallcap = "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘϙʀsᴛᴜᴠᴡxʏᴢABCDEFGHIJKLMNOPQRSTUVWXYZ"
_monospace = "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉"
_outline = "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ"
_script = "𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵"
_blackbubbles = "🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩"
_bubbles = "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ"
_bold = "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭"
_bolditalic = "𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕"


def gen_font(text, new_font):
    new_font = " ".join(new_font).split()
    for q in text:
        if q in _default:
            new = new_font[_default.index(q)]
            text = text.replace(q, new)
    return text


@ayiin_cmd(pattern="font (.*)(|$)")
async def _(ayiin):
    font = ayiin.pattern_match.group(1)
    reply = await ayiin.get_reply_message()
    yins = None
    if not font:
        return await edit_delete(ayiin, f"<b>Silahkan berikan saya nama font...</b>\n\n<b>Gunakan <code>.lf</code> Untuk melihat daftar font</b>", time=5)
    if font == "smallcap":
        yins = gen_font(reply.message, _smallcap)
    elif font == "monospace":
        yins = gen_font(reply.message, _monospace)
    elif font == "outline":
        yins = gen_font(reply.message, _outline)
    elif font == "script":
        yins = gen_font(reply.message, _script)
    elif font == "blackbubbles":
        yins = gen_font(reply.message, _blackbubbles)
    elif font == "bubbles":
        yins = gen_font(reply.message, _bubbles)
    elif font == "bold":
        yins = gen_font(reply.message, _bold)
    elif font == "bolditalic":
        yins = gen_font(reply.message, _bolditalic)
    if yins is not None:
        await edit_or_reply(ayiin, yins)


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


@ayiin_cmd(pattern="lf(.*)(|$)")
async def fonts(yins):
    await edit_or_reply(
        yins,
        """
**»» ᴅᴀғᴛᴀʀ ғᴏɴᴛs ««**

**• smallcap » ᴀʏɪɪɴ**
**• monospace » 𝙰𝚈𝙸𝙸𝙽**
**• outline » 𝔸𝕐𝕀𝕀ℕ**
**• script » 𝒜𝒴ℐℐ𝒩**
**• blackbubbles » 🅐︎🅨︎🅘︎🅘︎🅝︎**
**• bubbles » Ⓐ︎Ⓨ︎Ⓘ︎Ⓘ︎Ⓝ︎**
**• bold » 𝗔𝗬𝗜𝗜𝗡**
**• bolditalic » 𝘼𝙔𝙄𝙄𝙉**

**   ✧ ᴀʏɪɪɴ-ᴜsᴇʀʙᴏᴛ ✧**"""
    )


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
