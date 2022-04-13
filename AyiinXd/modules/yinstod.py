# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

from time import sleep
from secrets import choice

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiinxd.truthdare import Dare as d
from AyiinXd.ayiinxd.truthdare import Truth as t
from AyiinXd.utils import ayiin_cmd, edit_or_reply


Tod = ["Truth", "Dare"]


@ayiin_cmd(pattern=r"tod( truth| dare|$)")
async def truth_or_dare(tord):
    trod = tord.pattern_match.group(1).strip()
    troll = choice(Tod)
    if trod == "":
        await tord.edit(f"    __Truth Or Dare ???__\n\n"
                        f"__Didapatkan Secara Acak__\n"
                        f"**      »» {troll} ««**"
                        )

    if trod == "truth":
        Ayiin = await edit_or_reply(tord, "__Truth Or Dare__")
        sleep(1)
        trth = choice(t)
        await Ayiin.edit(f"__Mendapatkan Hasil Truth Tod__\n\n"
                         f"**»** __Truth__ :\n"
                         f"**»** __{trth}__")
        return

    if trod == "dare":
        Xd = await edit_or_reply(tord, "__Truth Or Dare__")
        sleep(1)
        dr = choice(d)
        await Xd.edit(f"__Mendapatkan Hasil Dare Tod__\n\n"
                      f"**»** __Dare__ :\n"
                      f"**»** __{dr}__"
                      )

        return


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "yinstod": f"**Plugin:** `yinstod`\
        \n\n  »  **Perintah :** `{cmd}tod`\
        \n  »  **Kegunaan :** __Mendapatkan Pilihan Secara Acak.__\
        \n\n  »  **Perintah :** `{cmd}tod <truth/dare>`\
        \n  »  **Kegunaan :** __Untuk Mendapatkan Truth or Dare Secara Acak.__\
    "
    }
)
