# Credits to Userge for Remove and Rename

import io
import os
import os.path
import re
import shutil
import time
from datetime import datetime
from os.path import basename, dirname, exists, isdir, isfile, join, relpath
from shutil import rmtree
from tarfile import TarFile, is_tarfile
from zipfile import ZIP_DEFLATED, BadZipFile, ZipFile, is_zipfile

from natsort import os_sorted
from rarfile import BadRarFile, RarFile, is_rarfile

from AyiinXd import CMD_HELP
from AyiinXd.ayiin import humanbytes, ayiin_cmd

from . import cmd, var


MAX_MESSAGE_SIZE_LIMIT = 4095


@ayiin_cmd(pattern="ls(?: |$)(.*)")
async def lst(event):
    if event.fwd_from:
        return
    cat = event.pattern_match.group(1)
    path = cat or os.getcwd()
    if not exists(path):
        await event.edit(
            f"Tidak ada direktori atau file dengan nama `{cat}` coba check lagi!"
        )
        return
    if isdir(path):
        if cat:
            msg = f"**Folder dan File di `{path}`** :\n\n"
        else:
            msg = "**Folder dan File di Direktori Saat Ini** :\n\n"
        lists = os.listdir(path)
        files = ""
        folders = ""
        for contents in os_sorted(lists):
            catpath = path + "/" + contents
            if not isdir(catpath):
                size = os.stat(catpath).st_size
                if contents.endswith((".mp3", ".flac", ".wav", ".m4a")):
                    files += "🎵 "
                elif contents.endswith((".opus")):
                    files += "🎙 "
                elif contents.endswith(
                    (".mkv", ".mp4", ".webm", ".avi", ".mov", ".flv")
                ):
                    files += "🎞 "
                elif contents.endswith(
                    (".zip", ".tar", ".tar.gz", ".rar", ".7z", ".xz")
                ):
                    files += "🗜 "
                elif contents.endswith(
                    (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".ico", ".webp")
                ):
                    files += "🖼 "
                elif contents.endswith((".exe", ".deb")):
                    files += "⚙️ "
                elif contents.endswith((".iso", ".img")):
                    files += "💿 "
                elif contents.endswith((".apk", ".xapk")):
                    files += "📱 "
                elif contents.endswith((".py")):
                    files += "🐍 "
                else:
                    files += "📄 "
                files += f"`{contents}` (__{humanbytes(size)}__)\n"
            else:
                folders += f"📁 `{contents}`\n"
        msg = msg + folders + files if files or folders else msg + "__empty path__"
    else:
        size = os.stat(path).st_size
        msg = "Rincian file yang diberikan:\n\n"
        if path.endswith((".mp3", ".flac", ".wav", ".m4a")):
            mode = "🎵 "
        elif path.endswith((".opus")):
            mode = "🎙 "
        elif path.endswith((".mkv", ".mp4", ".webm", ".avi", ".mov", ".flv")):
            mode = "🎞 "
        elif path.endswith((".zip", ".tar", ".tar.gz", ".rar", ".7z", ".xz")):
            mode = "🗜 "
        elif path.endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp", ".ico", ".webp")):
            mode = "🖼 "
        elif path.endswith((".exe", ".deb")):
            mode = "⚙️ "
        elif path.endswith((".iso", ".img")):
            mode = "💿 "
        elif path.endswith((".apk", ".xapk")):
            mode = "📱 "
        elif path.endswith((".py")):
            mode = "🐍 "
        else:
            mode = "📄 "
        time.ctime(os.path.getctime(path))
        time2 = time.ctime(os.path.getmtime(path))
        time3 = time.ctime(os.path.getatime(path))
        msg += f"**Lokasi :** `{path}`\n"
        msg += f"**Ikon :** `{mode}`\n"
        msg += f"**Ukuran :** `{humanbytes(size)}`\n"
        msg += f"**Waktu Modifikasi Terakhir :** `{time2}`\n"
        msg += f"**Waktu Terakhir Diakses :** `{time3}`"

    if len(msg) > MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(msg)) as out_file:
            out_file.name = "ls.txt"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=path,
            )
            await event.delete()
    else:
        await event.edit(msg)


@ayiin_cmd(pattern="rm(?: |$)(.*)")
async def rmove(event):
    """Removing Directory/File"""
    cat = event.pattern_match.group(1)
    if not cat:
        await event.edit("`Lokasi file tidak ada!`")
        return
    if not exists(cat):
        await event.edit("`Lokasi file tidak ada!`")
        return
    if isfile(cat):
        os.remove(cat)
    else:
        rmtree(cat)
    await event.edit(f"Dihapus `{cat}`")


@ayiin_cmd(pattern=r"rn ([^|]+)\|([^|]+)")
async def rname(event):
    """Renaming Directory/File"""
    cat = str(event.pattern_match.group(1)).strip()
    new_name = str(event.pattern_match.group(2)).strip()
    if not exists(cat):
        await event.edit(f"Jalur file : {cat} tidak ada!")
        return
    new_path = join(dirname(cat), new_name)
    shutil.move(cat, new_path)
    await event.edit(f"Diganti nama dari `{cat}` ke `{new_path}`")


@ayiin_cmd(pattern="zip (.*)")
async def zip_file(event):
    if event.fwd_from:
        return
    if not exists(var.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(var.TEMP_DOWNLOAD_DIRECTORY)
    input_str = event.pattern_match.group(1)
    path = input_str
    zip_name = ""
    if "|" in input_str:
        path, zip_name = path.split("|")
        path = path.strip()
        zip_name = zip_name.strip()
    if exists(path):
        await event.edit("`Zipping...`")
        start_time = datetime.now()
        if isdir(path):
            dir_path = path.split("/")[-1]
            if path.endswith("/"):
                dir_path = path.split("/")[-2]
            zip_path = join(var.TEMP_DOWNLOAD_DIRECTORY, dir_path) + ".zip"
            if zip_name:
                zip_path = join(var.TEMP_DOWNLOAD_DIRECTORY, zip_name)
                if not zip_name.endswith(".zip"):
                    zip_path += ".zip"
            with ZipFile(zip_path, "w", ZIP_DEFLATED) as zip_obj:
                for roots, _, files in os.walk(path):
                    for file in files:
                        files_path = join(roots, file)
                        arc_path = join(dir_path, relpath(files_path, path))
                        zip_obj.write(files_path, arc_path)
            end_time = (datetime.now() - start_time).seconds
            await event.edit(f"Zipped `{path}` ke `{zip_path}` dalam `{end_time}` detik."
            )
        elif isfile(path):
            file_name = basename(path)
            zip_path = join(var.TEMP_DOWNLOAD_DIRECTORY, file_name) + ".zip"
            if zip_name:
                zip_path = join(var.TEMP_DOWNLOAD_DIRECTORY, zip_name)
                if not zip_name.endswith(".zip"):
                    zip_path += ".zip"
            with ZipFile(zip_path, "w", ZIP_DEFLATED) as zip_obj:
                zip_obj.write(path, file_name)
            await event.edit(f"Zipped `{path}` ke `{zip_path}`")
    else:
        await event.edit("`404: Not Found`")


@ayiin_cmd(pattern="unzip (.*)")
async def unzip_file(event):
    if event.fwd_from:
        return
    if not exists(var.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(var.TEMP_DOWNLOAD_DIRECTORY)
    input_str = event.pattern_match.group(1)
    file_name = basename(input_str)
    output_path = var.TEMP_DOWNLOAD_DIRECTORY + \
        re.split("(.zip|.rar|.tar)", file_name)[0]
    if exists(input_str):
        start_time = datetime.now()
        await event.edit("`Unzipping...`")
        if is_zipfile(input_str):
            zip_type = ZipFile
        elif is_rarfile(input_str):
            zip_type = RarFile
        elif is_tarfile(input_str):
            zip_type = TarFile
        else:
            return await event.edit(
                "`Jenis file tidak didukung!`\n`Hanya Bisa ZIP, RAR dan TAR`"
            )
        try:
            with zip_type(input_str, "r") as zip_obj:
                zip_obj.extractall(output_path)
        except BadRarFile:
            return await event.edit("**Kesalahan:** `File RAR Rusak`")
        except BadZipFile:
            return await event.edit("**Kesalahan:** `File ZIP Rusak`")
        except BaseException as err:
            return await event.edit(f"**KESALAHAN : **`{str(err)}`")
        end_time = (datetime.now() - start_time).seconds
        await event.edit(f"Unzipped `{input_str}` ke `{output_path}` dalam `{end_time}` detik."
        )
    else:
        await event.edit("`404: Not Found`")


CMD_HELP.update(
    {
        "file": f"**Plugin : **`file`\
        \n\n  »  **Perintah :** `{cmd}ls`\
        \n  »  **Kegunaan : **Untuk Melihat Daftar file di dalam direktori server\
        \n\n  »  **Perintah :** `{cmd}rm` <directory/file>\
        \n  »  **Kegunaan : **Untuk Menghapus File atau folder yg tersimpan di server\
        \n\n  »  **Perintah :** `{cmd}rn` <directory/file> | <nama baru>\
        \n  »  **Kegunaan : **Untuk Mengubah nama file atau direktori\
        \n\n  »  **Perintah :** `{cmd}zip` <file/folder path> | <nama zip> (optional)\
        \n  »  **Kegunaan : **Untuk mengcompress file atau folder.\
        \n\n  »  **Perintah :** `{cmd}unzip` <path ke zip file>\
        \n  »  **Kegunaan : **Untuk mengekstrak file arsip.\
        \n  •  **NOTE : **Hanya bisa untuk file ZIP, RAR dan TAR!\
    "
    }
)
