import sqlite3

class Database:
    def __init__(self, db_name='transactions.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._create_tables()

    def _create_tables(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS transactions (
                                tx_id TEXT PRIMARY KEY,
                                sender TEXT,
                                receiver TEXT,
                                amount REAL,
                                timestamp TEXT
                              )""")
        self.connection.commit()

    # Additional methods for database operations can be added here

    def __del__(self):
        self.connection.close()