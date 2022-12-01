# by:koala @mixiologist
# Lord Userbot


from AyiinXd import DEVS, WHITELIST, blacklistayiin
from AyiinXd.events import register
from AyiinXd.ayiin import ayiin_cmd, chataction, get_user_from_event
from Stringyins import get_string

# Ported For Lord-Userbot by liualvinas/Alvin


@chataction()
async def handler(tele):
    if not tele.user_joined and not tele.user_added:
        return
    try:
        from AyiinXd.modules.sql_helper.gmute_sql import is_gmuted

        guser = await tele.get_user()
        gmuted = is_gmuted(guser.id)
    except BaseException:
        return
    if gmuted:
        for i in gmuted:
            if i.sender == str(guser.id):
                chat = await tele.get_chat()
                admin = chat.admin_rights
                creator = chat.creator
                if admin or creator:
                    try:
                        await tele.client.edit_permissions(
                            tele.chat_id, guser.id, view_messages=False
                        )
                        await tele.reply(get_string("gban_1").format(guser.id, guser.id)
                        )
                    except BaseException:
                        return


@ayiin_cmd(pattern="gband(?: |$)(.*)")
@register(pattern=r"^\.cgband(?: |$)(.*)", sudo=True)
async def gben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if sender.id != me.id:
        dark = await dc.reply(get_string("gban_2"))
    else:
        dark = await dc.edit(get_string("gban_2"))
    await dark.edit(get_string("gban_3"))
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    try:
        user, reason = await get_user_from_event(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await dark.edit(get_string("gban_4"))
    if user:
        if user.id in DEVS:
            return await dark.edit(get_string("gban_5"))
        if user.id in WHITELIST:
            return await dark.edit(get_string("gban_6")
            )
        try:
            from AyiinXd.modules.sql_helper.gmute_sql import gmute
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await dark.edit(get_string("gban_7").format(user.first_name, user.id, user.id)
                )
            except BaseException:
                b += 1
    else:
        await dark.edit(get_string("gban_8"))
    try:
        if gmute(user.id) is False:
            return await dark.edit(get_string("gban_9")
            )

    except BaseException:
        pass
    return await dark.edit(get_string("gban_10").format(user.first_name, user.id, user.id, me.first_name)
    )


@ayiin_cmd(pattern=r"ungband(?: |$)(.*)")
@register(pattern=r"^\.cungband(?: |$)(.*)", sudo=True)
async def gunben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if sender.id != me.id:
        dark = await dc.reply(get_string("ungban_1"))
    else:
        dark = await dc.edit(get_string("ungban_1"))
    await dark.edit(get_string("ungban_1"))
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    try:
        user, reason = await get_user_from_event(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await dark.edit(get_string("ungban_2"))
    if user:
        if user.id in blacklistayiin:
            return await dark.edit(get_string("ungban_3")
            )
        try:
            from AyiinXd.modules.sql_helper.gmute_sql import ungmute
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await dark.edit(get_string("ungban_1"))
            except BaseException:
                b += 1
    else:
        await dark.edit(get_string("gban_8"))
    try:
        if ungmute(user.id) is False:
            return await dark.edit("**Error! Pengguna Sedang Tidak Di Global Banned.**")
    except BaseException:
        pass
    return await dark.edit(get_string("ungban_4").format(user.first_name, user.id, user.id, me.first_name)
    )
