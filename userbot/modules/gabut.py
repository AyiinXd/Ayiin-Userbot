from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.tmo(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`𝙏𝙈𝙊 𝙈𝙪𝙡𝙪 𝙇𝙪`")
    sleep(2)
    await typew.edit("`𝙅𝙖𝙙𝙞𝙖𝙣 𝙅𝙪𝙜𝙖 𝙆𝙖𝙜𝙖𝙠`")
    sleep(1)
    await typew.edit("`𝙏𝙖𝙥𝙞 𝙆𝙖𝙡𝙤 𝙇𝙪 𝙅𝙖𝙙𝙞𝙖𝙣, 𝙐𝙟𝙪𝙣𝙜-𝙐𝙟𝙪𝙣𝙜𝙣𝙮𝙖 𝙅𝙪𝙜𝙖 𝙆𝙚𝙣𝙖 𝙂𝙝𝙤𝙨𝙩𝙞𝙣𝙜`")


@register(outgoing=True, pattern='^.give(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`𝙎𝙮𝙖𝙧𝙖𝙩 𝙄𝙠𝙪𝙩 𝙂𝙞𝙥𝙚𝙚𝙬𝙚𝙮`")
    sleep(2)
    await typew.edit("`𝙂𝙘𝙖𝙨𝙩 𝙈𝙞𝙣𝙞𝙢𝙖𝙡 10 𝙂𝙧𝙪𝙥`")
    sleep(1)
    await typew.edit("`𝙉𝙖𝙞𝙠 𝙊𝙨, 𝘿𝙖𝙣 𝙎𝙨 𝘽𝙪𝙠𝙩𝙞 𝙂𝙘𝙖𝙨𝙩`")


@register(outgoing=True, pattern='^.uno(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`𝙆𝙖𝙠𝙠𝙠 👉👈`")
    sleep(2)
    await typew.edit("`𝘽𝙚𝙬𝙖𝙣 𝙐𝙣𝙤 𝙮𝙪𝙠 🙈`")
    sleep(1)
    await typew.edit("`𝙔𝙖𝙣𝙜 𝙆𝙖𝙡𝙖𝙝 𝙋𝙞𝙣𝙙𝙖𝙝 𝘼𝙜𝙖𝙢𝙖 🙊`")


CMD_HELP.update({
    "gabut3": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tmo`\
    \n↳ : Cobain Sendiri\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.give`\
    \n↳ : Cobain Sendiri`\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.uno`\
    \n↳ : Cobain Sendiri."
})
