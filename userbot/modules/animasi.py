# greyvbss
# cilik-userbot


from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, bot
from userbot.events import ayiin_cmd


@bot.on(ayiin_cmd(outgoing=True, pattern=r"skull(?: |$)(.*)"))
async def _(event):
    await event.edit(
        "███████████████████████████\n"
        "███████▀▀▀░░░░░░░▀▀▀███████\n"
        "████▀░░░░░░░░░░░░░░░░░▀████\n"
        "███│░░░░░░░░░░░░░░░░░░░│███\n"
        "██▌│░░░░░░░░░░░░░░░░░░░│▐██\n"
        "██░└┐░░░░░░░░░░░░░░░░░┌┘░██\n"
        "██░░└┐░░░░░░░░░░░░░░░┌┘░░██\n"
        "██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██\n"
        "██▌░│██████▌░░░▐██████│░▐██\n"
        "███░│▐███▀▀░░▄░░▀▀███▌│░███\n"
        "██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██\n"
        "██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██\n"
        "████▄─┘██▌░░░░░░░▐██└─▄████\n"
        "█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████\n"
        "████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████\n"
        "█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████\n"
        "███████▄░░░░░░░░░░░▄███████\n"
        "██████████▄▄▄▄▄▄▄██████████\n"
        "███████████████████████████\n"
    )


bot.on(ayiin_cmd(outgoing=True, pattern=r"wlc(?: |$)(.*)"))


async def _(event):
    await event.edit(
        "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
        "█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n"
        "█░░║║║╠─║─║─║║║║║╠─░░█\n"
        "█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n"
        "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n"
    )


@bot.on(ayiin_cmd(outgoing=True, pattern=r"klb(?: |$)(.*)"))
async def _(event):
    await event.edit(
        "   ╚⊙ ⊙╝..\n"
        "   ╚═(███)═╝\n"
        "    ╚═(███)═╝\n"
        "       ╚═(███)═╝\n"
        "        ╚═(███)═╝\n"
        "        ╚═(███)═╝\n"
        "        ╚═(███)═╝\n"
        "      ╚═(███)═╝\n"
        "     ╚═(███)═╝\n"
        "    ╚═(███)═╝ \n"
        "    ╚═(███)═╝\n"
        "     ╚═(███)═╝\n"
        "      ╚═(███)═╝\n"
        "       ╚═(███)═╝\n"
        "        ╚═(███)═╝\n"
        "        ╚═(███)═╝\n"
        "       ╚═(███)═╝\n"
        "      ╚═(███)═╝\n"
        "     ╚═(███)═╝\n"
        "     ╚═(███)═╝\n"
        "      ╚═(█)═╝\n"
    )


bot.on(ayiin_cmd(outgoing=True, pattern=r"fucek(?: |$)(.*)"))


async def _(event):
    await event.edit(
        "░░░░░░░░░░░░░░░▄▄░░░░░░░░░░░\n"
        "░░░░░░░░░░░░░░█░░█░░░░░░░░░░\n"
        "░░░░░░░░░░░░░░█░░█░░░░░░░░░░\n"
        "░░░░░░░░░░░░░░█░░█░░░░░░░░░░\n"
        "░░░░░░░░░░░░░░█░░█░░░░░░░░░░\n"
        "██████▄███▄████░░███▄░░░░░░░\n"
        "▓▓▓▓▓▓█░░░█░░░█░░█░░░███░░░░\n"
        "▓▓▓▓▓▓█░░░█░░░█░░█░░░█░░█░░░\n"
        "▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░█░░░\n"
        "▓▓▓▓▓▓█░░░░░░░░░░░░░░░░█░░░░\n"
        "▓▓▓▓▓▓█░░░░░░░░░░░░░░██░░░░░\n"
        "▓▓▓▓▓▓█████░░░░░░░░░██░░░░░░\n"
    )


CMD_HELP.update(
    {
        "animasi": f"**Plugin : **`animasi`\
        \n\n  •  **Syntax :** `{cmd}skull`\
        \n  •  **Function : **Cobain sendiri tod\
        \n\n  •  **Syntax :** `{cmd}wlc`\
        \n  •  **Function : **Cobain sendiri tod\
        \n\n  •  **Syntax :** `{cmd}klb`\
        \n  •  **Function : **Cobain sendiri tod\
        \n\n  •  **Syntax :** `{cmd}fucek`\
        \n  •  **Function : **Cobain sendiri tod\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
)
