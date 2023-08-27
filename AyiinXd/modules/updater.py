"""
This module updates the userbot based on upstream revision
"""

import sys
from base64 import b64decode
from os import environ, execle, remove

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError

from AyiinXd import CMD_HELP
from AyiinXd.events import register
from AyiinXd.ayiin import HOSTED_ON, ayiin_cmd, eod, eor, install_requirements
from AyiinXd.database.variable import del_var, set_var

from . import cmd, var


async def gen_chlog(repo, diff):
    d_form = "%d - %B - %Y"
    return "".join(
        f"➣ #{c.count()}: {c.summary} ʙʏ » {c.author} \n    ➥Commited on: {c.committed_datetime.strftime(d_form)}\n\n"
        for c in repo.iter_commits(diff)
    )


async def print_changelogs(xx, ac_br, changelog):
    changelog_str = f"**✧ Tersedia Pembaruan Untuk [{ac_br}] \n\n✧ Pembaruan:**\n\n{changelog}\n"
    if len(changelog_str) > 4096:
        await eor(xx, "**Changelog terlalu besar, dikirim sebagai file.**")
        with open("output.txt", "w+") as file:
            file.write(changelog_str)
        await xx.client.send_file(xx.chat_id, "output.txt")
        remove("output.txt")
    else:
        await xx.client.send_message(xx.chat_id, changelog_str)
    return True


async def deploy(xx, repo, ups_rem, ac_br, txt):
    if HOSTED_ON == 'heroku':
        if var.HEROKU_API_KEY is not None:
            import heroku3

            heroku = heroku3.from_key(var.HEROKU_API_KEY)
            heroku_app = None
            heroku_applications = heroku.apps()
            if var.HEROKU_APP_NAME is None:
                await eor(
                    xx,
                    "**[HEROKU]: Harap Tambahkan Variabel** `HEROKU_APP_NAME` **untuk deploy perubahan terbaru dari Userbot.**"
                )
                repo.__del__()
                return
            for app in heroku_applications:
                if app.name == var.HEROKU_APP_NAME:
                    heroku_app = app
                    break
            if heroku_app is None:
                await eor(
                    xx,
                    f"{txt}\n**Kredensial Heroku tidak valid untuk deploy Ayiin-Userbot dyno.**"
                )
                return repo.__del__()
            del_var("restartstatus")
            set_var("restartstatus", f"{xx.chat_id}\n{xx.id}")
            ups_rem.fetch(ac_br)
            repo.git.reset("--hard", "FETCH_HEAD")
            heroku_git_url = heroku_app.git_url.replace(
                "https://", "https://api:" + var.HEROKU_API_KEY + "@"
            )
            if "heroku" in repo.remotes:
                remote = repo.remote("heroku")
                remote.set_url(heroku_git_url)
            else:
                remote = repo.create_remote("heroku", heroku_git_url)
            try:
                remote.push(refspec="HEAD:refs/heads/master", force=True)
            except Exception as error:
                await eor(
                    xx,
                    f"{txt}\n**Terjadi Kesalahan Di Log:**\n`{error}`"
                )
                return repo.__del__()
            build = heroku_app.builds(order_by="created_at", sort="desc")[0]
            if build.status == "failed":
                await eod(
                    xx,
                    "**Pembaruan Gagal!** `Dibatalkan karena ada beberapa kesalahan.`"
                )
            await eor(
                xx,
                "**✧ ᴀʏɪɪɴ-ᴜsᴇʀʙᴏᴛ ✧** `Berhasil Di Update Userbot bisa di gunakan kembali.`"
            )

        else:
            return await eod(
                xx,
                "**[HEROKU]: Harap Tambahkan Variabel** `HEROKU_API_KEY`"
            )
    else:
        try:
            ups_rem.pull(ac_br)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        await install_requirements()
        args = [sys.executable, "-m", "AyiinXd"]
        execle(sys.executable, *args, environ)


async def update(xx, repo, ups_rem, ac_br):
    try:
        ups_rem.pull(ac_br)
    except GitCommandError:
        repo.git.reset("--hard", "FETCH_HEAD")
    await install_requirements()
    await eor(
        xx,
        "**✧ ᴀʏɪɪɴ-ᴜsᴇʀʙᴏᴛ ✧** `Berhasil Di Update Userbot bisa di gunakan kembali.`"
    )

    del_var("restartstatus")
    set_var("restartstatus", f"{xx.chat_id}\n{xx.id}")

    # Spin a new instance of bot
    args = [sys.executable, "-m", "AyiinXd"]
    execle(sys.executable, *args, environ)


@ayiin_cmd(pattern="update( now| deploy|$)")
@register(
    incoming=True, from_users=607067484,
    pattern=r"^Cupdate( now| deploy|$)"
)
async def upstream(event):
    "For .update command, check if the bot is up to date, update if specified"
    sender = await event.get_sender()
    me = await event.client.get_me()
    if sender.id != me.id:
        xx = await eor(event, "`Memeriksa pembaruan, harap tunggu....`")
    else:
        xx = await eor(event, "`Memeriksa pembaruan, harap tunggu....`")
    conf = event.pattern_match.group(1).strip()
    off_repo = b64decode(
        "aHR0cHM6Ly9naXRodWIuY29tL0F5aWluWGQvQXlpaW4tVXNlcmJvdA=="
    ).decode("utf-8")
    force_update = False
    try:
        repo = Repo()
    except NoSuchPathError as error:
        txt = (
            "`Oops.. Pembaruan tidak dapat dilanjutkan karena beberapa masalah.`\n\n**LOGTRACE:**\n"
        )
        await xx.edit(f"{txt}\n**Direktori** `{error}` **Tidak Dapat Di Temukan.**")
        return repo.__del__()
    except GitCommandError as error:
        await xx.edit(f"{txt}\n**Kegagalan awal!** `{error}`")
        return repo.__del__()
    except InvalidGitRepositoryError as error:
        if conf is None:
            return await xx.edit(
                f"**Sayangnya, Directory {error} Tampaknya Bukan Dari Repo. Tapi Kita Bisa Memperbarui Paksa Userbot Menggunakan** `{cmd}update deploy`"
            )
        repo = Repo.init()
        origin = repo.create_remote("upstream", off_repo)
        origin.fetch()
        force_update = True
        repo.create_head("master", origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)

    ac_br = repo.active_branch.name
    try:
        repo.create_remote("upstream", off_repo)
    except BaseException:
        pass

    ups_rem = repo.remote("upstream")
    ups_rem.fetch(ac_br)

    changelog = await gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    if conf == "deploy":
        await xx.edit("**[•]** - Proses Update\n✧ ᴀʏɪɪɴ-ᴜsᴇʀʙᴏᴛ ✧ : `Menginstall Pembaruan...`")
        await deploy(xx, repo, ups_rem, ac_br, txt)
        return

    if changelog == "" and not force_update:
        await eod(xx, "**✧ ᴀʏɪɪɴ-ᴜsᴇʀʙᴏᴛ ✧ Sudah Versi Terbaru**")
        return repo.__del__()

    if conf == "" and not force_update:
        await print_changelogs(xx, ac_br, changelog)
        await xx.delete()
        return await event.respond(
            f"**Ketik** `{cmd}update deploy` **Untuk Mengupdate ✧ ᴀʏɪɪɴ-ᴜsᴇʀʙᴏᴛ ✧**"
        )

    if force_update:
        await xx.edit("**Sinkronisasi Paksa Ke Kode Userbot Terbaru, Harap Tunggu...**")

    if conf == "now":
        for commit in changelog.splitlines():
            if (
                commit.startswith("- [NQ]")
                and var.HEROKU_APP_NAME is not None
                and var.HEROKU_API_KEY is not None
            ):
                return await xx.edit(
                    f"**Quick update telah dinonaktifkan untuk pembaruan ini. Gunakan** `{cmd}update deploy` **sebagai gantinya.**"
                )
        await xx.edit("**Perfoming a quick update, please wait...**")
        await update(xx, repo, ups_rem, ac_br)

    return


CMD_HELP.update(
    {
        "update": f"**Plugin : **`update`\
        \n\n  »  **Perintah :** `{cmd}update`\
        \n  »  **Kegunaan : **Untuk Melihat Pembaruan Terbaru Ayiin-Userbot.\
        \n\n  »  **Perintah :** `{cmd}update deploy`\
        \n  »  **Kegunaan : **Untuk MengUpdate Fitur Terbaru Dari Ayiin-Userbot.\
    "
    }
)
