import sqlite3
from pathlib import Path
from statistics import mean

DATABASE = (
    Path(__file__)
    .parent.parent
    .joinpath("database", "inventory.db")
)


class DemandPredictor:

    def predict(self):

        conn = sqlite3.connect(DATABASE)

        cursor = conn.cursor()

        cursor.execute("""
        SELECT quantity
        FROM inventory
        """)

        data = [row[0] for row in cursor.fetchall()]

        conn.close()

        if not data:
            return {
                "predicted_demand": 0
            }

        prediction = round(mean(data) * 1.10)

        return {
            "historical_average": round(mean(data), 2),
            "predicted_demand": prediction
        }
        