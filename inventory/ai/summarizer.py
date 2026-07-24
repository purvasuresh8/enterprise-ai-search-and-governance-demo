import sqlite3
from pathlib import Path

DATABASE = (
    Path(__file__)
    .parent.parent
    .joinpath("database", "inventory.db")
)


class InventorySummarizer:

    def generate_summary(self):

        conn = sqlite3.connect(DATABASE)

        cursor = conn.cursor()

        cursor.execute("""
        SELECT COUNT(*)
        FROM inventory
        """)

        total_products = cursor.fetchone()[0]

        cursor.execute("""
        SELECT SUM(quantity)
        FROM inventory
        """)

        total_units = cursor.fetchone()[0]

        conn.close()

        return {
            "summary": (
                f"Inventory contains "
                f"{total_products} products "
                f"with {total_units} total units."
            )
        }