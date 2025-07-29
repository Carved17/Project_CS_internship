import sqlite3
import time

def detect_port_scanning(threshold=20, window_sec=10):
    conn = sqlite3.connect("packets.db")
    cur = conn.cursor()
    cur.execute("""
    SELECT src_ip, COUNT(DISTINCT dst_port) as port_count
    FROM packets
    WHERE timestamp > datetime('now', ?)
    GROUP BY src_ip
    HAVING port_count > ?
    """, (f'-{window_sec} seconds', threshold))

    return cur.fetchall()
