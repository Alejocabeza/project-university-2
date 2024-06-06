from services.mysql import db

class BaseRepository:
    def __init__(self, table):
        self.table = table
        self.connect = db()
        self.cursor = self.connect.cursor()

    def _findAll(self):
        try:
            sql = f"SELECT * FROM {self.table}"
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as ex:
            print(f"Error al ejecutar la consulta: {ex}")
            return None
        finally:
            self.__close_connection()

    def _findOne(self, id):
        try:
            sql = f"SELECT * FROM {self.table} WHERE id = %s"
            self.cursor.execute(sql, (id,))
            return self.cursor.fetchone()
        except Exception as ex:
            print(f"Error al ejecutar la consulta: {ex}")
            return None
        finally:
            self.__close_connection()

    def _save(self, data):
        try:
            fields = ", ".join(data.keys())
            placeholders = ", ".join(["%s"] * len(data))
            sql = f"INSERT INTO {self.table} ({fields}) VALUES ({placeholders})"
            self.cursor.execute(sql, tuple(data.values()))
            self.connect.commit()
            return True
        except Exception as ex:
            print(f"Error al ejecutar la consulta: {ex}")
            return None
        finally:
            self.__close_connection()

    def __close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connect:
            self.connect.close()
