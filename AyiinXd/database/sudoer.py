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

def sudoer():
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    cursor = conn.execute(
        "SELECT user_id FROM sudoer"
    )
    try:
        row = cursor.fetchone()
        cursor.close()
        return row[0]
    except:
        return []


def add_sudo(user_id: int):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    x = sudoer()
    if x:
        xx = eval(x)
        xx.append(user_id)
        conn.execute("""UPDATE sudoer SET user_id = ?""", (str(xx), user_id))
    else:
        x.append(user_id)
        conn.execute("""INSERT INTO sudoer (user_id) VALUES(?)""", (str(x),))
    conn.commit()


def del_sudo(user_id: int):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    x = eval(sudoer())
    x.remove(user_id)
    conn.execute("""UPDATE sudoer SET user_id = ?""", (str(x),))
    conn.commit()
