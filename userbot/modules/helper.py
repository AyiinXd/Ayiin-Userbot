""" Userbot module for other small commands. """
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, ayiin_cmd


@ayiin_cmd(pattern="ihelp$")
async def usit(event):
    me = await event.client.get_me()
    await edit_or_reply(
        event,
        f"**Hai {me.first_name} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `{cmd}help` Atau Bisa Minta Bantuan Ke:\n"
        f"⍟ **Group Support :** [𝙰𝚈𝙸𝙸𝙽 𝚂𝚄𝙿𝙿𝙾𝚁𝚃](t.me/AyiinXdSupport)\n"
        f"⍟ **Channel Ayiin :** [𝙰𝚈𝙸𝙸𝙽 𝚂𝚄𝙿𝙿𝙾𝚁𝚃](t.me/AyiinSupport)\n"
        f"⍟ **Owner Repo :** [𝚈𝙸𝙽𝚂](t.me/AyiinXd)\n"
        f"⍟ **Repo :** [𝙰𝚈𝙸𝙸𝙽-𝚄𝚂𝙴𝚁𝙱𝙾𝚃](https://github.com/AyiinXd/Ayiin-Userbot)\n",
    )


@ayiin_cmd(pattern="listvar$")
async def var(event):
    await edit_or_reply(
        event,
        "**Daftar Lengkap Vars Dari Ayiin-Userbot:** [KLIK DISINI](https://telegra.ph/List-Variable-Heroku-Untuk-Ayiin-Userbot-02-08)",
    )


CMD_HELP.update(
    {
        "helper": f"**Plugin : **`helper`\
        \n\n  •  **Syntax :** `{cmd}ihelp`\
        \n  •  **Function : **Bantuan Untuk Ayiin-Userbot.\
        \n\n  •  **Syntax :** `{cmd}listvar`\
        \n  •  **Function : **Melihat Daftar Vars.\
        \n\n  •  **Syntax :** `{cmd}repo`\
        \n  •  **Function : **Melihat Repository Ayiin-Userbot.\
        \n\n  •  **Syntax :** `{cmd}string`\
        \n  •  **Function : **Link untuk mengambil String Ayiin-Userbot.\
    "
    }
)
