from .core import db

conn = db.get_conn()


def cek_var():
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    cursor = conn.execute(
        '''
        SELECT * FROM variable
        '''
    )
    return cursor.fetchall()

def get_var(var):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    cur = conn.execute(
        '''
        SELECT value FROM variable WHERE vars = ?
        ''', (var,)
    )
    try:
        raw = cur.fetchone()
        cur.close()
        return raw[0]
    except:
        return None


def set_var(var, value):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    cek = get_var(var)
    if cek:
        conn.execute(
            '''
            UPDATE variable SET value = ? WHERE vars = ?
            ''', (value, var)
        )
    else:
        conn.execute(
            '''
            INSERT INTO variable (vars, value) VALUES (?,?)
            ''', (var, value)
        )
    conn.commit()


def del_var(var):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    conn.execute(
    """
    DELETE FROM variable WHERE vars = ?
    """, (var,)
    )
    conn.commit()
