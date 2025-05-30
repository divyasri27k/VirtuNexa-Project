
import sqlite3

def init_db():
    conn = sqlite3.connect("data/urls.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            long_url TEXT NOT NULL,
            short_code TEXT NOT NULL UNIQUE,
            click_count INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def save_url(long_url, short_code):
    conn = sqlite3.connect("data/urls.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO urls (long_url, short_code) VALUES (?, ?)", (long_url, short_code))
    conn.commit()
    conn.close()

def get_long_url(short_code):
    conn = sqlite3.connect("data/urls.db")
    cur = conn.cursor()
    cur.execute("SELECT long_url FROM urls WHERE short_code = ?", (short_code,))
    result = cur.fetchone()
    conn.close()
    return result[0] if result else None

def increment_clicks(short_code):
    conn = sqlite3.connect("data/urls.db")
    cur = conn.cursor()
    cur.execute("UPDATE urls SET click_count = click_count + 1 WHERE short_code = ?", (short_code,))
    conn.commit()
    conn.close()

def get_clicks(short_code):
    conn = sqlite3.connect("data/urls.db")
    cur = conn.cursor()
    cur.execute("SELECT click_count FROM urls WHERE short_code = ?", (short_code,))
    result = cur.fetchone()
    conn.close()
    return result[0] if result else 0

def short_exists(short_code):
    conn = sqlite3.connect("data/urls.db")
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM urls WHERE short_code = ?", (short_code,))
    exists = cur.fetchone()
    conn.close()
    return exists is not None
