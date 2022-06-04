from time import sleep

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eor
from Stringyins import get_string


@ayiin_cmd(pattern=r"ngentot(?: |$)(.*)")
async def _(ayiin):
    yins = await eor(ayiin, get_string("yitxc_23"))
    sleep(1)
    await yins.edit(get_string("yitxc_24"))
    sleep(1)
    await yins.edit(get_string("yitxc_25"))
    sleep(1)
    await yins.edit(get_string("yitxc_26"))
    sleep(1)
    await yins.edit(get_string("yitxc_27"))
    sleep(1)
    await yins.edit(get_string("yitxc_28"))
    sleep(1)
    await yins.edit(get_string("yitxc_29"))
    sleep(1)
    await yins.edit(get_string("yitxc_30"))
    sleep(1)
    await yins.edit(get_string("yitxc_31"))
    sleep(1)
    await yins.edit(get_string("yitxc_32"))
# Create by myself @localheart


@ayiin_cmd(pattern=r"goblok(?: |$)(.*)")
async def _(gblk):
    ayiin = await eor(gblk, get_string("yitxc_33"))
    sleep(1)
    await ayiin.edit(get_string("yitxc_34"))
    sleep(1)
    await ayiin.edit(get_string("yitxc_35"))
    sleep(1)
    await ayiin.edit(get_string("yitxc_36"))
    sleep(1)
    await ayiin.edit(get_string("yitxc_37"))
    sleep(1)
    await ayiin.edit(get_string("yitxc_38"))
    sleep(1)
    await ayiin.edit(get_string("yitxc_39"))
    sleep(1)
    await ayiin.edit(get_string("yitxc_40"))
    sleep(1)
    await ayiin.edit(get_string("yitxc_41"))
    sleep(1)
    await ayiin.edit(get_string("yitxc_42"))
# Create by myself @localheart


@ayiin_cmd(pattern=r"ngatain(?: |$)(.*)")
async def _(kntl):
    xd = await eor(kntl, get_string("yitxc_43"))
    sleep(1)
    await xd.edit(get_string("yitxc_44"))
    sleep(1)
    await xd.edit(get_string("yitxc_45"))
    sleep(1)
    await xd.edit(get_string("yitxc_46"))
    sleep(1)
    await xd.edit(get_string("yitxc_47"))
    sleep(1)
    await xd.edit(get_string("yitxc_48"))
    sleep(1)
    await xd.edit(get_string("yitxc_49"))
    sleep(1)
    await xd.edit(get_string("yitxc_50"))
    sleep(1)
    await xd.edit(get_string("yitxc_51"))
    sleep(1)
    await xd.edit(get_string("yitxc_52"))
# Create by myself @localheart


@ayiin_cmd(pattern=r"yatim(?: |$)(.*)")
async def _(ytim):
    ayiinxd = await eor(ytim, get_string("yitxc_53"))
    sleep(1)
    await ayiinxd.edit(get_string("yitxc_54"))
    sleep(1)
    await ayiinxd.edit(get_string("yitxc_55"))
    sleep(1)
    await ayiinxd.edit(get_string("yitxc_56"))
    sleep(1)
    await ayiinxd.edit(get_string("yitxc_57"))
    sleep(1)
    await ayiinxd.edit(get_string("yitxc_58"))
    sleep(1)
    await ayiinxd.edit(get_string("yitxc_59"))
    sleep(1)
    await ayiinxd.edit(get_string("yitxc_60"))
    sleep(1)
    await ayiinxd.edit(get_string("yitxc_61"))
    sleep(1)
    await ayiinxd.edit(get_string("yitxc_62"))
# Create by myself @localheart


@ayiin_cmd(pattern=r"kont(?: |$)(.*)")
async def _(kontol):
    yins = await eor(kontol, get_string("yitxc_23"))
    sleep(1.5)
    await yins.edit(get_string("yitxc_63"))
    sleep(1.5)
    await yins.edit(get_string("yitxc_64"))
    sleep(1.5)
    await yins.edit(get_string("yitxc_65"))
    sleep(1.5)
    await yins.edit(get_string("yitxc_66"))
    sleep(1.5)
    await yins.edit(get_string("yitxc_67"))
    sleep(1.5)
    await yins.edit(get_string("yitxc_68"))
    sleep(1.5)
    await yins.edit(get_string("yitxc_69"))
    sleep(1.5)
    await yins.edit(get_string("yitxc_70"))
    sleep(1.5)
    await yins.edit(get_string("yitxc_71"))
    sleep(1.5)
    await yins.edit(get_string("yitxc_72"))
    sleep(1.5)
    await yins.edit(get_string("yitxc_73"))

CMD_HELP.update(
    {
        "yinstoxic2": f"**Plugin : **`yinstoxic2`\
        \n\n  »  **Perintah :** `{cmd}ngentot`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}goblok`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}ngatain`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}kont`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}yatim`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
)
