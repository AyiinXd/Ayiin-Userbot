# Coded by KenHV
# Recode by @mrismanaziz
# FORM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import DeletePhotosRequest, UploadProfilePhotoRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import InputPhoto

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, DEVS, LOGS, STORAGE
from AyiinXd.ayiin import eor
from AyiinXd.ayiin import ayiin_cmd
from Stringyins import get_string

if not hasattr(STORAGE, "userObj"):
    STORAGE.userObj = False


@ayiin_cmd(pattern="clone ?(.*)", allow_sudo=False)
async def impostor(event):
    inputArgs = event.pattern_match.group(1)
    AyiinXd = ["@AyiinXd", "@ayiinxd"]
    if inputArgs in AyiinXd:
        await eor(event, get_string("ayiin_2"))
        await event.client.send_message("@AyiinXd", get_string("ayiin_3")
                                        )
        return
    xx = await eor(event, get_string("com_1"))
    if "restore" in inputArgs:
        await eor(event, get_string("clon_1"))
        if not STORAGE.userObj:
            return await xx.edit(get_string("clon_2"))
        await updateProfile(event, STORAGE.userObj, restore=True)
        return await xx.edit(get_string("clon_3"))
    if inputArgs:
        try:
            user = await event.client.get_entity(inputArgs)
        except BaseException:
            return await xx.edit(get_string("clon_4"))
        userObj = await event.client(GetFullUserRequest(user))
    elif event.reply_to_msg_id:
        replyMessage = await event.get_reply_message()
        if replyMessage.sender_id in DEVS:
            return await xx.edit(get_string("ayiin_2")
                                 )
        if replyMessage.sender_id is None:
            return await xx.edit("**Tidak dapat menyamar sebagai admin anonim 🥺**")
        userObj = await event.client(GetFullUserRequest(replyMessage.sender_id))
    else:
        return await xx.edit(get_string("clon_5").format(cmd))

    if not STORAGE.userObj:
        STORAGE.userObj = await event.client(GetFullUserRequest(event.sender_id))

    LOGS.info(STORAGE.userObj)
    await xx.edit(get_string("clon_8"))
    await updateProfile(event, userObj)
    await xx.edit(get_string("clon_7"))


async def updateProfile(event, userObj, restore=False):
    firstName = (
        "Deleted Account"
        if userObj.user.first_name is None
        else userObj.user.first_name
    )
    lastName = "" if userObj.user.last_name is None else userObj.user.last_name
    userAbout = userObj.about if userObj.about is not None else ""
    userAbout = "" if len(userAbout) > 70 else userAbout
    if restore:
        userPfps = await event.client.get_profile_photos("me")
        userPfp = userPfps[0]
        await event.client(
            DeletePhotosRequest(
                id=[
                    InputPhoto(
                        id=userPfp.id,
                        access_hash=userPfp.access_hash,
                        file_reference=userPfp.file_reference,
                    )
                ]
            )
        )
    else:
        try:
            userPfp = userObj.profile_photo
            pfpImage = await event.client.download_media(userPfp)
            await event.client(
                UploadProfilePhotoRequest(await event.client.upload_file(pfpImage))
            )
        except BaseException:
            pass
    await event.client(
        UpdateProfileRequest(about=userAbout, first_name=firstName, last_name=lastName)
    )


CMD_HELP.update(
    {
        "clone": f"**Plugin : **`clone`\
        \n\n  »  **Perintah :** `{cmd}clone` <reply/username/ID>\
        \n  »  **Kegunaan : **Untuk mengclone identitas dari username/ID Telegram yang diberikan.\
        \n\n  »  **Perintah :** `{cmd}clone restore`\
        \n  »  **Kegunaan : **Mengembalikan ke identitas asli anda.\
        \n\n  •  **NOTE :** `{cmd}clone restore` terlebih dahulu sebelum mau nge `{cmd}clone` lagi.\
    "
    }
)
