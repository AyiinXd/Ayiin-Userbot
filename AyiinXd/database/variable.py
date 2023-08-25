from .core import db

conn = db.get_conn()


def cek_var():
    cursor = conn.execute(
        '''
        SELECT * FROM variable
        '''
    )
    return cursor.fetchall()

def get_var(var):
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
    conn.execute(
    """
    DELETE FROM variable WHERE vars = ?
    """, (var,)
    )
    conn.commit()
