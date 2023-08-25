# Copyright (C) 2021 Catuserbot <https://github.com/sandy1709/catuserbot>
# Ported by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

import ast
import json
import re
import urllib.parse
from os import popen
from secrets import choice

import requests
from bs4 import BeautifulSoup
from humanize import naturalsize

from AyiinXd import CMD_HELP, LOGS
from AyiinXd.ayiin import ayiin_cmd, eod, eor

from . import cmd


@ayiin_cmd(pattern="direct(?: |$)([\\s\\S]*)")
async def direct_link_generator(event):
    textx = await event.get_reply_message()
    message = event.pattern_match.group(1)
    if not message:
        if textx:
            message = textx.text
        else:
            return await eod(
                event,
                f"**Gunakan:** `{cmd}direct url` **Bila butuh bantuan ketik** `{cmd}help direct`"
            )
    xxnx = await eor(event, "`Memproses...`")
    reply = ""
    links = re.findall(r"\bhttps?://.*\.\S+", message)
    if not links:
        await xxnx.edit("**Tidak ada Link URL yang ditemukan!**")
    for link in links:
        if "drive.google.com" in link:
            reply += gdrive(link)
        elif "zippyshare.com" in link:
            reply += zippy_share(link)
        elif "mega." in link:
            reply += mega_dl(link)
        elif "yadi.sk" in link:
            reply += yandex_disk(link)
        elif "cloud.mail.ru" in link:
            reply += cm_ru(link)
        elif "mediafire.com" in link:
            reply += mediafire(link)
        elif "sourceforge.net" in link:
            reply += sourceforge(link)
        elif "osdn.net" in link:
            reply += osdn(link)
        elif "github.com" in link:
            reply += github(link)
        elif "androidfilehost.com" in link:
            reply += androidfilehost(link)
        else:
            reply += re.findall(r"\bhttps?://(.*?[^/]+)",
                                link)[0] + "tidak didukung"
    await xxnx.edit(reply)


def gdrive(url: str) -> str:
    """GDrive direct links generator"""
    drive = "https://drive.google.com"
    try:
        link = re.findall(r"\bhttps?://drive\.google\.com\S+", url)[0]
    except IndexError:
        reply = "**Tidak ada link Google drive yang ditemukan**\n"
        return reply
    file_id = ""
    reply = ""
    if link.find("view") != -1:
        file_id = link.split("/")[-2]
    elif link.find("open?id=") != -1:
        file_id = link.split("open?id=")[1].strip()
    elif link.find("uc?id=") != -1:
        file_id = link.split("uc?id=")[1].strip()
    url = f"{drive}/uc?export=download&id={file_id}"
    download = requests.get(url, stream=True, allow_redirects=False)
    cookies = download.cookies
    try:
        # In case of small file size, Google downloads directly
        dl_url = download.headers["location"]
        if "accounts.google.com" in dl_url:  # non-public file
            reply += "**Link Tautan tidak bersifat publik!**\n"
            return reply
        name = "Direct Download Link"
    except KeyError:
        # In case of download warning page
        page = BeautifulSoup(download.content, "lxml")
        export = drive + page.find("a", {"id": "uc-download-link"}).get("href")
        name = page.find("span", {"class": "uc-name-size"}).text
        response = requests.get(
            export, stream=True, allow_redirects=False, cookies=cookies
        )
        dl_url = response.headers["location"]
        if "accounts.google.com" in dl_url:
            reply += "Link is not public!"
            return reply
    reply += f"[{name}]({dl_url})\n"
    return reply


def zippy_share(url: str) -> str:
    """ZippyShare direct links generator
    Based on https://github.com/LameLemon/ziggy"""
    reply = ""
    dl_url = ""
    try:
        link = re.findall(r"\bhttps?://.*zippyshare\.com\S+", url)[0]
    except IndexError:
        reply = "**Tidak ada link tautan ZippyShare yang ditemukan**\n"
        return reply
    session = requests.Session()
    base_url = re.search("http.+.com", link).group()
    response = session.get(link)
    page_soup = BeautifulSoup(response.content, "lxml")
    scripts = page_soup.find_all("script", {"type": "text/javascript"})
    for script in scripts:
        if "getElementById('dlbutton')" in script.text:
            url_raw = re.search(
                r"= (?P<url>\".+\" \+ (?P<math>\(.+\)) .+);", script.text
            ).group("url")
            math = re.search(
                r"= (?P<url>\".+\" \+ (?P<math>\(.+\)) .+);", script.text
            ).group("math")
            dl_url = url_raw.replace(math, '"' + str(ast.literal_eval(math)) + '"')
            break
    dl_url = base_url + ast.literal_eval(dl_url)
    name = urllib.parse.unquote(dl_url.split("/")[-1])
    reply += f"[{name}]({dl_url})\n"
    return reply


def yandex_disk(url: str) -> str:
    """Yandex.Disk direct links generator
    Based on https://github.com/wldhx/yadisk-direct"""
    reply = ""
    try:
        link = re.findall(r"\bhttps?://.*yadi\.sk\S+", url)[0]
    except IndexError:
        reply = "**Tidak link tautan Yandex.Disk ditemukan link tautan**\n"
        return reply
    api = "https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={}"
    try:
        dl_url = requests.get(api.format(link)).json()["href"]
        name = dl_url.split("filename=")[1].split("&disposition")[0]
        reply += f"[{name}]({dl_url})\n"
    except KeyError:
        reply += "**ERROR: File tidak ditemukan atau Batas download tercapai**\n"
        return reply
    return reply


def mega_dl(url: str) -> str:
    """MEGA.nz direct links generator
    Using https://github.com/tonikelope/megadown"""
    reply = ""
    try:
        link = re.findall(r"\bhttps?://.*mega.*\.nz\S+", url)[0]
    except IndexError:
        reply = "**Tidak ada link tautan MEGA.nz yang ditemukan**\n"
        return reply
    command = f"bin/megadown -q -m {link}"
    result = popen(command).read()
    try:
        data = json.loads(result)
        LOGS.info(data)
    except json.JSONDecodeError:
        reply += "**ERROR: Tidak dapat mengekstrak link**\n"
        return reply
    dl_url = data["url"]
    name = data["file_name"]
    size = naturalsize(int(data["file_size"]))
    reply += f"[{name} ({size})]({dl_url})\n"
    return reply


def cm_ru(url: str) -> str:
    """cloud.mail.ru direct links generator
    Using https://github.com/JrMasterModelBuilder/cmrudl.py"""
    reply = ""
    try:
        link = re.findall(r"\bhttps?://.*cloud\.mail\.ru\S+", url)[0]
    except IndexError:
        reply = "**Tidak ada link tautan cloud.mail.ru yang ditemukan**\n"
        return reply
    command = f"bin/cmrudl -s {link}"
    result = popen(command).read()
    result = result.splitlines()[-1]
    try:
        data = json.loads(result)
    except json.decoder.JSONDecodeError:
        reply += "**ERROR: Tidak dapat mengekstrak link tautan**\n"
        return reply
    dl_url = data["download"]
    name = data["file_name"]
    size = naturalsize(int(data["file_size"]))
    reply += f"[{name} ({size})]({dl_url})\n"
    return reply


def mediafire(url: str) -> str:
    """MediaFire direct links generator"""
    try:
        link = re.findall(r"\bhttps?://.*mediafire\.com\S+", url)[0]
    except IndexError:
        reply = "**Tidak ada link tautan MediaFire yang ditemukan**\n"
        return reply
    reply = ""
    page = BeautifulSoup(requests.get(link).content, "lxml")
    info = page.find("a", {"aria-label": "Download file"})
    dl_url = info.get("href")
    size = re.findall(r"\(.*\)", info.text)[0]
    name = page.find("div", {"class": "filename"}).text
    reply += f"[{name} {size}]({dl_url})\n"
    return reply


def sourceforge(url: str) -> str:
    """SourceForge direct links generator"""
    try:
        link = re.findall(r"\bhttps?://.*sourceforge\.net\S+", url)[0]
    except IndexError:
        reply = "**Tidak ada link tautan SourceForge yang ditemukan**\n"
        return reply
    file_path = re.findall(r"files([\s\S]*)/download", link)[0]
    reply = f"Mirrors untuk __{file_path.split('/')[-1]}__\n"
    project = re.findall(r"projects?/(.*?)/files", link)[0]
    mirrors = (
        f"https://sourceforge.net/settings/mirror_choices?"
        f"projectname={project}&filename={file_path}"
    )
    page = BeautifulSoup(requests.get(mirrors).content, "html.parser")
    info = page.find("ul", {"id": "mirrorList"}).findAll("li")
    for mirror in info[1:]:
        name = re.findall(r"\(([\s\S]*)\)", mirror.text.strip())[0]
        dl_url = (
            f'https://{mirror["id"]}.dl.sourceforge.net/project/{project}/{file_path}'
        )
        reply += f"[{name}]({dl_url}) "
    return reply


def osdn(url: str) -> str:
    """OSDN direct links generator"""
    osdn_link = "https://osdn.net"
    try:
        link = re.findall(r"\bhttps?://.*osdn\.net\S+", url)[0]
    except IndexError:
        reply = "**Tidak ada link tautan OSDN yang ditemukan**\n"
        return reply
    page = BeautifulSoup(
        requests.get(
            link,
            allow_redirects=True).content,
        "lxml")
    info = page.find("a", {"class": "mirror_link"})
    link = urllib.parse.unquote(osdn_link + info["href"])
    reply = f"Mirrors untuk __{link.split('/')[-1]}__\n"
    mirrors = page.find("form", {"id": "mirror-select-form"}).findAll("tr")
    for data in mirrors[1:]:
        mirror = data.find("input")["value"]
        name = re.findall(r"\(([\s\S]*)\)", data.findAll("td")[-1].text.strip())[0]
        dl_url = re.sub(r"m=([\s\S]*)&f", f"m={mirror}&f", link)
        reply += f"[{name}]({dl_url}) "
    return reply


def github(url: str) -> str:
    """GitHub direct links generator"""
    try:
        link = re.findall(r"\bhttps?://.*github\.com.*releases\S+", url)[0]
    except IndexError:
        reply = "**Tidak ada link tautan Rilis GitHub yang ditemukan**\n"
        return reply
    reply = ""
    dl_url = ""
    download = requests.get(url, stream=True, allow_redirects=False)
    try:
        dl_url = download.headers["location"]
    except KeyError:
        reply += "**ERROR: Tidak dapat mengekstrak link tautan**\n"
    name = link.split("/")[-1]
    reply += f"[{name}]({dl_url}) "
    return reply


def androidfilehost(url: str) -> str:
    """AFH direct links generator"""
    try:
        link = re.findall(r"\bhttps?://.*androidfilehost.*fid.*\S+", url)[0]
    except IndexError:
        reply = "**Tidak ada link tautan AFH yang ditemukan**\n"
        return reply
    fid = re.findall(r"\?fid=([\s\S]*)", link)[0]
    session = requests.Session()
    user_agent = useragent()
    headers = {"user-agent": user_agent}
    res = session.get(link, headers=headers, allow_redirects=True)
    headers = {
        "origin": "https://androidfilehost.com",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "user-agent": user_agent,
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "x-mod-sbb-ctype": "xhr",
        "accept": "*/*",
        "referer": f"https://androidfilehost.com/?fid={fid}",
        "authority": "androidfilehost.com",
        "x-requested-with": "XMLHttpRequest",
    }
    data = {
        "submit": "submit",
        "action": "getdownloadmirrors",
        "fid": f"{fid}"}
    mirrors = None
    reply = ""
    error = "**ERROR: Tidak dapat menemukan Mirror untuk link tautan**\n"
    try:
        req = session.post(
            "https://androidfilehost.com/libs/otf/mirrors.otf.php",
            headers=headers,
            data=data,
            cookies=res.cookies,
        )
        mirrors = req.json()["MIRRORS"]
    except (json.decoder.JSONDecodeError, TypeError):
        reply += error
    if not mirrors:
        reply += error
        return reply
    for item in mirrors:
        name = item["name"]
        dl_url = item["url"]
        reply += f"[{name}]({dl_url}) "
    return reply


def useragent():
    """
    useragent random setter
    """
    useragents = BeautifulSoup(
        requests.get(
            "https://developers.whatismybrowser.com/"
            "useragents/explore/operating_system_name/android/"
        ).content,
        "lxml",
    ).findAll("td", {"class": "useragent"})
    user_agent = choice(useragents)
    return user_agent.text


CMD_HELP.update(
    {
        "direct": f"**Plugin : **`direct`\
        \n\n  »  **Perintah :** `{cmd}direct` <url>\
        \n  »  **Kegunaan : **Balas tautan atau tempel URL untuk membuat tautan unduhan langsung.\
        \n\n  •  **Supported URL :** `Google Drive` - `Cloud Mail` - `Yandex.Disk` - `AFH` - `ZippyShare` - `MediaFire` - `SourceForge` - `OSDN` - `GitHub`\
    "
    }
)
