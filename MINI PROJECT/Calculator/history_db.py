import sqlite3

def init_db():
    conn = sqlite3.connect('calc_history.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS history (operation TEXT, a REAL, b REAL, result REAL)")
    conn.commit()
    conn.close()

def log_to_db(op, a, b, result):
    conn = sqlite3.connect('calc_history.db')
    c = conn.cursor()
    c.execute("INSERT INTO history VALUES (?, ?, ?, ?)", (op, a, b, result))
    conn.commit()
    conn.close()