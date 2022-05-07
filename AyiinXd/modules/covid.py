# Copyright (C) 2020 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.

from covid import Covid

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, bot
from AyiinXd.events import ayiin_cmd
from Stringyins import get_string


@bot.on(ayiin_cmd(outgoing=True, pattern=r"covid (.*)"))
async def corona(event):
    await event.edit(get_string("com_1"))
    country = event.pattern_match.group(1)
    covid = Covid(source="worldometers")
    country_data = covid.get_status_by_country_name(country)
    if country_data:
        output_text = f"`⚠️Confirmed   : {country_data['confirmed']} (+{country_data['new_cases']})`\n"
        output_text += f"`☢️Active      : {country_data['active']}`\n"
        output_text += f"`🤕Critical    : {country_data['critical']}`\n"
        output_text += f"`😟New Deaths  : {country_data['new_deaths']}`\n\n"
        output_text += f"`⚰️Deaths      : {country_data['deaths']} (+{country_data['new_deaths']})`\n"
        output_text += f"`😔New Cases   : {country_data['new_cases']}`\n"
        output_text += f"`😇Recovered   : {country_data['recovered']}`\n"
        output_text += f"`🧪Total tests : {country_data['total_tests']}`\n\n"
        output_text += f"**Data provided by [Worldometer]**(https://www.worldometers.info/coronavirus/country/{country})"
    else:
        output_text = get_string("covid_2")

    await event.edit(get_string("covid_1").format(country, output_text))


@bot.on(ayiin_cmd(outgoing=True, pattern="covid$"))
async def corona(event):
    await event.edit(get_string("com_1"))
    country = "World"
    covid = Covid(source="worldometers")
    country_data = covid.get_status_by_country_name(country)
    if country_data:
        output_text = f"`⚠️Confirmed   : {country_data['confirmed']} (+{country_data['new_cases']})`\n"
        output_text += f"`☢️Active      : {country_data['active']}`\n"
        output_text += f"`🤕Critical    : {country_data['critical']}`\n"
        output_text += f"`😟New Deaths  : {country_data['new_deaths']}`\n\n"
        output_text += f"`⚰️Deaths      : {country_data['deaths']} (+{country_data['new_deaths']})`\n"
        output_text += f"`😔New Cases   : {country_data['new_cases']}`\n"
        output_text += f"`😇Recovered   : {country_data['recovered']}`\n"
        output_text += "`🧪Total tests : N/A`\n\n"
        output_text += f"**Data provided by **[Worldometer](https://www.worldometers.info/coronavirus/country/{country})"
    else:
        output_text = get_string("covid_2")

    await event.edit(get_string("covid_1").format(country, output_text))


CMD_HELP.update(
    {
        "covid": f"**Plugin : **`covid`\
        \n\n  »  **Perintah :** `{cmd}covid`\
        \n  »  **Kegunaan : **Memberikan Informasi semua data COVID-19 dari semua negara.\
        \n\n  »  **Perintah :** `{cmd}covid` <nama negara>\
        \n  »  **Kegunaan : **Memberikan Informasi tentang data COVID-19 dari negara.\
    "
    }
)
