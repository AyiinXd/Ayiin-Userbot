from .core import db

con = db.get_conn()


def cek_is_braodcast(keyword):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    cursor = con.execute(
        '''
        SELECT gcast_id FROM broadcast WHERE keyword = ?
        ''',
        (keyword,)
    )
    try:
        list_ = cursor.fetchone()
        cursor.close()
        return list_[0]
    except:
        return []


def add_broadcast(keyword, chat_id):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    ok = cek_is_braodcast(keyword)
    if ok:
        xx = eval(ok)
        xx.append(chat_id)
        con.execute(
            '''
            UPDATE broadcast SET gcast_id = ? WHERE keyword = ?
            ''',
            (str(xx), keyword)
        )
    else:
        ok.append(chat_id)
        con.execute(
            '''
            INSERT INTO broadcast (keyword, gcast_id) VALUES (?, ?)
            ''', (str(keyword), str(ok))
        )
    con.commit()


def del_broadcast(keyword, chat_id):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    ok = cek_is_braodcast(keyword)
    x = eval(ok)
    x.remove(chat_id)
    con.execute("""UPDATE broadcast SET gcast_id = ? WHERE keyword = ?""", (str(x), keyword))
    con.commit()


def get_broadcast():
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    cursor = con.execute(
        '''
        SELECT * FROM broadcast
        '''
    )
    return cursor.fetchall()
