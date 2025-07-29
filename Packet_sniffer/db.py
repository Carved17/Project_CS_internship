import sqlite3

conn = sqlite3.connect("packets.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS packets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    src_ip TEXT,
    dst_ip TEXT,
    proto INTEGER,
    src_port INTEGER,
    dst_port INTEGER,
    length INTEGER,
    flags TEXT
)
""")
conn.commit()

def log_packet(src_ip, dst_ip, proto, src_port, dst_port, length, flags):
    cur.execute("INSERT INTO packets (src_ip, dst_ip, proto, src_port, dst_port, length, flags) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (src_ip, dst_ip, proto, src_port, dst_port, length, flags))
    conn.commit()
