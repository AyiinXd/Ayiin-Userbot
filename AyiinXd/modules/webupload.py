# credits: SNAPDRAGON (@s_n_a_p_s)
# originally from xtra-telegram
# ported by @heyworld

import asyncio
import time

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY, bot
from AyiinXd.ayiin import ayiin_cmd, eor
from Stringyins import get_string


@ayiin_cmd(
    pattern="webupload ?(.+?|) (?:--)(anonfiles|transfer|filebin|anonymousfiles|megaupload|bayfiles)"
)
async def _(event):
    if event.fwd_from:
        return
    xx = await eor(event, get_string("com_1"))
    PROCESS_RUN_TIME = 100
    input_str = event.pattern_match.group(1)
    selected_transfer = event.pattern_match.group(2)
    if input_str:
        file_name = input_str
    else:
        reply = await event.get_reply_message()
        file_name = await bot.download_media(reply.media, TEMP_DOWNLOAD_DIRECTORY)
    CMD_WEB = {
        "anonfiles": 'curl -F "file=@{}" https://anonfiles.com/api/upload',
        "transfer": 'curl --upload-file "{}" https://transfer.sh/{os.path.basename(file_name)}',
        "filebin": 'curl -X POST --data-binary "@test.png" -H "filename: {}" "https://filebin.net"',
        "anonymousfiles": 'curl -F file="@{}" https://api.anonymousfiles.io/',
        "megaupload": 'curl -F "file=@{}" https://megaupload.is/api/upload',
        "bayfiles": '.exec curl -F "file=@{}" https://bayfiles.com/api/upload',
    }
    try:
        selected_one = CMD_WEB[selected_transfer].format(file_name)
    except KeyError:
        await xx.edit(get_string("webup_1"))
    cmd = selected_one
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    await xx.edit(f"{stdout.decode()}")


CMD_HELP.update(
    {
        "webupload": f"**Plugin : **`webupload`\
        \n\n  »  **Perintah :** `{cmd}webupload --`(`anonfiles`|`transfer`|`filebin`|`anonymousfiles`|`megaupload`|`bayfiles`)\
        \n  »  **Kegunaan : **Reply `{cmd}webupload --anonfiles` or `.webupload --filebin` dan file akan diunggah ke situs web itu. \
    "
    }
)
