# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for getting the date
    and time of any country or the userbot server.  """

from datetime import datetime as dt

from pytz import country_names as c_n
from pytz import country_timezones as c_tz
from pytz import timezone as tz

from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd


from . import cmd, var


async def get_tz(con):
    """Get time zone of the given country."""
    if "(Uk)" in con:
        con = con.replace("Uk", "UK")
    if "(Us)" in con:
        con = con.replace("Us", "US")
    if " Of " in con:
        con = con.replace(" Of ", " of ")
    if "(Western)" in con:
        con = con.replace("(Western)", "(western)")
    if "Minor Outlying Islands" in con:
        con = con.replace("Minor Outlying Islands", "minor outlying islands")
    if "Nl" in con:
        con = con.replace("Nl", "NL")

    for c_code in c_n:
        if con == c_n[c_code]:
            return c_tz[c_code]
    try:
        if c_n[con]:
            return c_tz[con]
    except KeyError:
        return


@ayiin_cmd(pattern="time(?: |$)(.*)(?<![0-9])(?: |$)([0-9]+)?")
async def time_func(tdata):
    """For .time command, return the time of
    1. The country passed as an argument,
    2. The default userbot country(set it by using .settime),
    3. The server where the userbot runs.
    """
    con = tdata.pattern_match.group(1).title()
    tz_num = tdata.pattern_match.group(2)

    t_form = "%H:%M"
    c_name = None

    if len(con) > 4:
        try:
            c_name = c_n[con]
        except KeyError:
            c_name = con
        timezones = await get_tz(con)
    elif var.COUNTRY:
        c_name = var.COUNTRY
        tz_num = var.TZ_NUMBER
        timezones = await get_tz(var.COUNTRY)
    else:
        await tdata.edit(f"**Sekarang Jam**  `{dt.now().strftime(t_form)}`  **disini**")
        return

    if not timezones:
        await tdata.edit("`Negara tidak valid.`")
        return

    if len(timezones) == 1:
        time_zone = timezones[0]
    elif len(timezones) > 1:
        if tz_num:
            tz_num = int(tz_num)
            time_zone = timezones[tz_num - 1]
        else:
            return_str = f"`{c_name} memiliki beberapa zona waktu:`\n\n"

            for i, item in enumerate(timezones):
                return_str += f"`{i+1}. {item}`\n"

            return_str += "\n`Pilih salah satu dengan mengetikkan angka"
            return_str += "dalam perintah.`\n"
            return_str += f"`Contoh: {cmd}time {c_name} 2`"

            await tdata.edit(return_str)
            return

    dtnow = dt.now(tz(time_zone)).strftime(t_form)

    if c_name != var.COUNTRY:
        await tdata.edit(
            f"**Sekarang Jam** `{dtnow}` **di {c_name}({time_zone} timezone).**"
        )
        return

    if var.COUNTRY:
        await tdata.edit(
            f"**Sekarang Tanggal** `{dtnow}` **di {var.COUNTRY} ({time_zone} timezone.)**"
        )
        return


@ayiin_cmd(pattern="date(?: |$)(.*)(?<![0-9])(?: |$)([0-9]+)?")
async def date_func(dat):
    """For .date command, return the date of
    1. The country passed as an argument,
    2. The default userbot country(set it by using .settime),
    3. The server where the userbot runs.
    """
    con = dat.pattern_match.group(1).title()
    tz_num = dat.pattern_match.group(2)

    d_form = "%d/%m/%y - %A"
    c_name = ""

    if len(con) > 4:
        try:
            c_name = c_n[con]
        except KeyError:
            c_name = con
        timezones = await get_tz(con)
    elif var.COUNTRY:
        c_name = var.COUNTRY
        tz_num = var.TZ_NUMBER
        timezones = await get_tz(var.COUNTRY)
    else:
        await dat.edit(f"**Sekarang Tanggal** `{dt.now().strftime(d_form)}` **disini.**"
        )
        return

    if not timezones:
        await dat.edit("`Negara tidak valid.`")
        return

    if len(timezones) == 1:
        time_zone = timezones[0]
    elif len(timezones) > 1:
        if tz_num:
            tz_num = int(tz_num)
            time_zone = timezones[tz_num - 1]
        else:
            return_str = f"`{c_name} memiliki beberapa zona waktu:`\n\n"

            for i, item in enumerate(timezones):
                return_str += f"`{i+1}. {item}`\n"

            return_str += "\n`Pilih salah satu dengan mengetikkan angka"
            return_str += "dalam perintah.`\n"
            return_str += f"`Contoh: {cmd}time {c_name} 2`"

            await dat.edit(return_str)
            return

    dtnow = dt.now(tz(time_zone)).strftime(d_form)

    if c_name != var.COUNTRY:
        await dat.edit(
            f"**Sekarang Tanggal** `{dtnow}` **di {c_name} ({time_zone} timezone.)**"
        )
        return

    if var.COUNTRY:
        await dat.edit(
            f"**Sekarang Tanggal** `{dtnow}` **di {var.COUNTRY} ({time_zone} timezone.)**"
        )
        return


CMD_HELP.update(
    {
        "timedate": f"**Plugin : **`timedate`\
        \n\n  »  **Perintah :** `{cmd}time` <country name/code> <timezone number>\
        \n  »  **Kegunaan : **Dapatkan waktu suatu negara. Jika suatu negara memiliki beberapa zona waktu, itu akan mencantumkan semuanya dan memungkinkan Anda memilihnya.\
        \n\n  »  **Perintah :** `{cmd}date` <country name/code> <timezone number>\
        \n  »  **Kegunaan : **Dapatkan tanggal suatu negara. Jika suatu negara memiliki beberapa zona waktu, itu akan mencantumkan semuanya dan memungkinkan Anda memilihnya.\
    "
    }
)
