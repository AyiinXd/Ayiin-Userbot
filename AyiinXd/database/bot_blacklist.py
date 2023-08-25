from .core import db

conn = db.get_conn()



# ========================×========================
#               BLACKLIST USER DATABASE
# ========================×========================
def check_is_black_list(user_id: int):
    """check if user_id is blacklisted"""
    cursor = conn.execute(
        '''
        SELECT * FROM bot_blacklist WHERE user_id = ?
        ''', (user_id,)
    )
    try:
        ok = cursor.fetchone()
        cursor.close()
        return ok
    except:
        return None


def add_user_to_bl(
    user_id: int,
    first_name: str,
    username: str,
    reason: str,
    date: str
):
    """add the user to the blacklist"""
    to_check = check_is_black_list(user_id)
    if not to_check:
        conn.execute(
            '''
            INSERT INTO bot_starter (
                user_id,
                first_name,
                username,
                reason,
                date
            )
            VALUES (?, ?, ?, ?, ?)
            ''',
            (user_id, first_name, username, reason, date)
        )
    else:
        conn.execute(
            '''
            UPDATE bot_starter 
            SET first_name = ?, username = ?, reason = ?, date = ?
            WHERE user_id = ?
            ''',
            (first_name, username, reason, date, user_id)
        )
    conn.commit()


def rem_user_from_bl(user_id: int):
    """remove the user from the blacklist"""
    conn.execute(
        '''
        DELETE FROM bot_blacklist WHERE user_id = ?
        ''', (user_id,)
    )


def get_all_bl_users():
    get = conn.execute(
        '''
        SELECT * FROM bot_blacklist
        '''
    )
    return get.fetchall()
