""" Userbot module for other small commands. """
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, owner
from userbot.utils import edit_or_reply, man_cmd


@man_cmd(pattern="ihelp$")
async def usit(event):
    await edit_or_reply(
        event,
        f"**Hai {owner} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        f"✣ **Group Support :** [𝗔𝘆𝗶𝗶𝗻 𝗨𝘀𝗲𝗿𝗯𝗼𝘁](t.me/AyiinXdSupport)\n"
        f"✣ **Channel Ayiin :** [𝗔𝘆𝗶𝗶𝗻𝗦𝘂𝗽𝗽𝗼𝗿𝘁](t.me/AyiinSupport)\n"
        f"✣ **Owner Repo :** [ʏɪɴs](t.me/AyiinXd)\n"
        f"✣ **Repo :** [𝗔𝘆𝗶𝗶𝗻-𝗨𝘀𝗲𝗿𝗯𝗼𝘁](https://github.com/AyiinXd/Ayiin-Userbot)\n",
    )


@man_cmd(pattern="listvar$")
async def var(event):
    await edit_or_reply(
        event,
        "**Daftar Lengkap Vars Dari Ayiin-Userbot:** [KLIK DISINI](https://telegra.ph/List-Variabel-Heroku-untuk-Man-Userbot-09-22)",
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
