# Ported by X_ImFine
# Recode by @mrismanaziz

from telethon.tl.functions.contacts import BlockRequest, UnblockRequest

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, DEVS
from AyiinXd.events import register
from AyiinXd.ayiin import get_user_from_event, ayiin_cmd
from Stringyins import get_string


@ayiin_cmd(pattern="gkick(?: |$)(.*)")
@register(pattern=r"^\.cgkick(?: |$)(.*)", sudo=True)
async def gspide(rk):
    lazy = rk
    sender = await lazy.get_sender()
    me = await lazy.client.get_me()
    if sender.id != me.id:
        rkp = await lazy.reply(get_string("com_1"))
    else:
        rkp = await lazy.edit(get_string("com_1"))
    me = await rk.client.get_me()
    await rkp.edit(get_string("gkick_1"))
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    await rk.get_chat()
    a = b = 0
    if rk.is_private:
        user = rk.chat
        reason = rk.pattern_match.group(1)
    try:
        user, reason = await get_user_from_event(rk)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await rkp.edit(get_string("gkick_2"))
    if user:
        if user.id == DEVS:
            return await rkp.edit(get_string("gkick_5"))
        try:
            await rk.client(BlockRequest(user))
            await rk.client(UnblockRequest(user))
        except BaseException:
            pass
        testrk = [
            d.entity.id
            for d in await rk.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testrk:
            try:
                await rk.client.edit_permissions(i, user, view_messages=False)
                await rk.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await rkp.edit(get_string("gkick_3").format(a)
                )

            except BaseException:
                b += 1
    else:
        await rkp.edit(get_string("gban_8"))

    return await rkp.edit(get_string("gkick_4").format(user.first_name, user.id, a)
    )


CMD_HELP.update(
    {
        "gkick": f"**Plugin : **`gkick`\
        \n\n  »  **Perintah :** `{cmd}gkick` <alasan>\
        \n  »  **Kegunaan : **kick pengguna secara global dari semua Administrasi Grup di mana Anda berada.\
    "
    }
)
