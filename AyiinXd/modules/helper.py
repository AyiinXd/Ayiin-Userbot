""" Userbot module for other small commands. """

from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eor
from AyiinXd.database.variable import cek_var

from . import cmd


@ayiin_cmd(pattern="ihelp$")
async def usit(event):
    me = await event.client.get_me()
    await eor(
        event,
        f"""
**Hai {me.first_name} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `{cmd}help` Atau Bisa Minta Bantuan Ke:
⍟ **Group Support :** [𝙰𝚈𝙸𝙸𝙽 𝚂𝚄𝙿𝙿𝙾𝚁𝚃](t.me/AyiinChats)
⍟ **Channel Ayiin :** [𝙰𝚈𝙸𝙸𝙽 𝚂𝚄𝙿𝙿𝙾𝚁𝚃](t.me/AyiinSupport)
⍟ **Owner Repo :** [𝚈𝙸𝙽𝚂](t.me/AyiinXd)
⍟ **Repo :** [𝙰𝚈𝙸𝙸𝙽-𝚄𝚂𝙴𝚁𝙱𝙾𝚃](https://github.com/AyiinXd/Ayiin-Userbot)
"""
    )


@ayiin_cmd(pattern="listvar$")
async def var(event):
    text = "**Hasil database vars ditemukan.**\n\n**No | Variable | Value**"
    no = 0
    listvar = cek_var()
    if listvar:
        for xd in listvar:
            no += 1
            text += f"\n{no}. {xd[0]} - {xd[1]}"
    else:
        text = "**Anda Belum memiliki database vars.**"
    await eor(
        event,
        text
    )


CMD_HELP.update(
    {
        "helper": f"**Plugin : **`helper`\
        \n\n  »  **Perintah :** `{cmd}ihelp`\
        \n  »  **Kegunaan : **Bantuan Untuk Ayiin-Userbot.\
        \n\n  »  **Perintah :** `{cmd}listvar`\
        \n  »  **Kegunaan : **Melihat Daftar Vars.\
        \n\n  »  **Perintah :** `{cmd}repo`\
        \n  »  **Kegunaan : **Melihat Repository Ayiin-Userbot.\
        \n\n  »  **Perintah :** `{cmd}string`\
        \n  »  **Kegunaan : **Link untuk mengambil String Ayiin-Userbot.\
    "
    }
)
