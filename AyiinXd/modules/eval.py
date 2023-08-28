# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
"""Userbot module for executing code and terminal commands from Telegram."""

import asyncio
import io
import sys
import traceback

from os import remove
from pprint import pprint
from sqlite3 import IntegrityError, OperationalError

from config import var
from AyiinXd import Ayiin, CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from AyiinXd.database.core import db
from AyiinXd.events import register


conn = db.get_conn()
cmd = var.CMD_HANDLER
p, pp = print, pprint


@ayiin_cmd(pattern="eval(?:\\s|$)([\\s\\S]*)")
@register(pattern=r"^Eval(?:\\s|$)([\\s\\S]*)", sudo=True)
async def _(event):
    expression = event.pattern_match.group(1)
    if not expression:
        return await eor(event, "**Berikan Code untuk di eksekusi.**")
    if expression in ("AyiinXd.session", "config.env"):
        return await eor(event, "**Itu operasi yang berbahaya! Tidak diperbolehkan!**")
    cmd = "".join(event.message.message.split(maxsplit=1)[1:])
    if not cmd:
        return eor(event, "**Apa yang harus saya jalankan ?**")
    cmd = (
        cmd.replace("sendmessage", "send_message")
        .replace("sendfile", "send_file")
        .replace("editmessage", "edit_message")
    )
    sender = await event.get_sender()
    me = await event.client.get_me()
    if sender.id != me.id:
        xx = await eor(event, '**Memproses...**')
    else:
        xx = await eor(event, '**Memproses...**')
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    reply_to_id = event.message.id

    async def aexec(code, event):
        exec(
            "async def __aexec(e, client): "
            + "\n message = event = e"
            + "\n reply = await event.get_reply_message()"
            + "\n chat_id = (await event.get_chat()).id"
            + "\n me = await client.get_me()"
            + "".join(f"\n {line}" for line in code.split("\n")),
        )

        return await locals()["__aexec"](event, event.client)

    try:
        await aexec(cmd, event)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "`Berhasil`"
    final_output = f"**⪼ Memerintah : **\n`{cmd}` \n\n**⪼  Hasil : **\n`{evaluation}` \n"

    if len(final_output) > 4096:
        yins = final_output.replace(
            "`",
            "").replace(
            "**",
            "").replace(
            "__",
            "")
        with io.BytesIO(str.encode(yins)) as out_file:
            out_file.name = "eval.txt"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                thumb="AyiinXd/resources/logo.jpg",
                allow_cache=False,
                caption=f"`{cmd}`" if len(cmd) < 998 else None,
                reply_to=reply_to_id,
            )
            await xx.delete()
    else:
        await xx.edit(final_output)


@ayiin_cmd(pattern="exec(?: |$|\n)([\\s\\S]*)")
async def run(event):
    code = event.pattern_match.group(1)
    if not code:
        return await eor(event, f"**Silahkan Ketik** `{cmd}help exec` **sebagai contoh.**")
    if code in ("AyiinXd.session", "config.env"):
        return await eor(event, "**Itu operasi yang berbahaya! Tidak diperbolehkan!**")
    await eor(event, '**Memproses...**')
    if len(code.splitlines()) <= 5:
        codepre = code
    else:
        clines = code.splitlines()
        codepre = (
            clines[0] +
            "\n" +
            clines[1] +
            "\n" +
            clines[2] +
            "\n" +
            clines[3] +
            "...")
    command = "".join(f"\n {l}" for l in code.split("\n.strip()"))
    process = await asyncio.create_subprocess_exec(
        sys.executable,
        "-c",
        command.strip(),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT,
    )
    codepre.encode("unicode-escape").decode().replace("\\\\", "\\")
    stdout, _ = await process.communicate()
    if stdout and stdout != "":
        stdout = str(stdout.decode().strip())
        stdout.encode("unicode-escape").decode().replace("\\\\", "\\")
    else:
        stdout = "`Berhasil`"
    if len(stdout) > 4096:
        with open("output.txt", "w+") as file:
            file.write(stdout)
        await event.client.send_file(
            event.chat_id,
            "output.txt",
            reply_to=event.id,
            thumb="AyiinXd/resources/logo.jpg",
            caption="**Output terlalu besar, dikirim sebagai file**",
        )
        return remove("output.txt")
    await eor(
        event,
        f"**⪼ Memerintah : **\n`{codepre}` \n\n**⪼  Hasil : **\n`{stdout}` \n"
    )


@ayiin_cmd(pattern="bash(?: |$|\n)([\\s\\S]*)")
async def terminal_runner(event):
    command = event.pattern_match.group(1)
    if not command:
        return await eod(event, f"`Berikan perintah atau gunakan {cmd}help term sebagai contoh.`")
    if command in ("AyiinXd.session", "config.env"):
        return await eod(event, "**Itu operasi yang berbahaya! Tidak diperbolehkan!**")
    await eor(event, '**Memproses...**')
    process = await asyncio.create_subprocess_shell(
        command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.STDOUT
    )
    command.encode("unicode-escape").decode().replace("\\\\", "\\")
    stdout, _ = await process.communicate()
    if stdout and stdout != "":
        result = str(stdout.decode().strip())
        result.encode("unicode-escape").decode().replace("\\\\", "\\")
    else:
        result = "`Berhasil`"
    if len(result) > 4096:
        with open("output.txt", "w+") as output:
            output.write(result)
        await event.client.send_file(
            event.chat_id,
            "output.txt",
            reply_to=event.id,
            thumb="AyiinXd/resources/logo.jpg",
            caption="**Output terlalu besar, dikirim sebagai file**",
        )
        return remove("output.txt")

    await eor(
        event,
        f"**⪼ Memerintah : **\n`{command}` \n\n**⪼  Hasil : **\n`{result}` \n"
    )


@ayiin_cmd(pattern="json$")
async def _(event):
    if event.fwd_from:
        return
    the_real_message = None
    reply_to_id = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.stringify()
        reply_to_id = event.reply_to_msg_id
    else:
        the_real_message = event.stringify()
        reply_to_id = event.message.id
    if len(the_real_message) > 4096:
        with io.BytesIO(str.encode(the_real_message)) as out_file:
            out_file.name = "json.text"
            await Ayiin.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                thumb="AyiinXd/resources/logo.jpg",
                allow_cache=False,
                reply_to=reply_to_id,
            )
            await event.delete()
    else:
        await event.edit("`{}`".format(the_real_message))


@ayiin_cmd(pattern="sql(?: |$|\n)([\\s\\S]*)")
async def execsql(event):
    command = event.pattern_match.group(1)
    if not command:
        return await eor(event, "Berikan saya kode untuk saya eksekusi")
    try:
        ex = conn.execute(command)
    except (IntegrityError, OperationalError) as e:
        return await eor(
            event,
            f"SQL executed with an error: {e.__class__.__name__}: {e}"
        )

    ret = ex.fetchall()
    conn.commit()

    if ret:
        res = "|".join([name[0] for name in ex.description]) + "\n"
        res += "\n".join(["|".join(str(s) for s in items) for items in ret])
        if len(res) > 3500:
            bio = io.BytesIO()
            bio.name = "output.txt"
            bio.write(res.encode())
            await Ayiin.send_file(
                event.chat_id,
                bio,
            )
        else:
            await eor(event, f"`{res}`")
    else:
        await eod(event, "SQL executed successfully and without any return.")


CMD_HELP.update(
    {
        "json": f"**Plugin : **`json`\
        \n\n  »  **Perintah :** `{cmd}json` <reply ke pesan>\
        \n  »  **Kegunaan : **Untuk mendapatkan detail pesan dalam format json.\
    "
    }
)


CMD_HELP.update(
    {
        "eval": f"**Plugin : **`eval`\
        \n\n  »  **Perintah :** `{cmd}eval` <cmd>\
        \n  »  **Kegunaan : **Evaluasi ekspresi Python dalam argumen skrip yang sedang berjalan\
    "
    }
)


CMD_HELP.update(
    {
        "exec": f"**Plugin : **`exec`\
        \n\n  »  **Perintah :** `{cmd}exec print('hello')`\
        \n  »  **Kegunaan : **Jalankan skrip python kecil di subproses.\
    "
    }
)


CMD_HELP.update(
    {
        "bash": f"**Plugin : **`bash`\
        \n\n  »  **Perintah :** `{cmd}bash` <cmd>\
        \n  »  **Kegunaan : **Jalankan perintah dan skrip bash di server Anda.\
    "
    }
)
