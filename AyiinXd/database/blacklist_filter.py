from .core import db

con = db.get_conn()


# ========================×========================
#              BLACKLIST FILTER DATABASE
# ========================×========================
def get_chat_blacklist(chat_id):
    cursor = con.execute(
        '''
        SELECT * FROM blacklist_filter WHERE chat_id = ?
        ''', (chat_id,)
    )
    try:
        ok = cursor.fetchone()
        cursor.close()
        return ok
    except:
        return None


def add_to_blacklist(chat_id, chat_title, trigger):
    cek = get_chat_blacklist()
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
            VALUES (?, ?)
            ''',
            (chat_id, chat_title, trigger)
        )
    con.commit()


def rm_from_blacklist(chat_id, trigger):
    con.execute(
        '''
        DELETE FROM blacklist_filter WHERE chat_id = ? AND trigger = ?
        ''',
        (chat_id, trigger)
    )
    con.commit()


def get_all_chat_blacklist():
    cursor = con.execute(
        '''
        SELECT * FROM blacklist_filter
        '''
    )
    return cursor.fetchall()
