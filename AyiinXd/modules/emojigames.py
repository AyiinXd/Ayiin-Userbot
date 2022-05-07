# fix by @heyworld for OUB
# bug fixed by @d3athwarrior
# Recode by @mrismanaziz
# t.me/SharingUserbot

from telethon.tl.types import InputMediaDice

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd


@ayiin_cmd(pattern="dice(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.delete()
    r = await event.reply(file=InputMediaDice(""))
    if input_str:
        try:
            required_number = int(input_str)
            while r.media.value != required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice(""))
        except BaseException:
            pass


@ayiin_cmd(pattern="dart(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.delete()
    r = await event.reply(file=InputMediaDice("🎯"))
    if input_str:
        try:
            required_number = int(input_str)
            while r.media.value != required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice("🎯"))
        except BaseException:
            pass


@ayiin_cmd(pattern="basket(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.delete()
    r = await event.reply(file=InputMediaDice("🏀"))
    if input_str:
        try:
            required_number = int(input_str)
            while r.media.value != required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice("🏀"))
        except BaseException:
            pass


@ayiin_cmd(pattern="bowling(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.delete()
    r = await event.reply(file=InputMediaDice("🎳"))
    if input_str:
        try:
            required_number = int(input_str)
            while r.media.value != required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice("🎳"))
        except BaseException:
            pass


@ayiin_cmd(pattern="ball(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.delete()
    r = await event.reply(file=InputMediaDice("⚽"))
    if input_str:
        try:
            required_number = int(input_str)
            while r.media.value != required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice("⚽"))
        except BaseException:
            pass


@ayiin_cmd(pattern="jackpot(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.delete()
    r = await event.reply(file=InputMediaDice("🎰"))
    if input_str:
        try:
            required_number = int(input_str)
            while r.media.value != required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice("🎰"))
        except BaseException:
            pass


CMD_HELP.update(
    {
        "emojigames": f"**Plugin : **`emojigames`\
        \n\n  »  **Perintah :** `{cmd}dice` 1-6\
        \n  »  **Kegunaan : **Memainkan emoji game dice dengan score yg di tentukan kita.\
        \n\n  »  **Perintah :** `{cmd}dart` 1-6\
        \n  »  **Kegunaan : **Memainkan emoji game dart dengan score yg di tentukan kita.\
        \n\n  »  **Perintah :** `{cmd}basket` 1-5\
        \n  »  **Kegunaan : **Memainkan emoji game basket dengan score yg di tentukan kita.\
        \n\n  »  **Perintah :** `{cmd}bowling` 1-6\
        \n  »  **Kegunaan : **Memainkan emoji game bowling dengan score yg di tentukan kita.\
        \n\n  »  **Perintah :** `{cmd}ball` 1-5\
        \n  »  **Kegunaan : **Memainkan emoji game ball telegram score yg di tentukan kita.\
        \n\n  »  **Perintah :** `{cmd}jackpot` 1\
        \n  »  **Kegunaan : **Memainkan emoji game jackpot dengan score yg di tentukan kita.\
        \n\n  •  **NOTE: **Jangan gunakan nilai lebih atau bot akan Crash**\
    "
    }
)
