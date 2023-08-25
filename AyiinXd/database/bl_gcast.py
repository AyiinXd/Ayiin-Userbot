# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinChats & t.me/AyiinChannel


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

from .core import db

conn = db.get_conn()


# ========================×========================
#              BLACKLIST GCAST DATABASE
# ========================×========================

def cek_gcast(user_id: int):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    cursor = conn.execute(
        "SELECT bl_gcast FROM blacklist_gcast WHERE user_id = ?", (user_id,)
    )
    try:
        row = cursor.fetchone()
        cursor.close()
        return row[0]
    except:
        return []


def add_gcast(user_id: int, chat_id: int):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    x = cek_gcast(user_id)
    if x:
        xx = eval(x)
        xx.append(chat_id)
        conn.execute("""UPDATE blacklist_gcast SET bl_gcast = ? WHERE user_id = ?""", (str(xx), user_id))
    else:
        x.append(chat_id)
        conn.execute("""INSERT INTO blacklist_gcast (user_id, bl_gcast) VALUES(?,?)""", (user_id, str(x)))
    conn.commit()


def del_gcast(user_id: int, chat_id: int):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    x = eval(cek_gcast(user_id))
    x.remove(chat_id)
    conn.execute("""UPDATE blacklist_gcast SET bl_gcast = ? WHERE user_id = ?""", (str(x), user_id))
    conn.commit()
