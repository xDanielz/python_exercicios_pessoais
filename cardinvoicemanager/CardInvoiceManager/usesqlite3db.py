import sqlite3


class UseSqlite3db:
    def __init__(self, *config):
        self.config = config

    def __enter__(self):
        self.conn = sqlite3.connect(*self.config)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
