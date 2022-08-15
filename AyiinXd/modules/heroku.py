# Copyright (C) 2020 Adek Maulana.
# All rights reserved.
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
"""
   Heroku manager for your userbot
"""

import math
import os

import aiohttp
import heroku3
import urllib3

from AyiinXd import BOTLOG_CHATID
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, HEROKU_API_KEY, HEROKU_APP_NAME
from AyiinXd.modules.sql_helper.globals import addgvar, delgvar, gvarstatus
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from Stringyins import get_string
from time import sleep

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
heroku_api = "https://api.heroku.com"
if HEROKU_APP_NAME is not None and HEROKU_API_KEY is not None:
    Heroku = heroku3.from_key(HEROKU_API_KEY)
    app = Heroku.app(HEROKU_APP_NAME)
    heroku_var = app.config()
else:
    app = None


"""
   ConfigVars setting, get current var, set var or delete var...
"""


@ayiin_cmd(pattern="(get|del) var(?: |$)(\\w*)", allow_sudo=False)
async def variable(var):
    exe = var.pattern_match.group(1)
    if app is None:
        await eor(var, get_string("heroku_1")
        )
        return False
    if exe == "get":
        xx = await eor(var, get_string("com_8"))
        variable = var.pattern_match.group(2)
        if variable == "":
            configvars = heroku_var.to_dict()
            if BOTLOG_CHATID:
                msg = "".join(
                    f"`{item}` = `{configvars[item]}`\n" for item in configvars
                )
                await var.client.send_message(
                    BOTLOG_CHATID, get_string("heroku_2").format(msg)
                )
                await xx.edit(get_string("heroku_3"))
                return True
            await xx.edit(get_string("heroku_4"))
            return False
        if variable in heroku_var:
            if BOTLOG_CHATID:
                await var.client.send_message(
                    BOTLOG_CHATID, get_string("heroku_9").format(variable, heroku_var[variable])
                )
                await xx.edit(get_string("heroku_6"))
                return True
            await xx.edit(get_string("heroku_4"))
            return False
        await var.edit(get_string("com_8"))
        return True
    if exe == "del":
        xx = await eor(var, get_string("heroku_7"))
        variable = var.pattern_match.group(2)
        if variable == "":
            await xx.edit(get_string("heroku_8"))
            return False
        if variable in heroku_var:
            if BOTLOG_CHATID:
                await var.client.send_message(
                    BOTLOG_CHATID, get_string("heroku_9").format(variable)
                )
            await xx.edit(get_string("heroku_10"))
            del heroku_var[variable]
        else:
            await xx.edit(get_string("heroku_11"))
            return True


@ayiin_cmd(pattern="set var (\\w*) ([\\s\\S]*)", allow_sudo=False)
async def set_var(var):
    if app is None:
        return await eor(
            var, "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **dan** `HEROKU_API_KEY`"
        )
    xx = await eor(var, get_string("com_1"))
    variable = var.pattern_match.group(1)
    value = var.pattern_match.group(2)
    if variable in heroku_var:
        if BOTLOG_CHATID:
            await var.client.send_message(
                BOTLOG_CHATID, get_string("heroku_5").format(variable, value)
            )
        await eod(var, get_string("heroku_13"))
    else:
        if BOTLOG_CHATID:
            await var.client.send_message(
                BOTLOG_CHATID, get_string("heroku_5").format(variable, value)
            )
        await xx.edit(get_string("heroku_14"))
    heroku_var[variable] = value


"""
    Check account quota, remaining quota, used quota, used app quota
"""


@ayiin_cmd(pattern="(usage|kuota|dyno)(?: |$)")
async def dyno_usage(dyno):
    if app is None:
        return await dyno.edit(get_string("heroku_12")
        )
    xx = await eor(dyno, "🤖")
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/81.0.4044.117 Mobile Safari/537.36"
    )
    user_id = Heroku.account().id
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    async with aiohttp.ClientSession() as session, session.get(
        heroku_api + path, headers=headers
    ) as r:
        if r.status != 200:
            await dyno.client.send_message(
                dyno.chat_id, f"`{r.reason}`", reply_to=dyno.id
            )
            await xx.edit(get_string("usage_1"))
            return False
        result = await r.json()
        quota = result["account_quota"]
        quota_used = result["quota_used"]

        """ - User Quota Limit and Used - """
        remaining_quota = quota - quota_used
        percentage = math.floor(remaining_quota / quota * 100)
        minutes_remaining = remaining_quota / 60
        hours = math.floor(minutes_remaining / 60)
        minutes = math.floor(minutes_remaining % 60)
        day = math.floor(hours / 24)

        """ - User App Used Quota - """
        Apps = result["apps"]
        for apps in Apps:
            if apps.get("app_uuid") == app.id:
                AppQuotaUsed = apps.get("quota_used") / 60
                AppPercentage = math.floor(
                    apps.get("quota_used") * 100 / quota)
                break
        else:
            AppQuotaUsed = 0
            AppPercentage = 0

        AppHours = math.floor(AppQuotaUsed / 60)
        AppMinutes = math.floor(AppQuotaUsed % 60)

        sleep(3)
        await xx.edit(get_string("usage_2").format(app.name, AppHours, AppMinutes, AppPercentage, hours, minutes, percentage, day)
        )
        return True


@ayiin_cmd(pattern="usange(?: |$)")
async def fake_dyno(event):
    xx = await eor(event, get_string("com_1"))
    await xx.edit(get_string("usange_1").format(app.name)
    )


@ayiin_cmd(pattern="logs")
async def _(dyno):
    if app is None:
        return await eor(
            dyno, get_string("heroku_12")
        )
    xx = await eor(dyno, get_string("logs_2"))
    data = app.get_log()
    await eor(xx, data, deflink=True, linktext=get_string("logs_1"))


@ayiin_cmd(pattern="getdb ?(.*)", allow_sudo=False)
async def getsql(event):
    var_ = event.pattern_match.group(1)
    xxnx = await eor(event, get_string("getdb_1").format(var_))
    if var_ == "":
        return await xxnx.edit(get_string("getdb_2").format(cmd)
        )
    try:
        sql_v = gvarstatus(var_)
        os_v = os.environ.get(var_) or "None"
    except Exception as e:
        return await xxnx.edit(get_string("error_1").format(e))
    await xxnx.edit(get_string("getdb_3").format(var_, os_v, var_, sql_v)
    )


@ayiin_cmd(pattern="setdb ?(.*)", allow_sudo=False)
async def setsql(event):
    hel_ = event.pattern_match.group(1)
    var_ = hel_.split(" ")[0]
    val_ = hel_.split(" ")[1:]
    valu = " ".join(val_)
    xxnx = await eor(event, get_string("setdb_1").format(var_, valu))
    if "" in (var_, valu):
        return await xxnx.edit(get_string("setdb_2").format(cmd)
        )
    try:
        addgvar(var_, valu)
    except Exception as e:
        return await xxnx.edit(get_string("error_1").format(e))
    await xxnx.edit(get_string("setdb_3").format(var_, valu))


@ayiin_cmd(pattern="deldb ?(.*)", allow_sudo=False)
async def delsql(event):
    var_ = event.pattern_match.group(1)
    xxnx = await eor(event, get_string("deldb_1").format(var_))
    if var_ == "":
        return await xxnx.edit(get_string("deldb_2").format(cmd)
        )
    try:
        delgvar(var_)
    except Exception as e:
        return await xxnx.edit(get_string("error_1").format(e))
    await xxnx.edit(get_string("deldb_3").format(var_))


CMD_HELP.update(
    {
        "heroku": f"**Plugin : **`heroku`\
        \n\n  »  **Perintah :** `{cmd}set var <nama var> <value>`\
        \n  »  **Kegunaan : **Tambahkan Variabel Baru Atau Memperbarui Variabel Setelah Menyetel Variabel Ayiin-Userbot Akan Di Restart.\
        \n\n  »  **Perintah :** `{cmd}get var or {cmd}get var <nama var>`\
        \n  »  **Kegunaan : **Dapatkan Variabel Yang Ada,Harap Gunakan Di Grup Private Anda!\
        \n\n  »  **Perintah :** `{cmd}del var <nama var>`\
        \n  »  **Kegunaan : **Untuk Menghapus var heroku\
        \n\n  »  **Perintah :** `{cmd}usage` atau `{cmd}kuota`\
        \n  »  **Kegunaan : **Check Kouta Dyno Heroku\
        \n\n  »  **Perintah :** `{cmd}usange`\
        \n  »  **Kegunaan : **Fake Check Kouta Dyno Heroku jadi 9999jam Untuk menipu temanmu wkwk\
    "
    }
)


CMD_HELP.update(
    {
        "database": f"**Plugin : **`database`\
        \n\n  »  **Perintah :** `{cmd}setdb <nama var> <value>`\
        \n  »  **Kegunaan : **Tambahkan Variabel SQL Tanpa Merestart userbot.\
        \n\n  »  **Perintah :** `{cmd}getdb <nama var>`\
        \n  »  **Kegunaan : **Dapatkan Variabel SQL Yang Ada Harap Gunakan Di Grup Private Anda!\
        \n\n  »  **Perintah :** `{cmd}deldb <nama var>`\
        \n  »  **Kegunaan : **Untuk Menghapus Variabel SQL\
    "
    }
)