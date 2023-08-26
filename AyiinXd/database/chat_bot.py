from .core import db

con = db.get_conn()


def is_chatbot(chat_id):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    cursor = con.execute(
        '''
        SELECT status FROM chat_bot WHERE chat_id = ?
        ''',
        (chat_id,)
    )
    try:
        on_off = cursor.fetchone()
        cursor.close()
        return on_off[0]
    except:
        return None


def set_chatbot(chat_id, status: bool = None):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    ok = is_chatbot(chat_id)
    if ok:
        get_status = True if status is not None else False
        con.execute(
            '''
            UPDATE chat_bot SET status = ? WHERE chat_id = ?
            ''',
            (get_status, chat_id)
        )
    else:
        get_status = True if status is not None else False
        con.execute(
            '''
            INSERT INTO chat_bot (chat_id, status) VALUES (?, ?)
            ''',
            (chat_id, get_status)
        )
    con.commit()
