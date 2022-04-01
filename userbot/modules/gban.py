# by:koala @mixiologist
# Lord Userbot


from userbot import DEVS, WHITELIST, blacklistayiin
from userbot.events import register
from userbot.utils import ayiin_cmd, chataction, get_user_from_event

# Ported For Lord-Userbot by liualvinas/Alvin


@chataction()
async def handler(tele):
    if not tele.user_joined and not tele.user_added:
        return
    try:
        from userbot.modules.sql_helper.gmute_sql import is_gmuted

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
                        await client.edit_permissions(
                            tele.chat_id, guser.id, view_messages=False
                        )
                        await tele.reply(
                            f"**𝘽𝙖𝙣𝙣𝙚𝙙 𝙎𝙥𝙤𝙩𝙚𝙙**\n"
                            f"**𝙁𝙞𝙧𝙨𝙩 𝙉𝙖𝙢𝙚 :** [{guser.id}](tg://user?id={guser.id})\n"
                            f"**𝘼𝙘𝙩𝙞𝙤𝙣 :** `𝘽𝙖𝙣𝙣𝙚𝙙 𝙄𝙣 𝙂𝙧𝙤𝙪𝙥`\n"
                            f"**𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 :** ✧ 𝙰𝚈𝙸𝙸𝙽-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ✧"
                        )
                    except BaseException:
                        return


@ayiin_cmd(pattern="gban(?: |$)(.*)")
@register(pattern=r"^\.cgban(?: |$)(.*)", sudo=True)
async def gben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if sender.id != me.id:
        dark = await dc.reply("`𝙂𝙪𝙖 𝙋𝙧𝙤𝙨𝙚𝙨 𝙂𝙗𝙖𝙣𝙣𝙞𝙣𝙜 𝙎𝙚𝙠𝙖𝙧𝙖𝙣𝙜 𝙏𝙤𝙙...`")
    else:
        dark = await dc.edit("`𝙈𝙚𝙢𝙥𝙧𝙤𝙨𝙚𝙨 𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙 𝙏𝙞𝙩𝙞𝙨𝙖𝙣 𝘿𝙖𝙟𝙟𝙖𝙡..`")
    await dark.edit("`𖣘 𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙 𝘼𝙠𝙖𝙣 𝘼𝙠𝙩𝙞𝙛 𝙏𝙤𝙙..`")
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
        return await dark.edit("**𝘼𝙣𝙟𝙞𝙣𝙜 𝙂𝙖𝙜𝙖𝙡 𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙 :(**")
    if user:
        if user.id in DEVS:
            return await dark.edit("**𝙂𝙖𝙜𝙖𝙡 𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙 𝙏𝙤𝙙, 𝙆𝙖𝙧𝙣𝙖 𝘿𝙞𝙖 𝘼𝙙𝙖𝙡𝙖𝙝 𝘽𝙤𝙨𝙨 𝙂𝙪𝙖 🤪**")
        if user.id in WHITELIST:
            return await dark.edit(
                "**Gagal Global Banned, Karna dia adalah suhu cuaca 🤪**"
            )
        try:
            from userbot.modules.sql_helper.gmute_sql import gmute
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
                await dark.edit(
                    r"\\**#𝙂𝘽𝙖𝙣𝙣𝙚𝙙_𝙐𝙨𝙚𝙧**//"
                    f"\n\n**𝙁𝙞𝙧𝙨𝙩 𝙉𝙖𝙢𝙚 :** [{user.first_name}](tg://user?id={user.id})\n"
                    f"**𝙐𝙨𝙚𝙧 𝙄𝘿 :** `{user.id}`\n"
                    f"**𝘼𝙘𝙩𝙞𝙤𝙣 :** `𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙`"
                )
            except BaseException:
                b += 1
    else:
        await dark.edit("**𝘽𝙖𝙡𝙖𝙨 𝙆𝙚 𝙋𝙚𝙨𝙖𝙣 𝙋𝙚𝙣𝙜𝙜𝙪𝙣𝙖𝙣𝙮𝙖 𝙂𝙤𝙗𝙡𝙤𝙠**")
    try:
        if gmute(user.id) is False:
            return await dark.edit(
                "**#𝘼𝙡𝙧𝙚𝙖𝙙𝙮_𝙂𝘽𝙖𝙣𝙣𝙚𝙙**\n\n𝙐𝙨𝙚𝙧 𝘼𝙡𝙧𝙚𝙖𝙙𝙮 𝙀𝙭𝙞𝙨𝙩𝙨 𝙄𝙣 𝙈𝙮 𝙂𝙗𝙖𝙣 𝙇𝙞𝙨𝙩.**"
            )

    except BaseException:
        pass
    return await dark.edit(
        r"\\**#𝙂𝘽𝙖𝙣𝙣𝙚𝙙_𝙐𝙨𝙚𝙧**//"
        f"\n\n**𝙁𝙞𝙧𝙨𝙩 𝙉𝙖𝙢𝙚 :** [{user.first_name}](tg://user?id={user.id})\n"
        f"**𝙐𝙨𝙚𝙧 𝙄𝘿 :** `{user.id}`\n"
        f"**𝘼𝙘𝙩𝙞𝙤𝙣 :** `𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙`\n"
        f"**𝙂𝙗𝙖𝙣𝙣𝙚𝙙 𝘽𝙮 :** `{me.first_name}`\n"
        f"**𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 : ✧ 𝙰𝚈𝙸𝙸𝙽-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ✧**"
    )


@ayiin_cmd(pattern=r"ungban(?: |$)(.*)")
@register(pattern=r"^\.cungban(?: |$)(.*)", sudo=True)
async def gunben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if sender.id != me.id:
        dark = await dc.reply("`𝙐𝙣𝙂𝙗𝙖𝙣𝙣𝙞𝙣𝙜...`")
    else:
        dark = await dc.edit("`𝙐𝙣𝙂𝙗𝙖𝙣𝙣𝙞𝙣𝙜....`")
    await dark.edit("`𝙈𝙚𝙢𝙗𝙖𝙩𝙖𝙡𝙠𝙖𝙣 𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙`")
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
        return await dark.edit("**`𝙂𝙖𝙜𝙖𝙡 𝙐𝙣𝙂𝙗𝙖𝙣𝙣𝙚𝙙 :(`**")
    if user:
        if user.id in blacklistayiin:
            return await dark.edit(
                "**𝙂𝙖𝙜𝙖𝙡 𝙐𝙣𝙜𝙗𝙖𝙣𝙣𝙚𝙙, 𝙆𝙖𝙧𝙚𝙣𝙖 𝘿𝙞𝙖 𝘼𝙙𝙖 𝘿𝙞 𝘽𝙡𝙖𝙘𝙠𝙡𝙞𝙨𝙩 𝘼𝙮𝙞𝙞𝙣**"
            )
        try:
            from userbot.modules.sql_helper.gmute_sql import ungmute
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
                await dark.edit("`𝙈𝙚𝙢𝙗𝙖𝙩𝙖𝙡𝙠𝙖𝙣 𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙...`")
            except BaseException:
                b += 1
    else:
        await dark.edit("`𝘽𝙖𝙡𝙖𝙨 𝙆𝙚 𝙋𝙚𝙨𝙖𝙣 𝙋𝙚𝙣𝙜𝙜𝙪𝙣𝙖𝙣𝙮𝙖 𝙂𝙤𝙗𝙡𝙤𝙠`")
    try:
        if ungmute(user.id) is False:
            return await dark.edit("**𝙀𝙧𝙧𝙤𝙧! 𝙋𝙚𝙣𝙜𝙜𝙪𝙣𝙖 𝙎𝙚𝙙𝙖𝙣𝙜 𝙏𝙞𝙙𝙖𝙠 𝘿𝙞 𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙.**")
    except BaseException:
        pass
    return await dark.edit(
        r"\\**#𝙐𝙣𝙂𝙗𝙖𝙣𝙣𝙚𝙙_𝙐𝙨𝙚𝙧**//"
        f"\n\n**𝙁𝙞𝙧𝙨𝙩 𝙉𝙖𝙢𝙚 :** [{user.first_name}](tg://user?id={user.id})\n"
        f"**𝙐𝙨𝙚𝙧 𝙄𝘿 :** `{user.id}`\n"
        f"**𝘼𝙘𝙩𝙞𝙤𝙣 :** `𝙐𝙣𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙`\n"
        f"**𝙐𝙣𝙂𝙗𝙖𝙣𝙣𝙚𝙙 𝘽𝙮 :** `{me.first_name}`\n"
        f"**𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 : ✧ 𝙰𝚈𝙸𝙸𝙽-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ✧**"
    )
