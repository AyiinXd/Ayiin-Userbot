# Credit by https://github.com/sandy1709/catuserbot
# Ported by @X_ImFine
# Recode by @mrismanaziz
# @SharingUserbot

from asyncio import sleep

from AyiinXd import BOTLOG_CHATID
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, LOGS
from AyiinXd.modules.sql_helper import broadcast_sql as sql
from AyiinXd.ayiin import ayiin_cmd, eor, parse_pre
from Stringyins import get_string


@ayiin_cmd(pattern=r"sendto ?(.*)")
async def catbroadcast_send(event):
    if event.fwd_from:
        return
    catinput_str = event.pattern_match.group(1)
    if not catinput_str:
        return await eor(event, get_string("bd_10"), parse_mode=parse_pre
                         )
    reply = await event.get_reply_message()
    if not reply:
        return await eor(event, get_string("bd_1"), parse_mode=parse_pre
                         )
    keyword = catinput_str.lower()
    no_of_chats = sql.num_broadcastlist_chat(keyword)
    if no_of_chats == 0:
        return await event.edit(event, get_string("bd_2").format(keyword, cmd),
                                parse_mode=parse_pre,
                                )
    chats = sql.get_chat_broadcastlist(keyword)
    catevent = await eor(event, get_string("bd_3"),
                         parse_mode=parse_pre,
                         )
    i = 0
    for chat in chats:
        try:
            if int(event.chat_id) == int(chat):
                continue
            await event.client.send_message(int(chat), reply)
            i += 1
        except Exception as e:
            LOGS.info(str(e))
        await sleep(0.5)
    resultext = get_string("bd_4").format(i, no_of_chats, keyword)
    await catevent.edit(resultext)
    if BOTLOG_CHATID:
        await event.client.send_message(
            BOTLOG_CHATID, get_string("bd_5").format(i, no_of_chats, keyword),
            parse_mode=parse_pre,
        )


@ayiin_cmd(pattern=r"fwdto ?(.*)")
async def catbroadcast_send(event):
    if event.fwd_from:
        return
    catinput_str = event.pattern_match.group(1)
    if not catinput_str:
        return await eor(event, get_string("bd_10"), parse_mode=parse_pre
                         )
    reply = await event.get_reply_message()
    if not reply:
        return await eor(event, get_string("bd_1"), parse_mode=parse_pre
                         )
    keyword = catinput_str.lower()
    no_of_chats = sql.num_broadcastlist_chat(keyword)
    if no_of_chats == 0:
        return await eor(event, get_string("bd_2").format(keyword, cmd),
                               parse_mode=parse_pre,
                               )
    chats = sql.get_chat_broadcastlist(keyword)
    catevent = await eor(event, get_string("bd_3"), parse_mode=parse_pre,
                               )
    i = 0
    for chat in chats:
        try:
            if int(event.chat_id) == int(chat):
                continue
            await event.client.forward_messages(int(chat), reply)
            i += 1
        except Exception as e:
            LOGS.info(str(e))
        await sleep(0.5)
    resultext = get_string("bd_4").format(i, no_of_chats, keyword)
    await catevent.edit(resultext)
    if BOTLOG_CHATID:
        await event.client.send_message(
            BOTLOG_CHATID, get_string("bd_5").format(i, no_of_chats, keyword),
            parse_mode=parse_pre,
        )


@ayiin_cmd(pattern=r"addto ?(.*)")
async def catbroadcast_add(event):
    if event.fwd_from:
        return
    catinput_str = event.pattern_match.group(1)
    if not catinput_str:
        return await eor(event, get_string("bd_6"), parse_mode=parse_pre
                               )
    keyword = catinput_str.lower()
    check = sql.is_in_broadcastlist(keyword, event.chat_id)
    if check:
        return await eor(event, get_string("bd_7").format(keyword),
                               parse_mode=parse_pre,
                               )
    sql.add_to_broadcastlist(keyword, event.chat_id)
    await eor(event, get_string("bd_8").format(keyword), parse_mode=parse_pre
                    )
    chat = await event.get_chat()
    if BOTLOG_CHATID:
        try:
            await event.client.send_message(
                BOTLOG_CHATID, get_string("bd_9").format(chat.title, keyword),
                parse_mode=parse_pre,
            )
        except Exception:
            await event.client.send_message(
                BOTLOG_CHATID, get_string("bd_11").format(chat.first_name, keyword),
                parse_mode=parse_pre,
            )


@ayiin_cmd(pattern=r"rmfrom ?(.*)")
async def catbroadcast_remove(event):
    if event.fwd_from:
        return
    catinput_str = event.pattern_match.group(1)
    if not catinput_str:
        return await eor(event, get_string("bd_12"), parse_mode=parse_pre
                               )
    keyword = catinput_str.lower()
    check = sql.is_in_broadcastlist(keyword, event.chat_id)
    if not check:
        return await eor(event, get_string("bd_13").format(keyword), parse_mode=parse_pre
                               )
    sql.rm_from_broadcastlist(keyword, event.chat_id)
    await eor(event, get_string("bd_14").format(keyword),
                    parse_mode=parse_pre,
                    )
    chat = await event.get_chat()
    if BOTLOG_CHATID:
        try:
            await event.client.send_message(
                BOTLOG_CHATID, get_string("bd_15").format(chat.title, keyword),
                parse_mode=parse_pre,
            )
        except Exception:
            await event.client.send_message(
                BOTLOG_CHATID, get_string("bd_16").format(chat.first_name, keyword),
                parse_mode=parse_pre,
            )


@ayiin_cmd(pattern=r"bclist ?(.*)")
async def catbroadcast_list(event):
    if event.fwd_from:
        return
    catinput_str = event.pattern_match.group(1)
    if not catinput_str:
        return await event.edit(get_string("bd_17").format(cmd),
                                parse_mode=parse_pre,
                                )
    keyword = catinput_str.lower()
    no_of_chats = sql.num_broadcastlist_chat(keyword)
    if no_of_chats == 0:
        return await event.edit(get_string("bd_18").format(keyword, cmd),
                                parse_mode=parse_pre,
                                )
    chats = sql.get_chat_broadcastlist(keyword)
    catevent = await event.edit(get_string("bd_19").format(keyword), parse_mode=parse_pre
                                )
    resultlist = get_string("bd_20").format(keyword, no_of_chats)
    errorlist = ""
    for chat in chats:
        try:
            chatinfo = await event.client.get_entity(int(chat))
            try:
                if chatinfo.broadcast:
                    resultlist += f" 👉 📢 **Channel** \n  •  **Name : **{chatinfo.title} \n  •  **id : **`{int(chat)}`\n\n"
                else:
                    resultlist += f" 👉 👥 **Group** \n  •  **Name : **{chatinfo.title} \n  •  **id : **`{int(chat)}`\n\n"
            except AttributeError:
                resultlist += f" 👉 👤 **User** \n  •  **Name : **{chatinfo.first_name} \n  •  **id : **`{int(chat)}`\n\n"
        except Exception:
            errorlist += get_string("bd_21").format(int(chat),
                                                    cmd, keyword, int(chat))
    finaloutput = resultlist + errorlist
    await catevent.edit(finaloutput)


@ayiin_cmd(pattern=r"bclistall ?(.*)")
async def catbroadcast_list(event):
    if event.fwd_from:
        return
    if sql.num_broadcastlist_chats() == 0:
        return await event.edit(get_string("bd_22"),
                                parse_mode=parse_pre,
                                )
    chats = sql.get_broadcastlist_chats()
    resultext = "**Berikut adalah daftar kategori Anda :**\n\n"
    for i in chats:
        resultext += get_string("bd_24").format(i,
                                                sql.num_broadcastlist_chat(i))
    await event.efit(resultext)


@ayiin_cmd(pattern=r"frmfrom ?(.*)")
async def catbroadcast_remove(event):
    if event.fwd_from:
        return
    catinput_str = event.pattern_match.group(1)
    if not catinput_str:
        return await event.edit(get_string("bd_12"), parse_mode=parse_pre
                                )
    args = catinput_str.split(" ")
    if len(args) != 2:
        return await event.edit(get_string("bd_25").format(cmd),
                                parse_mode=parse_pre,
                                )
    try:
        groupid = int(args[0])
        keyword = args[1].lower()
    except ValueError:
        try:
            groupid = int(args[1])
            keyword = args[0].lower()
        except ValueError:
            return await event.edit(
                event, get_string("bd_25").format(cmd),
                parse_mode=parse_pre,
            )
    keyword = keyword.lower()
    check = sql.is_in_broadcastlist(keyword, int(groupid))
    if not check:
        return await event.edit(get_string("bd_26").format(groupid, keyword),
                                parse_mode=parse_pre,
                                )
    sql.rm_from_broadcastlist(keyword, groupid)
    await event.edit(get_string("bd_27").format(groupid, keyword),
                     parse_mode=parse_pre,
                     )
    chat = await event.get_chat()
    if BOTLOG_CHATID:
        try:
            await event.client.send_message(
                BOTLOG_CHATID, get_string("bd_27").format(chat.title, keyword),
                parse_mode=parse_pre,
            )
        except Exception:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"pengguna {chat.first_name} dihapus dari kategori {keyword}",
                parse_mode=parse_pre,
            )


@ayiin_cmd(pattern=r"delc ?(.*)")
async def catbroadcast_delete(event):
    if event.fwd_from:
        return
    catinput_str = event.pattern_match.group(1)
    check1 = sql.num_broadcastlist_chat(catinput_str)
    if check1 < 1:
        return await event.edit(get_string("bd_28").format(catinput_str),
                                parse_mode=parse_pre,
                                )
    try:
        sql.del_keyword_broadcastlist(catinput_str)
        await event.edit(get_string("bd_29").format(catinput_str),
                         parse_mode=parse_pre,
                         )
    except Exception as e:
        await event.edit(get_string("error_1").format(e),
                         parse_mode=parse_pre,
                         )


CMD_HELP.update(
    {
        "broadcast": f"**Plugin : **`broadcast`\
        \n\n  »  **Perintah :** `{cmd}sendto` <category_name>\
        \n  »  **Kegunaan : **akan mengirim pesan balasan ke semua obrolan dalam kategori yang diberikan.\
        \n\n  »  **Perintah :** `{cmd}fwdto` <category_name>\
        \n  »  **Kegunaan : **akan meneruskan pesan yang dibalas ke semua obrolan di kategori berikan. \
        \n\n  »  **Perintah :** `{cmd}addto` <category name>\
        \n  »  **Kegunaan : **Ini akan menambahkan obrolan / pengguna / saluran ini ke kategori nama yang diberikan. \
        \n\n  »  **Perintah :** `{cmd}rmfrom` <category name>\
        \n  »  **Kegunaan : **Untuk menghapus Obrolan / pengguna / saluran dari nama kategori yang diberikan. \
        \n\n  »  **Perintah :** `{cmd}bclist` <category_name>\
        \n  »  **Kegunaan : **Akan menampilkan daftar semua obrolan dalam kategori yang diberikan. \
        \n\n  »  **Perintah :** `{cmd}bclistall`\
        \n  »  **Kegunaan : **Akan menampilkan daftar semua nama kategori. \
        \n\n  »  **Perintah :** `{cmd}frmfrom` <category_name/chat_id>\
        \n  »  **Kegunaan : **Untuk memaksa menghapus chat_id yang diberikan dari nama kategori yang diberikan berguna ketika Anda meninggalkan obrolan itu atau melarang Anda di sana \
        \n\n  »  **Perintah :** `{cmd}delc` <category_name>\
        \n  »  **Kegunaan : **Menghapus kategori sepenuhnya di database \
    "
    }
)
