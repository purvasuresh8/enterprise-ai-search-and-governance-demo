import sqlite3
from pathlib import Path
from statistics import mean

DATABASE = (
    Path(__file__)
    .parent.parent
    .joinpath("database", "inventory.db")
)


class AnomalyDetector:

    def detect(self):

        conn = sqlite3.connect(DATABASE)

        cursor = conn.cursor()

        cursor.execute("""
        SELECT product_name, quantity
        FROM inventory
        """)

        rows = cursor.fetchall()

        conn.close()

        quantities = [r[1] for r in rows]

        if not quantities:
            return []

        avg = mean(quantities)

        anomalies = []

        for name, quantity in rows:

            if quantity > avg * 2:
                anomalies.append({
                    "product": name,
                    "quantity": quantity,
                    "reason": "Unusual stock spike"
                })

            if quantity < avg * 0.25:
                anomalies.append({
                    "product": name,
                    "quantity": quantity,
                    "reason": "Potential stockout"
                })

        return anomalies