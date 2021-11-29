from Sqlite3Manager import UseSqlite3db
from sqlite3 import OperationalError


class AccountManager:

    _instance_count = 0

    def __init__(self, /, account, email, password, login=None):
        self.account = account
        self.email = email
        self.password = password
        self.login = str(login)
        self._id = self._instance_count
        self._new_instance_()

        try:
            with UseSqlite3db('Accounts.db') as cursor:
                cursor.execute('''CREATE TABLE accounts(ID, ACCOUNTS, EMAIL, PASSWORD, LOGIN)''')
        except OperationalError:
            pass

    def get_alldatas(self) -> tuple:
        return self._id, self.account, self.email, self.password, self.login

    def set_alldatas(self, **datas) -> None:
        for k in datas.keys():
            if k in self.__dict__.keys() and isinstance(datas[k], str):
                self.__dict__[k] = datas[k]
                continue
            self.__dict__['_id'] = int(datas['_id'])

        return None

    def save(self) -> None:
        _id, *rest = self.get_alldatas()
        with UseSqlite3db('Accounts.db') as cursor:
            if cursor.execute(f'SELECT ID FROM accounts WHERE ID={_id}').fetchone() is None:
                cursor.execute(f'''INSERT INTO accounts VALUES({_id}, ?, ?, ?, ?)''',
                               rest)
                return None
        raise OperationalError('this account has already been saved')

    def change(self, **kwargs) -> None:
        self.set_alldatas(**kwargs)
        _id, *rest = self.get_alldatas()
        with UseSqlite3db('Accounts.db') as cursor:
            cursor.execute(f'''UPDATE accounts SET ACCOUNTS=?, EMAIL=?, PASSWORD=?, LOGIN=? 
                               WHERE ID={_id}''', rest)
        return None

    def delete(self) -> None:
        with UseSqlite3db('Accounts.db') as cursor:
            cursor.execute(f'DELETE FROM accounts WHERE ID={self._id}')

    def show(self) -> 'record in the table':
        with UseSqlite3db('Accounts.db') as cursor:
            reg = cursor.execute(f'SELECT * FROM accounts WHERE ID={self._id}')
            return reg.fetchone()

    @classmethod
    def _new_instance_(cls):
        cls._instance_count += 1


def findacc(_id, accounts):
    for i, a in enumerate(accounts):
        if a.get_alldatas()[0] == _id:
            return i
    raise ValueError(f'{_id} not in acounts')
