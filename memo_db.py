import sqlite3
from datetime import datetime


DB_NAME = "goodday.db"


def connect_db():
    return sqlite3.connect(DB_NAME)


def create_table():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memos (
            date TEXT PRIMARY KEY,
            memo TEXT,
            updated_at TEXT
        )
    """)

    conn.commit()
    conn.close()


def get_memo(date):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT memo FROM memos WHERE date = ?",
        (date,)
    )

    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]

    return ""


def save_memo(date, memo):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO memos (date, memo, updated_at)
        VALUES (?, ?, ?)

        ON CONFLICT(date)
        DO UPDATE SET
            memo = excluded.memo,
            updated_at = excluded.updated_at
    """, (
        date,
        memo,
        datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()


def delete_memo(date):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM memos WHERE date = ?",
        (date,)
    )

    conn.commit()
    conn.close()

def has_memo(date):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT memo
        FROM memos
        WHERE date = ?
        """,
        (date,)
    )

    result = cursor.fetchone()

    conn.close()

    if result and result[0].strip():
        return True

    return False