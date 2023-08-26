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
#                 PM PERMIT DATABASE
# ========================×========================

# ========================×========================
#               PM PERMIT MODE DATABASE
# ========================×========================
def get_mode_permit():
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    cursor = conn.execute(
        "SELECT mode FROM permit_mode"
    )
    try:
        cur = cursor.fetchone()
        cursor.close()
        return cur[0]
    except:
        return None


def set_mode_permit(mode):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    cek = get_mode_permit()
    if cek and cek[0] is not None:
        conn.execute("""UPDATE permit_mode SET mode = ?""", (mode,))
    else:
        conn.execute("""INSERT INTO permit_mode (mode) VALUES(?)""", (mode,))
    conn.commit()


# ========================×========================
#               PM PERMIT USER DATABASE
# ========================×========================
def is_approved() -> list:
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    cursor = conn.execute(
        "SELECT user_id FROM permit_user"
    )
    try:
        row = cursor.fetchone()
        cursor.close()
        return row[0]
    except:
        return []


def approve(user_id: int):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    x = is_approved()
    if x:
        xx = eval(x)
        xx.append(user_id)
        conn.execute("""UPDATE permit_user SET user_id = ?""", (str(xx),))
    else:
        x.append(user_id)
        conn.execute("""INSERT INTO permit_user (user_id) VALUES(?)""", (str(x),))
    conn.commit()


def disapprove(user_id: int):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    x = eval(is_approved())
    if len(x) == 1:
        conn.execute("""DELETE FROM permit_user""")
    else:
        x.remove(user_id)
        conn.execute("""UPDATE permit_user SET user_id = ?""", (str(x), user_id))
    conn.commit()


# ========================×========================
#             PM PERMIT MESSAGE DATABASE
# ========================×========================
def get_permit_message():
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    cursor = conn.execute(
        "SELECT permit_msg FROM permit_message"
    )
    try:
        cur = cursor.fetchone()
        cursor.close()
        return cur[0]
    except:
        return None


def set_permit_message(permit):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    cek = get_permit_message()
    if cek:
        conn.execute("""UPDATE permit_message SET permit_msg = ?""", (permit,))
    else:
        conn.execute("""INSERT INTO permit_message (permit_msg) VALUES(?)""", (permit,))
    conn.commit()


def del_permit_message():
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    cek = get_permit_message()
    if cek:
        conn.execute("DELETE from permit_message")
        conn.commit()
        return True
    else:
        return False
