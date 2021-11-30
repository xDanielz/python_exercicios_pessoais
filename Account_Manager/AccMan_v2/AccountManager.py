import os
from sqlite3 import OperationalError
from Sqlite3Manager import UseSqlite3db, cursor_exc


class AccountManager:
    def __init__(self, dbname):
        self.dbname = dbname

        try:
            with UseSqlite3db(self.dbname) as cursor:
                cursor.execute('''CREATE TABLE accounts_v2(ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                                  ACCOUNT, EMAIL, PASSWORD, USER)''')
        except OperationalError:
            pass

    def save(self, account, email, password, user):
        sql = '''INSERT INTO accounts_v2 (ACCOUNT, EMAIL, PASSWORD, USER) VALUES (?, ?, ?, ?)'''
        cursor_exc(self.dbname, sql, (account, email, password, user))

    def delete(self, _id):
        sql = f'''DELETE FROM accounts_v2 WHERE ID=?'''
        cursor_exc(self.dbname, sql, (_id,))

    def delete_all(self):
        sql = f'''DELETE FROM accounts_v2'''
        cursor_exc(self.dbname, '''UPDATE sqlite_sequence SET seq=0''')
        cursor_exc(self.dbname, sql)

    def change(self, _id, **kwargs):
        sql = '''UPDATE accounts_v2 SET '''
        keys = []
        values = []
        for k, v in kwargs.items():
            k = k.upper()
            if k in 'ACCOUNT EMAIL PASSWORD USER'.split():
                keys.append(f'{k}=?')
                values.append(v)
        sql += ', '.join(keys) + 'WHERE ID=?'
        cursor_exc(self.dbname, sql, (*values, _id))

    def show(self, _id):
        sql = '''SELECT * FROM accounts_v2 WHERE ID=%s''' % _id
        with UseSqlite3db(self.dbname) as cursor:
            data = cursor.execute(sql)
            return data.fetchone()

    def show_all(self):
        sql = '''SELECT * FROM accounts_v2'''
        with UseSqlite3db(self.dbname) as cursor:
            data = cursor.execute(sql)
            return data.fetchall()


def id_check(dbname: str, tablename: str):
    dbname = str(dbname)
    tablename = str(tablename)

    def func(_id):
        _id = int(_id)
        with UseSqlite3db(dbname) as cursor:
            regs = cursor.execute(f'''SELECT ID FROM {tablename}''')
            regs = [reg[0] for reg in regs.fetchall()]

        return _id in regs

    return func
