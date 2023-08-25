# Credits: @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

import os
from pathlib import Path

from AyiinXd import CMD_HELP
from AyiinXd.ayiin import eor
from AyiinXd.ayiin import ayiin_cmd, load_module, remove_plugin, reply_id

from . import cmd


@ayiin_cmd(pattern="install$")
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            xx = await eor(event, "`Memasang Modul...`")
            downloaded_file_name = await event.client.download_media(
                await event.get_reply_message(),
                "AyiinXd/modules/",
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await xx.edit(
                    f"**Plugin** `{os.path.basename(downloaded_file_name)}` **Berhasil di pasang**"
                )
            else:
                os.remove(downloaded_file_name)
                await xx.edit("**Kesalahan!** Plugin ini sudah terpasang di userbot.")
        except Exception as e:
            await xx.edit(f"**KESALAHAN : **`{str(e)}`")
            os.remove(downloaded_file_name)


@ayiin_cmd(pattern="psend ([\\s\\S]*)")
async def send(event):
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(1)
    the_plugin_file = f"./AyiinXd/modules/{input_str}.py"
    if os.path.exists(the_plugin_file):
        caat = await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            force_document=True,
            thumb="AyiinXd/resources/logo.jpg",
            allow_cache=False,
            reply_to=reply_to_id,
            caption=f"**➠ Nama Plugin:** `{input_str}`"
        )
        await event.delete()
    else:
        await eor(event, "**KESALAHAN: Modul Tidak ditemukan**")


@ayiin_cmd(pattern="uninstall (?P<shortname>\\w+)")
async def uninstall(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    dir_path = f"./AyiinXd/modules/{shortname}.py"
    xx = await eor(event, "`Memproses...`")
    try:
        remove_plugin(shortname)
        os.remove(dir_path)
        await xx.edit(f"**Berhasil Menghapus Modul** `{shortname}`")
    except OSError as e:
        await xx.edit("**ERROR:** `%s` : %s" % (dir_path, e.strerror))


CMD_HELP.update(
    {
        "core": f"**Plugin : **`core`\
        \n\n  »  **Perintah :** `{cmd}install` <reply ke file module>\
        \n  »  **Kegunaan : **Untuk Menginstall module userbot secara instan.\
        \n\n  »  **Perintah :** `{cmd}uninstall` <nama module>\
        \n  »  **Kegunaan : **Untuk Menguninstall / Menghapus module userbot secara instan.\
        \n\n  »  **Perintah :** `{cmd}psend` <nama module>\
        \n  »  **Kegunaan : **Untuk Mengirim module userbot secara instan.\
    "
    }
)
