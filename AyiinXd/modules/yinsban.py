# Port By @VckyouuBitch From GeezProject
# Perkontolan Dengan Hapus Credits
# Recode By : @AyiinXd

from asyncio import sleep
from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelParticipantsKicked
from AyiinXd import CMD_HELP
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd.utils import edit_or_reply, ayiin_cmd


@ayiin_cmd(pattern="banall(?: |$)(.*)")
async def testing(ayiinxd):
    ayiin = await ayiinxd.get_chat()
    yins = await ayiinxd.client.get_me()
    admin = ayiin.admin_rights
    creator = ayiin.creator
    if not admin and not creator:
        await edit_delete(ayiinxd, "Lu Gak Punya Hak Untuk Melakukan Ini Bego!!!")
        return
    await edit_or_reply(ayiinxd, "Tidak Melakukan Apa-apa")
# Thank for Dark_Cobra
    ayiinkontol = await ayiinxd.client.get_participants(ayiinxd.chat_id)
    for user in ayiinkontol:
        if user.id == yins.id:
            pass
        try:
            xx = await ayiinxd.client(EditBannedRequest(ayiinxd.chat_id, int(user.id), ChatBannedRights(until_date=None, view_messages=True)))
        except Exception as e:
            await ayiinxd.edit(str(e))
        await sleep(.5)
    await edit_or_reply(ayiinxd, "Tidak Ada yang Terjadi di sini🙃🙂")


@ayiin_cmd(pattern="unbanall(?: |$)(.*)")
async def _(ayiin):
    yins = await edit_or_reply(ayiin, "`Sabar Tod Sedang Mencari Daftar Blokir.`")
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
