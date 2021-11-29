from CardInvoiceManager.usesqlite3db import *


class CardInvoiceManager:
    dbname = 'invoice_man.db'

    def addpeople(self, name):
        name = str(name)
        sql = '''CREATE TABLE %s(ID INTEGER PRIMARY KEY AUTOINCREMENT, DATE, INSTALLMENTS, VALUE)'''
        with UseSqlite3db(self.dbname) as c:
            c.execute(sql % name)

    def subpeople(self, name):
        name = str(name)
        sql = f'''DROP TABLE %s'''
        with UseSqlite3db(self.dbname) as c:
            c.execute(sql % name)

    def changepeople(self, name, newname):
        name = str(name)
        newname = str(newname)
        sql = '''ALTER TABLE {} RENAME TO {}'''.format(name, newname)
        with UseSqlite3db(self.dbname) as c:
            c.execute(sql)

    def viewpeoples(self):
        sql = '''SELECT * FROM sqlite_master WHERE type="table"'''
        with UseSqlite3db(self.dbname) as c:
            tablesinfo = c.execute(sql)
            tables = [tablename[1] for tablename in tablesinfo.fetchall() if tablename[1] != 'sqlite_sequence']
        return tables

    def addreg(self, name, date, installments, value):
        sql = f'''INSERT INTO %s (DATE, INSTALLMENTS, VALUE) VALUES (?, ?, ?)'''
        with UseSqlite3db(self.dbname) as c:
            c.execute(sql % name, (date, installments, value))

    def delreg(self, name, _id):
        sql = f'''DELETE FROM %s WHERE ID=?'''
        with UseSqlite3db(self.dbname) as c:
            c.execute(sql % name, (_id,))

    def delallreg(self, name):
        sql = '''TRUNCATE TABLE {}'''.format(name)
        with UseSqlite3db(self.dbname) as c:
            c.execute(sql)

    def viewinvoice(self, name):
        sql = '''SELECT * FROM {}'''.format(name)
        with UseSqlite3db(self.dbname) as c:
            d = c.execute(sql)
            return d.fetchall()

    def changerecords(self, name, _id, **kwargs):
        sql = f'''UPDATE %s SET'''
        for k in kwargs.keys():
            if k not in 'DATE INSTALLMENTS VALUE'.split():
                return
        sql += ', '.join(kwargs.keys()) + 'WHERE ID=?'
        with UseSqlite3db(self.dbname) as c:
            c.execute(sql % name, (*kwargs.values(), _id))
