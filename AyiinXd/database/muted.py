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
#                   MUTED DATABASE
# ========================×========================

def cek_mute(user_id: int):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    cursor = conn.execute(
        "SELECT mute_id FROM muted_user WHERE user_id = ?", (user_id,)
    )
    try:
        row = cursor.fetchone()
        cursor.close()
        return row[0]
    except:
        return []


def add_mute(user_id: int, target_id: int):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    x = cek_mute(user_id)
    if x:
        xx = eval(x)
        xx.append(target_id)
        conn.execute("""UPDATE muted_user SET mute_id = ? WHERE user_id = ?""", (str(xx), user_id))
    else:
        x.append(target_id)
        conn.execute("""INSERT INTO muted_user (user_id, mute_id) VALUES(?,?)""", (user_id, str(x)))
    conn.commit()


def del_mute(user_id: int, target_id: int):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    x = eval(cek_mute(user_id))
    if len(x) == 1:
        conn.execute("""DELETE FROM muted_user WHERE user_id = ?""", (user_id,))
    else:
        x.remove(target_id)
        conn.execute("""UPDATE muted_user SET mute_id = ? WHERE user_id = ?""", (str(x), user_id))
    conn.commit()


# ========================×========================
#               GLOBAL MUTED DATABASE
# ========================×========================

def cek_gmute(user_id: int):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    cursor = conn.execute(
        "SELECT gmute_id FROM gmuted_user WHERE user_id = ?", (user_id,)
    )
    try:
        row = cursor.fetchone()
        cursor.close()
        return row[0]
    except:
        return []


def add_gmute(user_id: int, target_id: int):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    x = cek_gmute(user_id)
    if x:
        xx = eval(x)
        xx.append(target_id)
        conn.execute("""UPDATE gmuted_user SET gmute_id = ? WHERE user_id = ?""", (str(xx), user_id))
    else:
        x.append(target_id)
        conn.execute("""INSERT INTO gmuted_user (user_id, gmute_id) VALUES(?,?)""", (user_id, str(x)))
    conn.commit()


def del_gmute(user_id: int, target_id: int):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    x = eval(cek_gmute(user_id))
    if len(x) == 1:
        conn.execute("""DELETE FROM gmuted_user WHERE user_id = ?""", (user_id,))
    else:
        x.remove(target_id)
        conn.execute("""UPDATE gmuted_user SET gmute_id = ? WHERE user_id = ?""", (str(x), user_id))
    conn.commit()
