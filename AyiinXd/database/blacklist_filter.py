from .core import db

con = db.get_conn()


# ========================×========================
#              BLACKLIST FILTER DATABASE
# ========================×========================
def get_chat_blacklist(chat_id):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    cursor = con.execute(
        '''
        SELECT * FROM blacklist_filter WHERE chat_id = ?
        ''', (chat_id,)
    )
    try:
        ok = cursor.fetchone()
        cursor.close()
        return ok[0]
    except:
        return None


def add_to_blacklist(chat_id, chat_title, trigger):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    cek = get_chat_blacklist(chat_id)
    if cek:
        con.execute(
            '''
            UPDATE blacklist_filter SET chat_title = ?, trigger = ? WHERE chat_id = ?
            ''', 
            (chat_title, trigger, chat_id)
        )
    else:
        con.execute(
            '''
            INSERT INTO blacklist_filter (
                chat_id,
                chat_title,
                trigger
            )
            VALUES (?, ?, ?)
            ''',
            (chat_id, chat_title, trigger)
        )
    con.commit()


def rm_from_blacklist(chat_id, trigger):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    con.execute(
        '''
        DELETE FROM blacklist_filter WHERE chat_id = ? AND trigger = ?
        ''',
        (chat_id, trigger)
    )
    con.commit()


def get_all_chat_blacklist():
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    cursor = con.execute(
        '''
        SELECT * FROM blacklist_filter
        '''
    )
    return cursor.fetchall()
