from services.mysql import db


class BaseRepository:
    """
        Clase base para la base de datos
    """
    def __init__(self, table):
        self.table = table
        self.connect = db

    def _save(self, data):
        try:
            fields = ", ".join(data.keys())
            placeholders = ", ".join(["%s"] * len(data))
            sql = f"INSERT INTO {self.table} ({fields}) VALUES ({placeholders})"
            cursor = self.connect.cursor()
            cursor.execute(sql, tuple(data.values()))
            result = self.connect.commit()
            cursor.close()
            return result
        except Exception as ex:
            print(f"Error al ejecutar la consulta: {ex}")
            return None

    def _update(self, id, data):
        try:
            fields = ", ".join([f"{key} = %s" for key in data.keys()])
            sql = f"UPDATE {self.table} SET {fields} WHERE id = {id}"
            cursor = self.connect.cursor()
            cursor.execute(sql, tuple(data.values()))
            result = self.connect.commit()
            cursor.close()
            return result
        except Exception as ex:
            print(f"Error al ejecutar la consulta: {ex}")
            return None
