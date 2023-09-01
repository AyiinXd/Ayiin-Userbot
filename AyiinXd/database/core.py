# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinChats & t.me/AyiinChannel


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

import logging
import sqlite3

from config import var

logger = logging.getLogger(__name__)


execute_xd = """
CREATE TABLE IF NOT EXISTS blacklist_gcast(
    user_id INTEGER PRIMARY KEY,
    bl_gcast JSON
);
CREATE TABLE IF NOT EXISTS blacklist_filter(
    chat_id INTEGER,
    chat_title TEXT,
    trigger TEXT
);
CREATE TABLE IF NOT EXISTS bot_blacklist(
    user_id INTEGER PRIMARY KEY,
    first_name TEXT,
    username TEXT,
    reason TEXT,
    date DATETIME
);
CREATE TABLE IF NOT EXISTS bot_starter(
    user_id INTEGER PRIMARY KEY,
    first_name TEXT,
    date DATETIME,
    username TEXT
);
CREATE TABLE IF NOT EXISTS bot_pms(
    user_id INTEGER PRIMARY KEY,
    message_id INTEGER,
    first_name TEXT,
    reply_id INTEGER,
    logger_id INTEGER,
    result_id INTEGER
);
CREATE TABLE IF NOT EXISTS broadcast(
    keyword TEXT PRIMARY KEY,
    gcast_id JSON
);
CREATE TABLE IF NOT EXISTS chat_bot(
    chat_id INTEGER PRIMARY KEY,
    status TEXT
);
CREATE TABLE IF NOT EXISTS filters(
    chat_id INTEGER,
    trigger TEXT,
    string TEXT,
    msg_id TEXT
);
CREATE TABLE IF NOT EXISTS gbanned(
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    reason TEXT
);
CREATE TABLE IF NOT EXISTS gmuted_user(
    user_id INTEGER PRIMARY KEY,
    gmute_id JSON
);
CREATE TABLE IF NOT EXISTS log(
    chat_id INTEGER
);
CREATE TABLE IF NOT EXISTS muted_user(
    user_id INTEGER PRIMARY KEY,
    mute_id JSON
);
CREATE TABLE IF NOT EXISTS notes(
    chat_id INTEGER,
    keyword TEXT,
    reply TEXT,
    msg_id TEXT
);
CREATE TABLE IF NOT EXISTS permit_mode(
    mode
);
CREATE TABLE IF NOT EXISTS permit_message(
    permit_msg TEXT
);
CREATE TABLE IF NOT EXISTS permit_user(
    user_id JSON
);
CREATE TABLE IF NOT EXISTS sudoer(
    user_id JSON
);
CREATE TABLE IF NOT EXISTS variable(
    vars TEXT PRIMARY KEY,
    value TEXT
);
"""


class DatabaseXd:
    def __init__(self):
        self.conn: sqlite3.Connection = None
        self.path: str = var.DATABASE_PATH
        self.is_connected: bool = False

    def connect(self):
        """
        KANG COPAS GAUSAH MAIN HAPUS KONTOL
        Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
        """
        conn = sqlite3.connect(self.path)

        conn.executescript(execute_xd)

        conn.execute("VACUUM")

        conn.commit()

        conn.row_factory = sqlite3.Row

        self.conn = conn
        self.is_connected: bool = True

        logger.info("Database Anda Telah Terhubung.")

    def close(self):
        """
        KANG COPAS GAUSAH MAIN HAPUS KREDIT KONTOL
        Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
        """
        self.conn.close()

        self.is_connected: bool = False

        logger.info("Database Anda Telah Ditutup.")

    def get_conn(self) -> sqlite3.Connection:
        """
        KANG COPAS GAUSAH MAIN HAPUS KONTOL
        Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
        """
        if not self.is_connected:
            self.connect()

        return self.conn


db = DatabaseXd()
