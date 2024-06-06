from services.mysql import db


class BaseRepository:
    def __init__(self, table):
        self.table = table
        self.connect = db()

    def _findAll(self):
        try:
            sql = f"SELECT * FROM {self.table}"
            self.connect.execute(sql)
            return self.connect.fetchall()
        except Exception as ex:
            print(f"Error al ejecutar la consulta: {ex}")
            return None

    def _findOne(self, id):
        try:
            sql = f"SELECT * FROM {self.table} WHERE id = %s"
            self.connect.execute(sql, (id,))
            return self.connect.fetchone()
        except Exception as ex:
            print(f"Error al ejecutar la consulta: {ex}")
            return None

    def _save(self, data):
        try:
            fields = ", ".join(data.keys())
            placeholders = ", ".join(["%s"] * len(data))
            sql = f"INSERT INTO {self.table} ({fields}) VALUES ({placeholders})"
            self.connect.execute(sql, tuple(data.values()))
            self.connect.commit()
            return True
        except Exception as ex:
            print(f"Error al ejecutar la consulta: {ex}")
            return None

    def __close_connection(self):
        if self.connect:
            self.connect.close()
