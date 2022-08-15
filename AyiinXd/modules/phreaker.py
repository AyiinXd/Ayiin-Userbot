from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import edit_or_reply, ayiin_cmd


@ayiin_cmd(pattern="nmap(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@scriptkiddies_bot"
    nmap = "nmap"
    xx = await edit_or_reply(event, "Processing....")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=510263282)
            )
            await conv.send_message(f"/{nmap} {link}")
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message(f"/{nmap} {link}")
            response = await response
        else:
            await xx.edit(f"{response.message.message}")
            await event.client.delete_messages(response.message.message)


@ayiin_cmd(pattern="subd(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    subdomain = "subdomain"
    chat = "@scriptkiddies_bot"
    xx = await edit_or_reply(event, "Processing....")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=510263282)
            )
            await conv.send_message(f"/{subdomain} {link}")
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message(f"/{subdomain} {link}")
            response = await response
        else:
            await xx.edit(f"{response.message.message}")
            await event.client.delete_messages(response.message.message)


@ayiin_cmd(pattern="cek(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@scriptkiddies_bot"
    httpheader = "httpheader"
    xx = await edit_or_reply(event, "Processing....")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=510263282)
            )
            await conv.send_message(f"/{httpheader} {link}")
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message(f"/{httpheader} {link}")
            response = await response
        else:
            await xx.edit(f"{response.message.message}")
            await event.client.delete_messages(httpheader, response.message.message)


@ayiin_cmd(pattern="bin(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    xx = await edit_or_reply(event, "Processing....")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await conv.send_message(f"/{bin} {link}")
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message(f"/{bin} {link}")
            response = await response
        else:
            await xx.edit(f"{response.message.message}")
            await event.client.delete_messages(response.message.message)


@ayiin_cmd(pattern="cc(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    ss = "ss"
    xx = await edit_or_reply(event, "Processing....")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await conv.send_message(f"/{ss} {link}")
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message(f"/{ss} {link}")
            response = await response
        else:
            await xx.edit(f"{response.message.message}")
            await event.client.delete_messages(response.message.message)


CMD_HELP.update(
    {
        "phreaker": f"**Plugin : **`phreaker`\
        \n\n  »  **Perintah :** `{cmd}nmap` <bug hosts>\
        \n  »  **Kegunaan : **Untuk mendapatkan info bug / host.\
        \n\n  »  **Perintah :** `{cmd}subd` <bug hosts>\
        \n  »  **Kegunaan : **Untuk mendapatkan bug / host subdomain.\
        \n\n  »  **Perintah :** `{cmd}cek <bug hosts>\
        \n  »  **Kegunaan : **Untuk cek respons bug / host.\
        \n\n  »  **Perintah :** `{cmd}bin <bin number>\
        \n  »  **Kegunaan : **untuk cek bin ip.\
        \n\n  »  **Perintah :** `{cmd}cc <mm|yy|cvv>\
        \n  »  **Kegunaan : **untuk cek Statistik Kartu Kredit.\
    "
    }
)
