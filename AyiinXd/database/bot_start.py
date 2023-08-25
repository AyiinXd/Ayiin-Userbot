from .core import db

conn = db.get_conn()


def get_starter_details(user_id):
    cursor = conn.execute(
        '''
        SELECT * FROM bot_starter WHERE user_id = ?
        ''',
        (user_id,)
    )
    try:
        user = cursor.fetchone()
        cursor.close()
        return user
    except:
        return None


def add_starter_to_db(
    user_id,
    first_name,
    date,
    username,
):
    to_check = get_starter_details(user_id)
    if not to_check:
        conn.execute(
            '''
            INSERT INTO bot_starter (
                user_id,
                first_name,
                date,
                username
            )
            VALUES (?, ?, ?, ?)
            ''',
            (user_id, first_name, date, username)
        )
    else:
        conn.execute(
            '''
            UPDATE bot_starter 
            SET first_name = ?, date = ?, username = ?
            WHERE user_id = ?
            ''',
            (first_name, date, username, user_id)
        )
    conn.commit()


def del_starter_from_db(user_id):
    conn.execute(
        '''
        DELETE FROM bot_starter WHERE user_id = ?
        ''',
        (user_id,)
    )
    conn.commit()


def get_all_starters():
    cursor = conn.execute(
        '''
        SELECT * FROM bot_starter
        '''
    )
    return cursor.fetchall()
