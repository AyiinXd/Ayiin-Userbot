# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for filter commands """


import codecs
import json
import os

import requests
from bs4 import BeautifulSoup as bs

from AyiinXd import CMD_HELP, Ayiin
from AyiinXd.events import ayiin_cmd

from . import cmd, var


@Ayiin.on(ayiin_cmd(outgoing=True, pattern=r"ts (.*)"))
async def gengkapak(e):
    await e.edit("`Harap tunggu, mengambil hasil...`")
    query = e.pattern_match.group(1)
    response = requests.get(f"https://api.sumanjay.cf/torrent/?query={query}")
    ts = json.loads(response.text)
    if ts != response.json():
        await e.edit("**Beberapa kesalahan terjadi**\n`Coba Lagi Nanti`")
        return
    listdata = ""
    run = 0
    while True:
        try:
            run += 1
            r1 = ts[run]
            list1 = f"<-----{run}----->\nNama: {r1['name']}\nPembibitan: {r1['seeder']}\nUkuran: {r1['size']}\nUmur: {r1['age']}\n<--Magnet Di Bawah-->\n{r1['magnet']}\n\n\n "
            listdata += list1
        except BaseException:
            break

    if not listdata:
        return await e.edit("**Kesalahan:** `Tidak ada hasil yang ditemukan`")

    tsfileloc = f"{var.TEMP_DOWNLOAD_DIRECTORY}/{query}.txt"
    with open(tsfileloc, "w+", encoding="utf8") as out_file:
        out_file.write(str(listdata))
    fd = codecs.open(tsfileloc, "r", encoding="utf-8")
    data = fd.read()
    key = (
        requests.post(
            "https://nekobin.com/api/documents",
            json={"content": data}
        ).json().get("result").get("key")
    )
    url = f"https://nekobin.com/raw/{key}"
    caption = (
        f"**Ini hasil kueri:** `{query}`\n\nDitempelkan ke: [Nekobin]({url})"
    )
    os.remove(tsfileloc)
    await e.edit(caption, link_preview=False)


def dogbin(magnets):
    counter = 0
    urls = []
    while counter != len(magnets):
        message = magnets[counter]
        url = "https://del.dog/documents"
        r = requests.post(url, data=message.encode("UTF-8")).json()
        url = f"https://del.dog/raw/{r['key']}"
        urls.append(url)
        counter += 1
    return urls


@Ayiin.on(ayiin_cmd(outgoing=True, pattern=r"tos(?: |$)(.*)"))
async def tor_search(event):
    if event.fwd_from:
        return
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }

    search_str = event.pattern_match.group(1)

    print(search_str)
    await event.edit(f"Mencari {search_str}....")
    if " " in search_str:
        search_str = search_str.replace(" ", "+")
        print(search_str)
        res = requests.get(
            "https://www.torrentdownloads.me/search/?new=1&s_cat=0&search="
            + search_str,
            headers,
        )

    else:
        res = requests.get(
            "https://www.torrentdownloads.me/search/?search=" +
            search_str,
            headers)

    source = bs(res.text, "lxml")
    urls = []
    magnets = []
    titles = []
    counter = 0
    for div in source.find_all("div", {"class": "grey_bar3 back_none"}):
        # print("https://www.torrentdownloads.me"+a['href'])
        try:
            title = div.p.a["title"]
            title = title[20:]
            titles.append(title)
            urls.append("https://www.torrentdownloads.me" + div.p.a["href"])
        except (KeyError, TypeError, AttributeError):
            pass
        if counter == 11:
            break
        counter += 1
    if not urls:
        await event.edit("Entah Kata Kunci dibatasi atau tidak ditemukan..")
        return

    print("Found URLS...")
    for url in urls:
        res = requests.get(url, headers)
        # print("URl: "+url)
        source = bs(res.text, "lxml")
        for div in source.find_all("div", {"class": "grey_bar1 back_none"}):
            try:
                mg = div.p.a["href"]
                magnets.append(mg)
            except Exception:
                pass
    print("Found Magnets...")
    shorted_links = dogbin(magnets)
    print("Dogged Magnets to del.dog...")
    msg = ""
    try:
        search_str = search_str.replace("+", " ")
    except BaseException:
        pass
    msg = f"**Kueri Penelusuran Torrent**\n`{search_str}`\n**Hasil**\n"
    counter = 0
    while counter != len(titles):
        msg = (
            msg
            + "⁍ [{}]".format(titles[counter])
            + "({})".format(shorted_links[counter])
            + "\n\n"
        )
        counter += 1
    await event.edit(msg, link_preview=False)


CMD_HELP.update(
    {
        "torrent": f"**Plugin : **`torrent`\
        \n\n  »  **Perintah :** `{cmd}ts` <search query>\
        \n  »  **Kegunaan : **Cari query torrent dan posting ke dogbin.\
        \n\n  »  **Perintah :** `{cmd}tos` <search query>\
        \n  »  **Kegunaan : **Cari magnet torrent dari query.\
    "
    }
)
