# Copyright (C) 2020 TeamDerUntergang.
#
# SedenUserBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SedenUserBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# @Qulec tarafından yazılmıştır.
# Thanks @Spechide.

from telethon.errors.rpcerrorlist import BotInlineDisabledError as noinline
from telethon.errors.rpcerrorlist import BotResponseTimeoutError as timout
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest

from config import var
from AyiinXd import Ayiin, CMD_HELP, bot, ch
from AyiinXd.ayiin import ayiin_cmd, eod, eor


@ayiin_cmd(pattern="help(?: |$)(.*)")
async def helpyins(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await eor(event, f"{CMD_HELP[args]}\n\n© AyiinChats")
        else:
            await eod(
                event,
                f"**Modul {args} Tidak diketahui**, **Silahkan Ketik {var.CMD_HANDLER}help untuk melihat modul.**"
            )
    else:
        AyiinUBOT = await bot.get_me()
        BOT_USERNAME = AyiinUBOT.username
        if BOT_USERNAME is not None:
            chat = "@Botfather"
            try:
                results = await event.client.inline_query(
                    BOT_USERNAME,
                    "@AyiinChats"
                )
                await results[0].click(
                    event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
                )
                await event.delete()
            except timout:
                return await eor(
                    event,
                    f"Bot tidak menanggapi inline kueri.\nSilahkan Ketik `{var.CMD_HANDLER}restart`"
                )
            except noinline:
                xx = await eor(
                    event,
                    "**Inline Mode Tidak aktif.**\n__Sedang Menyalakannya, Harap Tunggu Sebentar...__",
                )
                async with event.client.conversation(chat) as conv:
                    try:
                        first = await conv.send_message("/setinline")
                        second = await conv.get_response()
                        third = await conv.send_message(BOT_USERNAME)
                        fourth = await conv.get_response()
                        fifth = await conv.send_message("Search")
                        sixth = await conv.get_response()
                        await event.client.send_read_acknowledge(conv.chat_id)
                    except YouBlockedUserError:
                        await event.client(UnblockRequest(chat))
                        first = await conv.send_message("/setinline")
                        second = await conv.get_response()
                        third = await conv.send_message(BOT_USERNAME)
                        fourth = await conv.get_response()
                        fifth = await conv.send_message("Search")
                        sixth = await conv.get_response()
                        await event.client.send_read_acknowledge(conv.chat_id)
                    await xx.edit(
                        f"**Berhasil Menyalakan Mode Inline**\n\n**Ketik** `{var.CMD_HANDLER}help` **lagi untuk membuka menu bantuan.**"
                    )
                await event.client.delete_messages(
                    conv.chat_id,
                    [first.id, second.id, third.id, fourth.id, fifth.id, sixth.id],
                )
        else:
            await eor(
                event,
                "**Silahkan Buat BOT di @BotFather dan Tambahkan Var** `BOT_TOKEN` & `BOT_USERNAME`",
            )
