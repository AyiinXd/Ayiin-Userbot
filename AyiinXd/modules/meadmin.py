# COPYRIGHT ULTROID USERBOT
# edit by @JustRex Xa-Userbot
# Jangan hapus Anjg

import asyncio
import os

from AyiinXd import CMD_HELP, Ayiin
from AyiinXd.ayiin import ayiin_cmd, edit_or_reply

from . import cmd


@ayiin_cmd(pattern="meadmin(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    here = event.chat_id
    args = event.pattern_match.group(1)
    xnxx = await edit_or_reply(event, "**Memproses...**")
    admin_list = []
    dialogue = await Ayiin.get_dialogs()
    for dialog in dialogue:
        if dialog.is_group or dialog.is_channel:
            ids = await Ayiin.get_entity(dialog)
            try:
                if ids.admin_rights or ids.creator:
                    info = f"{ids.id}:  {ids.title}"
                    admin_list.append(info)
            except BaseException:
                pass
            except Exception:
                continue

    if len(admin_list) > 0:
        await xnxx.edit('`Berhasil, Sedang Membuat File 🖨️`')
        with open('list_admin.txt', 'w') as book:
            for groups_channels in admin_list:
                book.write(groups_channels + '\n')
        await asyncio.sleep(1)
        caption = f'reply pesan ini dengan ketik {cmd}carbon untuk melihat list Admin anda, [total: {len(admin_list)}]'
        if args and "pv" in args:
            await Ayiin.send_file("me", "list_admin.txt", caption=caption)
            await xnxx.respond("`File terkirim ke Pesan Tersimpan mu`")
        else:
            await Ayiin.send_file(here, "list_admin.txt", caption=caption)
        os.remove("list_admin.txt")
        await xnxx.delete()
    else:
        await xnxx.edit("`Sedih, saya bukan Admin di grup dan channel mana pun 🤧`")


CMD_HELP.update(
    {
        "meadmin": f"**Plugin :** `meadmin`\
        \n\n  »  **Perintah :** `{cmd}meadmin`\
        \n  »  **Kegunaan :** memberikan list group dimana kamu menjadi admin.\
    "
    }
)
