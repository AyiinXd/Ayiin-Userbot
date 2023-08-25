from .core import db

con = db.get_conn()


def get_note(chat_id, keyword):
    cur = con.execute(
        '''
        SELECT * FROM notes WHERE chat_id = ? AND keyword = ?
        ''', (chat_id, keyword)
    )
    try:
        raw = cur.fetchone()
        cur.close()
        return raw
    except:
        return None


def get_notes(chat_id):
    cur = con.execute(
        '''
        SELECT * FROM notes WHERE chat_id = ?
        ''', (chat_id,)
    )
    return cur.fetchall()


def add_note(chat_id, keyword, reply, f_mesg_id):
    con.execute(
        '''
        INSERT INTO notes (
            chat_id,
            keyword,
            reply,
            msg_id
        )
        VALUES (?, ?, ?, ?)
        ''',
        (chat_id, keyword, reply, f_mesg_id)
    )
    con.commit()


def update_note(chat_id, keyword, reply, f_mesg_id):
    con.execute(
        '''
        UPDATE notes 
        SET reply = ?, msg_id = ? 
        WHERE chat_id = ? AND keyword = ?
        ''',
        (reply, f_mesg_id, chat_id, keyword)
    )
    con.commit()


def rm_note(chat_id, keyword):
    con.execute(
        '''
        DELETE FROM notes WHERE chat_id = ? AND keyword = ?
        ''',
        (chat_id, keyword)
    )
