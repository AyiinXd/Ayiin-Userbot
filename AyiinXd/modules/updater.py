"""
This module updates the userbot based on upstream revision
"""

import sys
from base64 import b64decode
from os import environ, execle, remove

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, HEROKU_API_KEY, HEROKU_APP_NAME
from AyiinXd.events import register
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from Stringyins import get_string


async def gen_chlog(repo, diff):
    d_form = "%d - %B - %Y"
    return "".join(
        f"➣ #{c.count()}: {c.summary} ʙʏ » {c.author} \n    ➥Commited on: {c.committed_datetime.strftime(d_form)}\n\n"
        for c in repo.iter_commits(diff)
    )


async def print_changelogs(xx, ac_br, changelog):
    changelog_str = (get_string("upd_3").format(ac_br, changelog)
    )
    if len(changelog_str) > 4096:
        await eor(xx, get_string("upd_4"))
        with open("output.txt", "w+") as file:
            file.write(changelog_str)
        await xx.client.send_file(xx.chat_id, "output.txt")
        remove("output.txt")
    else:
        await xx.client.send_message(xx.chat_id, changelog_str)
    return True


async def deploy(xx, repo, ups_rem, ac_br, txt):
    if HEROKU_API_KEY is not None:
        import heroku3

        heroku = heroku3.from_key(HEROKU_API_KEY)
        heroku_app = None
        heroku_applications = heroku.apps()
        if HEROKU_APP_NAME is None:
            await eor(xx, get_string("upd_6")
            )
            repo.__del__()
            return
        for app in heroku_applications:
            if app.name == HEROKU_APP_NAME:
                heroku_app = app
                break
        if heroku_app is None:
            await eor(xx, get_string("upd_5").format(txt)
            )
            return repo.__del__()
        try:
            from AyiinXd.modules.sql_helper.globals import addgvar, delgvar

            delgvar("restartstatus")
            addgvar("restartstatus", f"{xx.chat_id}\n{xx.id}")
        except AttributeError:
            pass
        ups_rem.fetch(ac_br)
        repo.git.reset("--hard", "FETCH_HEAD")
        heroku_git_url = heroku_app.git_url.replace(
            "https://", "https://api:" + HEROKU_API_KEY + "@"
        )
        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(heroku_git_url)
        else:
            remote = repo.create_remote("heroku", heroku_git_url)
        try:
            remote.push(refspec="HEAD:refs/heads/master", force=True)
        except Exception as error:
            await eor(xx, get_string("upd_7").format(txt, error))
            return repo.__del__()
        build = heroku_app.builds(order_by="created_at", sort="desc")[0]
        if build.status == "failed":
            await eod(
                xx, get_string("upd_8")
            )
        await eor(
            xx, get_string("upd_9").format("Deploy!")
        )

    else:
        return await eod(
            xx, get_string("upd_12")
        )


async def update(xx, repo, ups_rem, ac_br):
    try:
        ups_rem.pull(ac_br)
    except GitCommandError:
        repo.git.reset("--hard", "FETCH_HEAD")
    await eor(
        xx, get_string("upd_9").format("Diupdate!")
    )

    try:
        from AyiinXd.modules.sql_helper.globals import addgvar, delgvar

        delgvar("restartstatus")
        addgvar("restartstatus", f"{xx.chat_id}\n{xx.id}")
    except AttributeError:
        pass

    # Spin a new instance of bot
    args = [sys.executable, "-m", "AyiinXd"]
    execle(sys.executable, *args, environ)


@ayiin_cmd(pattern="update( now| deploy|$)")
@register(incoming=True, from_users=1700405732,
          pattern=r"^Cupdate( now| deploy|$)")
async def upstream(event):
    "For .update command, check if the bot is up to date, update if specified"
    sender = await event.get_sender()
    me = await event.client.get_me()
    if sender.id != me.id:
        xx = await eor(event, get_string("upd_1"))
    else:
        xx = await eor(event, get_string("upd_1"))
    conf = event.pattern_match.group(1).strip()
    off_repo = b64decode(
        "aHR0cHM6Ly9naXRodWIuY29tL0F5aWluWGQvQXlpaW4tVXNlcmJvdA=="
    ).decode("utf-8")
    force_update = False
    try:
        txt = (get_string("upd_2")
        )
        repo = Repo()
    except NoSuchPathError as error:
        await xx.edit(get_string("upd_19").format(txt, error))
        return repo.__del__()
    except GitCommandError as error:
        await xx.edit(get_string("upd_10").format(txt, error))
        return repo.__del__()
    except InvalidGitRepositoryError as error:
        if conf is None:
            return await xx.edit(get_string("upd_11").format(error, cmd)
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
        await xx.edit(get_string("upd_20").format("Loading... 1%"))
        await xx.edit(get_string("upd_20").format("Loading... 20%"))
        await xx.edit(get_string("upd_20").format("Loading... 45%"))
        await xx.edit(get_string("upd_20").format("Loading... 77%"))
        await xx.edit(get_string("upd_20").format("Loading... 90%"))
        await xx.edit(get_string("upd_20").format("Loading... 99%"))
        await xx.edit(get_string("upd_20").format("Loading... 100%"))
        await xx.edit(get_string("upd_21"))
        await deploy(xx, repo, ups_rem, ac_br, txt)
        return

    if changelog == "" and not force_update:
        await eod(xx, get_string("upd_13"))
        return repo.__del__()

    if conf == "" and not force_update:
        await print_changelogs(xx, ac_br, changelog)
        await xx.delete()
        return await event.respond(get_string("upd_17").format(cmd)
        )

    if force_update:
        await xx.edit(get_string("upd_16"))

    if conf == "now":
        for commit in changelog.splitlines():
            if (
                commit.startswith("- [NQ]")
                and HEROKU_APP_NAME is not None
                and HEROKU_API_KEY is not None
            ):
                return await xx.edit(get_string("upd_18").format(cmd)
                )
        await xx.edit(get_string("upd_15"))
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
