from .core import db

conn = db.get_conn()



# ========================×========================
#               GLOBAL BANNED DATABASE
# ========================×========================
def cek_gbanned(user_id: int):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    cursor = conn.execute(
        '''
        SELECT * FROM gbanned WHERE user_id = ?
        ''', (user_id,)
    )
    try:
        ok = cursor.fetchone()
        cursor.close()
        return ok
    except:
        return None


def add_gbanned(
    user_id: int,
    first_name: str,
    reason
):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    to_check = cek_gbanned(user_id)
    if not to_check:
        conn.execute(
            '''
            INSERT INTO gbanned (
                user_id,
                name,
                reason
            )
            VALUES (?, ?, ?)
            ''',
            (user_id, first_name, reason)
        )
    else:
        conn.execute(
            '''
            UPDATE gbanned 
            SET name = ?, reason = ?
            WHERE user_id = ?
            ''',
            (first_name, reason, user_id)
        )
    conn.commit()


def del_gbanned(user_id: int):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    conn.execute(
        '''
        DELETE FROM gbanned WHERE user_id = ?
        ''', (user_id,)
    )


def get_gbanned():
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    get = conn.execute(
        '''
        SELECT * FROM gbanned
        '''
    )
    return get.fetchall()
