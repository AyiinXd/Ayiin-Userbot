from .core import db

conn = db.get_conn()


def add_filter(chat_id, trigger, string, msg_id):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    conn.execute(
        "INSERT INTO filters(chat_id, trigger, string, msg_id) VALUES(?, ?, ?, ?)",
        (chat_id, trigger, string, msg_id),
    )
    conn.commit()


def update_filter(chat_id, trigger, string, msg_id):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    conn.execute(
        "UPDATE filters SET trigger = ?, string = ?, msg_id = ? WHERE chat_id = ?",
        (trigger, string, msg_id, chat_id),
    )
    conn.commit()


def del_filter(chat_id, trigger):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    conn.execute(
        "DELETE from filters WHERE chat_id = ? AND trigger = ?", (chat_id, trigger)
    )
    conn.commit()


def get_all_filters(chat_id):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    cursor = conn.execute("SELECT * FROM filters WHERE chat_id = ?", (chat_id,))
    return cursor.fetchall()