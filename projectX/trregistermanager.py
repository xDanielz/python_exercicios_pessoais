import mysql.connector


class TrRegisterManager:
    def __init__(self, **dbconfig):
        """Inicializado com as configurações para ser realizado a conexão,
        host, user, password e o banco de dados que será realizado a conexão"""
        try:
            self._conn = mysql.connector.connect(**dbconfig)
        except Exception as exc:
            print(exc)
        else:
            self._cursor = self._conn.cursor()

    def add_register(self, *values):
        _SQL = """INSERT INTO log
                  (motorista, id, veiculo, ponto_partida, destino_final, km, preco_com, valor_frete, obs)
                  VALUES
                  (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        self._cursor.execute(_SQL, *values)

    def del_register(self, id):
        _SQL = """DELETE FROM log
                  WHERE _id = {}"""
        _SQL = _SQL.format(id)
        self._cursor.execute(_SQL)

    def change_register(self, id, column, new_value):
        _SQL = """UPDATE log
                  SET {col} = {newvalue}
                  WHERE _id = {id}"""
        _SQL = _SQL.format(col=column, newvalue=new_value, id=id)
        self._cursor.execute(_SQL)

    def get_records(self) -> dict:
        _SQL = "SELECT * FROM log"
        self._cursor.execute(_SQL)
        contents = self._cursor.fetchall()
        return contents

    def get_date(self):
        _SQL = "SELECT (DATA) FROM log"
        self._cursor.execute(_SQL)
        contents = self._cursor.fetchall()
        months_days = dict()
        days = set()
        for d1 in contents:
            month = d1[0].month
            for d2 in contents:
                day = d2[0].day
                if d2[0].month == month:
                    days.add(day)
            months_days[month] = list(days)
            days.clear()
        return months_days

    def exit(self):
        self._conn.commit()
        self._cursor.close()
        self._conn.close()

