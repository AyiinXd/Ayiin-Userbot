from time import sleep

from userbot import BLACKLIST_CHAT
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, bot
from userbot.events import ayiin_cmd



@bot.on(ayiin_cmd(outgoing=True, pattern=r"ngentot(?: |$)(.*)"))
async def _(event):
    await event.edit("**WOYY NGENTOD!!**")
    sleep(1)
    await event.edit("**JANGAN SOK JAGOAN DAH LU**")
    sleep(1)
    await event.edit("**MUKA MASIH KAYA KONTOL AJA**")
    sleep(1)
    await event.edit("**BANGGA LU HAHAHAHA**")
    sleep(1)
    await event.edit("**COBA DEH NGACA MUKA LU KAN HINA BANGET**")
    sleep(1)
    await event.edit("**HAHAHAHA**")
    sleep(1)
    await event.edit("**MAKANYA GANTENG KONTOL**")
    sleep(1)
    await event.edit("**BIAR MUKALU GAK DIHINA TERUS**")
    sleep(1)
    await event.edit("**SAMA ORANG LAIN**")
    sleep(1)
    await event.edit("**HAHAHAHA**")
# Create by myself @localheart


@bot.on(ayiin_cmd(outgoing=True, pattern=r"goblok(?: |$)(.*)"))
async def _(event):
    await event.edit("**WOYY GOBLOK!!**")
    sleep(1)
    await event.edit("**KO LU GOBLOK BANGET SIH**")
    sleep(1)
    await event.edit("**OTAK LU TUH KAYA KONTOL**")
    sleep(1)
    await event.edit("**YANG LEMBEK KETIKA LEMAH**")
    sleep(1)
    await event.edit("**DAN KERAS KETIKA LU SANGE GOBLOK**")
    sleep(1)
    await event.edit("**HAHAHAHA**")
    sleep(1)
    await event.edit("**MAKANYA JANGAN SANGEAN MULU**")
    sleep(1)
    await event.edit("**MUKA LU AJA KAYA ASPAL JALANAN**")
    sleep(1)
    await event.edit("**EHHH SANGE NYA MAU DAPAT YANG CANTIK**")
    sleep(1)
    await event.edit("**HAHAHAHA**")
# Create by myself @localheart


@bot.on(ayiin_cmd(outgoing=True, pattern=r"ngatain(?: |$)(.*)"))
async def _(event):
    await event.edit("**BABI!!**")
    sleep(1)
    await event.edit("**MUKA LU KAYA BABI**")
    sleep(1)
    await event.edit("**OTAK LU TUH KAYA KONTOL**")
    sleep(1)
    await event.edit("**MUKA LU HINA BANGET**")
    sleep(1)
    await event.edit("**OTAK LU KAYA BATU**")
    sleep(1)
    await event.edit("**HAHAHAHA**")
    sleep(1)
    await event.edit("**MAKANYA JANGAN SANGEAN MULU**")
    sleep(1)
    await event.edit("**KONTOL LU AJA MASIH BENGKOK**")
    sleep(1)
    await event.edit("**EHHH SANGE NYA MAU DAPAT YANG CANTIK**")
    sleep(1)
    await event.edit("**HAHAHAHA**")
# Create by myself @localheart


@bot.on(ayiin_cmd(outgoing=True, pattern=r"yatim(?: |$)(.*)"))
async def _(event):
    await event.edit("`Hai Anak Kontol 🙈, Jangan Lupa Makan Yaa`")
    sleep(1)
    await event.edit("`Jangan Bilang Lu Ga Dikasih Makan Sama Ortu 😁`")
    sleep(1)
    await event.edit("`APA PERLU GUA SANTUNIN ?? 🙈🙈 xixixi`")
    sleep(1)
    await event.edit("`OH IYAA LUPAAA, LU KAN BEBAN KELUARGA 🤣`")
    sleep(1)
    await event.edit("`MANA MUNGKIN ORTU LU PEDULII xixixi 🙈`")
    sleep(1)
    await event.edit("`KETAWA DULU BOLEH KALI YAA 😁`")
    sleep(1)
    await event.edit("`HAHAHAHAHAHAHA`")
    sleep(1)
    await event.edit("`KASIAN ORTUNYAA GAPEDULIII 🙈🤣`")
    sleep(1)
    await event.edit("`MAAF YA, CANDAA BEBANNNN xixixi 🙈`")
    sleep(1)
    await event.edit("`Tapi Bo'ong Hiyahiyahiya`")
# Create by myself @localheart


@bot.on(ayiin_cmd(outgoing=True, pattern=r"kont(?: |$)(.*)"))
async def _(event):
    await event.edit("**KONTOLL**")
    sleep(1.5)
    await event.edit("**LU ANAK KONTOLL**")
    sleep(1.5)
    await event.edit("**DI BIKIN DARI KONTOLL**")
    sleep(1.5)
    await event.edit("**MUKALU PERSIS KONTOLL**")
    sleep(1.5)
    await event.edit("**DASAR ANAK NGONTOLLLL**")
    sleep(1.5)
    await event.edit("**NOLEP KONTOLL**")
    sleep(1.5)
    await event.edit("**NGERUSUH KONTOLL**")
    sleep(1.5)
    await event.edit("**BENER BENER KONTOLL**")
    sleep(1.5)
    await event.edit("**PADAHAL LO GAPUNYA KONTOLL**")
    sleep(1.5)
    await event.edit("**MENDING LO OPERASI KONTOLL**")
    sleep(1.5)
    await event.edit("**BIAR LO PUNYA KONTOLL**")
    sleep(1.5)
    await event.edit("**KASIAN CACAD GAPUNYA KONTOLL**")

CMD_HELP.update(
    {
        "yinstoxic2": f"**Plugin : **`yinstoxic2`\
        \n\n  •  **Syntax :** `{cmd}ngentot`\
        \n  •  **Function : **Cobain sendiri tod\
        \n\n  •  **Syntax :** `{cmd}goblok`\
        \n  •  **Function : **Cobaij sendiri tod\
        \n\n  •  **Syntax :** `{cmd}ngatain`\
        \n  •  **Function : **Cobain sendiri tod\
        \n\n  •  **Syntax :** `{cmd}kont`\
        \n  •  **Function : **Cobain sendiri tod\
        \n\n  •  **Syntax :** `{cmd}yatim`\
        \n  •  **Function : **Cobain sendiri tod\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
) 

