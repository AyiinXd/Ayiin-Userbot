from .core import db

conn = db.get_conn()


# ========================×========================
#               PM PERMIT USER DATABASE
# ========================×========================
def is_approved_log(chat_id):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    cursor = conn.execute(
        "SELECT chat_id FROM log WHERE chat_id = ?", (chat_id,)
    )
    try:
        row = cursor.fetchone()
        cursor.close()
        return row[0]
    except:
        return None


def approve_log(chat_id: int):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    x = is_approved_log(chat_id)
    if x:
        conn.execute("""UPDATE log SET chat_id = ?""", (chat_id,))
    else:
        conn.execute("""INSERT INTO log (chat_id) VALUES(?)""", (chat_id,))
    conn.commit()


def disapprove_log(chat_id: int):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    x = is_approved_log(chat_id)
    if x:
        conn.execute("""DELETE FROM log""")
    conn.commit()

