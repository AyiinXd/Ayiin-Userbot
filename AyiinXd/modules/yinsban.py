# Port By @VckyouuBitch From GeezProject
# Perkontolan Dengan Hapus Credits
# Recode By : @AyiinXd

from asyncio import sleep

from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelParticipantsKicked

from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eod, eor

from . import cmd

@ayiin_cmd(pattern="banall(?: |$)(.*)")
async def testing(ayiinxd):
    ayiin = await ayiinxd.get_chat()
    yins = await ayiinxd.client.get_me()
    admin = ayiin.admin_rights
    creator = ayiin.creator
    if not admin and not creator:
        await eod(ayiinxd, f"**Maaf {yins.first_name} Bukan Admin 👮**")
        return
    xnxx = await eor(ayiinxd, "Tidak Melakukan Apa-apa")
# Thank for Dark_Cobra
    ayiinkontol = await ayiinxd.client.get_participants(ayiinxd.chat_id)
    for user in ayiinkontol:
        if user.id == yins.id:
            pass
        try:
            xx = await ayiinxd.client(EditBannedRequest(ayiinxd.chat_id, int(user.id), ChatBannedRights(until_date=None, view_messages=True)))
        except Exception as e:
            await eod(xnxx, "**KESALAHAN : **`{}`".format(str(e)))
        await sleep(.5)
    await xnxx.edit("Tidak Ada yang Terjadi di sini🙃🙂")


@ayiin_cmd(pattern="unbanall(?: |$)(.*)")
async def _(ayiin):
    yins = await eor(ayiin, "`Sedang Mencari Daftar Blokir.`")
    p = 0
    (await ayiin.get_chat()).title
    async for i in ayiin.client.iter_participants(
        ayiin.chat_id,
        filter=ChannelParticipantsKicked,
        aggressive=True,
    ):
        try:
            await ayiin.client.edit_permissions(ayiin.chat_id, i, view_messages=True)
            p += 1
        except BaseException:
            pass
    await yins.edit(f"`Sukses Membebaskan {p} Tahanan...`")


CMD_HELP.update(
    {
        "yinsban": f"**Plugin : **`yinsban`\
        \n\n  »  **Perintah :** `{cmd}banall`\
        \n  »  **Kegunaan :** Banned Semua Member Dalam Satu Ketikan.\
        \n\n  »  **Perintah :** `{cmd}unbanall`\
        \n  »  **Kegunaan :** Membatalkan Banned Anggota Group.\
    "
    }
)
