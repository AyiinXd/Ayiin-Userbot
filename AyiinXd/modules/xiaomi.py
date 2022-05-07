# created by @eve_enryu

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eor
from Stringyins import get_string


@ayiin_cmd(pattern="firmware(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    firmware = "firmware"
    chat = "@XiaomiGeeksBot"
    await eor(event, get_string("com_1"))
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{firmware} {link}")
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message(f"/{firmware} {link}")
            response = await response
        else:
            await event.delete()
            await event.client.forward_messages(event.chat_id, response.message)


@ayiin_cmd(pattern="fastboot(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    fboot = "fastboot"
    chat = "@XiaomiGeeksBot"
    await eor(event, get_string("com_1"))
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{fboot} {link}")
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message(f"/{fboot} {link}")
            response = await response
        else:
            await event.delete()
            await event.client.forward_messages(event.chat_id, response.message)


@ayiin_cmd(pattern="recovery(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    recovery = "recovery"
    chat = "@XiaomiGeeksBot"
    await eor(event, get_string("com_1"))
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{recovery} {link}")
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message(f"/{recovery} {link}")
            response = await response
        else:
            await event.delete()
            await event.client.forward_messages(event.chat_id, response.message)


@ayiin_cmd(pattern="pb(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    pitch = "pb"
    chat = "@XiaomiGeeksBot"
    await eor(event, get_string("com_1"))
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{pitch} {link}")
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message(f"/{pitch} {link}")
            response = await response
        else:
            await event.delete()
            await event.client.forward_messages(event.chat_id, response.message)


@ayiin_cmd(pattern="of(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    ofox = "of"
    chat = "@XiaomiGeeksBot"
    await eor(event, get_string("com_1"))
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{ofox} {link}")
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message(f"/{ofox} {link}")
            response = await response
        else:
            await event.delete()
            await event.client.forward_messages(event.chat_id, response.message)


@ayiin_cmd(pattern="eu(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    eu = "eu"
    chat = "@XiaomiGeeksBot"
    await eor(event, get_string("com_1"))
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{eu} {link}")
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message(f"/{eu} {link}")
            response = await response
        else:
            await event.delete()
            await event.client.forward_messages(event.chat_id, response.message)


@ayiin_cmd(pattern="vendor(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    vendor = "vendor"
    chat = "@XiaomiGeeksBot"
    await eor(event, get_string("com_1"))
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{vendor} {link}")
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message(f"/{vendor} {link}")
            response = await response
        else:
            await event.delete()
            await event.client.forward_messages(event.chat_id, response.message)


@ayiin_cmd(pattern="specs(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    specs = "specs"
    chat = "@XiaomiGeeksBot"
    await eor(event, get_string("com_1"))
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{specs} {link}")
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message(f"/{specs} {link}")
            response = await response
        else:
            await event.delete()
            await event.client.forward_messages(event.chat_id, response.message)


CMD_HELP.update(
    {
        "xiaomi": f"**Plugin : **`xiaomi`\
        \n\n  »  **Perintah :** `{cmd}firmware` (codename)\
        \n  »  **Kegunaan : **Get lastest Firmware.\
        \n\n  »  **Perintah :** `{cmd}pb` (codename)\
        \n  »  **Kegunaan : **Get latest PitchBlack Recovery.\
        \n\n  »  **Perintah :** `{cmd}specs` (codename)\
        \n  »  **Kegunaan : **Get quick spec information about device.\
        \n\n  »  **Perintah :** `{cmd}fastboot` (codename)\
        \n  »  **Kegunaan : **Get latest fastboot MIUI.\
        \n\n  »  **Perintah :** `{cmd}recovery` (codename)\
        \n  »  **Kegunaan : **Get latest recovery MIUI.\
        \n\n  »  **Perintah :** `{cmd}eu` (codename)\
        \n  »  **Kegunaan : **Get latest xiaomi.eu rom.\
        \n\n  »  **Perintah :** `{cmd}vendor` (codename)\
        \n  »  **Kegunaan : **fetches latest vendor.\
        \n\n  »  **Perintah :** `{cmd}of` (codename)\
        \n  »  **Kegunaan : **Get latest ORangeFox Recovery.\
    "
    }
)
