# © Copyright 2022 Ayiin-Userbot LLC Company.
# GPL-3.0 License From Github
# WARNING !!
# Credits by @AyiinXd

from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^$yins(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`𝙃𝙖𝙞 𝙋𝙚𝙧𝙠𝙚𝙣𝙖𝙡𝙠𝙖𝙣 𝙉𝙖𝙢𝙖 𝙂𝙪𝙖 𝘼𝙮𝙞𝙞𝙣`")
    sleep(3)
    await typew.edit("`23 𝙏𝙖𝙝𝙪𝙣`")
    sleep(2)
    await typew.edit("`𝙏𝙞𝙣𝙜𝙜𝙖𝙡 𝘿𝙞 𝘽𝙖𝙡𝙞...'")
    sleep(3)
    await typew.edit("'𝙊𝙬𝙣𝙚𝙧 𝘿𝙖𝙧𝙞 𝘼𝙮𝙞𝙞𝙣 𝙐𝙨𝙚𝙧𝙗𝙤𝙩, 𝙎𝙖𝙡𝙖𝙢 𝙆𝙚𝙣𝙖𝙡 😁`")
    sleep(3)
    await typew.edit("'𝘿𝙖𝙣 𝙎𝙖𝙩𝙪 𝙇𝙖𝙜𝙞....'")
    sleep(3)
    await typew.edit("'𝙂𝙪𝙖 𝙂𝙖𝙣𝙩𝙚𝙣𝙜 𝙏𝙤𝙙 🗿'")
# Create by myself @Contoldisini


@register(outgoing=True, pattern='^$sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`𝘼𝙠𝙪 𝘾𝙪𝙢𝙖 𝙈𝙖𝙪 𝘽𝙞𝙡𝙖𝙣𝙜 👉👈`")
    sleep(3)
    await typew.edit("`𝘼𝙠𝙪 𝙎𝙖𝙮𝙖𝙣𝙜 𝙆𝙖𝙢𝙪 😘`")
    sleep(1)
    await typew.edit("`𝙈𝙪𝙖𝙖𝙘𝙘𝙝𝙝𝙝 😘💕`")
# Create by myself @Contoldisini


@register(outgoing=True, pattern='^$semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`𝘼𝙥𝙖𝙥𝙪𝙣 𝙔𝙖𝙣𝙜 𝙏𝙚𝙧𝙟𝙖𝙙𝙞`")
    sleep(3)
    await typew.edit("`𝙏𝙚𝙩𝙖𝙥𝙡𝙖𝙝 𝘽𝙚𝙧𝙣𝙖𝙥𝙖𝙨`")
    sleep(1)
    await typew.edit("`𝘿𝙖𝙣 𝙎𝙚𝙡𝙖𝙡𝙪 𝘽𝙚𝙧𝙨𝙮𝙪𝙠𝙪𝙧`")
# Create by myself @Contoldisini

@register(outgoing=True, pattern='^$mengeluh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`𝘼𝙥𝙖𝙥𝙪𝙣 𝙔𝙖𝙣𝙜 𝙏𝙚𝙧𝙟𝙖𝙙𝙞`")
    sleep(3)
    await typew.edit("`𝙏𝙚𝙩𝙖𝙥𝙡𝙖𝙝 𝙈𝙚𝙣𝙜𝙚𝙡𝙪𝙝`")
    sleep(1)
    await typew.edit("`𝘿𝙖𝙣 𝙎𝙚𝙡𝙖𝙡𝙪 𝙋𝙪𝙩𝙪𝙨 𝘼𝙨𝙖`")
# Create by myself @Contoldisini


CMD_HELP.update({
    "yinsubot3": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `$yins`\
    \n↳ : perkenalan yins\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `$sayang`\
    \n↳ : Gombalan maut`\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `$semangat`\
    \n↳ : Jan Lupa Semangat`\
n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `$mengeluh`\
    \n↳ : Jan Lupa Mengeluh."
})
