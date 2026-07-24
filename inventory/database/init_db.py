import sqlite3
from pathlib import Path

db_path = Path("inventory.db")

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS inventory(
    id INTEGER PRIMARY KEY,
    product_name TEXT,
    quantity INTEGER,
    reorder_threshold INTEGER
)
""")

sample_data = [
    ("Laptops", 120, 30),
    ("Monitors", 80, 20),
    ("Keyboards", 300, 50),
    ("Docking Stations", 15, 10),
    ("Headsets", 5, 15)
]

cursor.executemany("""
INSERT INTO inventory(
product_name,
quantity,
reorder_threshold)
VALUES(?,?,?)
""", sample_data)

conn.commit()

conn.close()

print("Inventory database initialized.")