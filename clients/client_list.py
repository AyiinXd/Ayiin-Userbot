# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

import telethon.utils
from telethon.tl.functions.users import GetFullUserRequest


async def clients_list(SUDO_USERS, bot, AYIIN2, AYIIN3, AYIIN4, AYIIN5):
    user_ids = list(SUDO_USERS) or []
    main_id = await bot.get_me()
    user_ids.append(main_id.id)

    try:
        if AYIIN2 is not None:
            id2 = await AYIIN2.get_me()
            user_ids.append(id2.id)
    except BaseException:
        pass

    try:
        if AYIIN3 is not None:
            id3 = await AYIIN3.get_me()
            user_ids.append(id3.id)
    except BaseException:
        pass

    try:
        if AYIIN4 is not None:
            id4 = await AYIIN4.get_me()
            user_ids.append(id4.id)
    except BaseException:
        pass

    try:
        if AYIIN5 is not None:
            id5 = await AYIIN5.get_me()
            user_ids.append(id5.id)
    except BaseException:
        pass

    return user_ids


async def client_id(event, botid=None):
    if botid is not None:
        uid = await event.client(GetFullUserRequest(botid))
        OWNER_ID = uid.user.id
        AYIIN_USER = uid.user.first_name
    else:
        client = await event.client.get_me()
        uid = telethon.utils.get_peer_id(client)
        OWNER_ID = uid
        AYIIN_USER = client.first_name
    ayiin_mention = f"[{AYIIN_USER}](tg://user?id={OWNER_ID})"
    return OWNER_ID, AYIIN_USER, ayiin_mention
