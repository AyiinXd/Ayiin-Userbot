from time import sleep

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, owner
from userbot.utils import edit_or_reply, ayiin_cmd


@ayiin_cmd(pattern="p(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**𝘼𝙨𝙨𝙖𝙡𝙖𝙢𝙪𝙖𝙡𝙖𝙞𝙠𝙪𝙢 𝘿𝙪𝙡𝙪 𝙏𝙤𝙙 𝘽𝙞𝙖𝙧 𝙎𝙤𝙥𝙖𝙣**")


@ayiin_cmd(pattern="pe(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**𝘼𝙨𝙨𝙖𝙡𝙖𝙢𝙪𝙖𝙡𝙞𝙠𝙪𝙢 𝙒𝙖𝙧𝙖𝙝𝙢𝙖𝙩𝙪𝙡𝙡𝙖𝙝𝙞 𝙒𝙖𝙗𝙖𝙧𝙖𝙠𝙖𝙩𝙪𝙝**")


@ayiin_cmd(pattern="P(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**𝙃𝙖𝙞𝙞 𝙎𝙖𝙡𝙠𝙚𝙣 𝙂𝙪𝙖 {owner}**")
    sleep(2)
    await xx.edit("**𝘼𝙨𝙨𝙖𝙡𝙖𝙢𝙪𝙖𝙡𝙖𝙞𝙠𝙪𝙢...**")


@ayiin_cmd(pattern="l(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**𝙒𝙖'𝙖𝙡𝙖𝙞𝙠𝙪𝙢𝙨𝙖𝙡𝙖𝙢**")


@ayiin_cmd(pattern="a(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**𝙃𝙖𝙞𝙞 𝙎𝙖𝙡𝙠𝙚𝙣 𝙂𝙪𝙖 {owner}**")
    sleep(2)
    await xx.edit("**𝘼𝙨𝙨𝙖𝙡𝙖𝙢𝙪𝙖𝙡𝙖𝙞𝙠𝙪𝙢**")


@ayiin_cmd(pattern="j(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, "**𝙅𝘼𝙆𝘼 𝙎𝙀𝙈𝘽𝙐𝙉𝙂 𝘽𝘼𝙒𝘼 𝙂𝙊𝙇𝙊𝙆**")
    sleep(3)
    await xx.edit("**𝙉𝙄𝙈𝘽𝙍𝙐𝙉𝙂 𝙂𝙊𝘽𝙇𝙊𝙆!!!🔥**")


@ayiin_cmd(pattern="k(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**𝙃𝘼𝙇𝙇𝙊 𝙆𝙊𝙉𝙏𝙊𝙇 𝙂𝙐𝘼 {owner}**")
    sleep(2)
    await xx.edit("**𝙇𝙐 𝙎𝙀𝙈𝙐𝘼 𝙉𝙂𝙀𝙉𝙏𝙊𝘿 🔥**")


@ayiin_cmd(pattern="ass(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, "**𝙎𝙖𝙡𝙖𝙢 𝘿𝙪𝙡𝙪 𝙏𝙤𝙙 𝘽𝙞𝙖𝙧 𝙎𝙤𝙥𝙖𝙣**")
    sleep(2)
    await xx.edit("**السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ**")


CMD_HELP.update(
    {
        "salam": f"**Plugin : **`salam`\
        \n\n  •  **Syntax :** `{cmd}p`\
        \n  •  **Function : **Assalamualaikum Dulu Biar Sopan..\
        \n\n  •  **Syntax :** `{cmd}pe`\
        \n  •  **Function : **salam Kenal dan salam\
        \n\n  •  **Syntax :** `{cmd}l`\
        \n  •  **Function : **Untuk Menjawab salam\
        \n\n  •  **Syntax :** `{cmd}ass`\
        \n  •  **Function : **Salam Bahas arab\
        \n\n  •  **Syntax :** `{cmd}semangat`\
        \n  •  **Function : **Memberikan Semangat.\
        \n\n  •  **Syntax :** `{cmd}ywc`\
        \n  •  **Function : **nMenampilkan Sama sama\
        \n\n  •  **Syntax :** `{cmd}sayang`\
        \n  •  **Function : **Kata I Love You.\
        \n\n  •  **Syntax :** `{cmd}k`\
        \n  •  **Function : **LU SEMUA NGENTOT 🔥\
        \n\n  •  **Syntax :** `{cmd}j`\
        \n  •  **Function : **NIMBRUNG GOBLOKK!!!🔥\
    "
    }
)
