from services.mysql import db


class BaseModel:
    """
    Clase base para la base de datos
    """

    def __init__(self, table):
        self.table = table
        self.connect = db

    def _save(self, data):
        """
        Crea un nuevo registro

        Args:
            data (dict): el diccionario con los datos

        Returns:
            boolean: True si el registro se crea correctamente
        """
        try:
            fields = ", ".join(data.keys())
            placeholders = ", ".join(["%s"] * len(data))
            sql = f"INSERT INTO {self.table} ({fields}) VALUES ({placeholders})"
            cursor = self.connect.cursor()
            cursor.execute(sql, tuple(data.values()))
            self.connect.commit()
            cursor.close()
            return True
        except Exception as ex:
            print(f"Error al ejecutar la consulta: {ex}")
            return None

    def _update(self, id, data):
        """
        Actualiza un registro

        Args:
            id (int): el identificador
            data (dict): el diccionario con los datos

        Returns:
            boolean: True si el registro se actualiza correctamente
        """
        try:
            fields = ", ".join([f"{key} = %s" for key in data.keys()])
            sql = f"UPDATE {self.table} SET {fields} WHERE id = {id}"
            cursor = self.connect.cursor()
            cursor.execute(sql, tuple(data.values()))
            self.connect.commit()
            cursor.close()
            return True
        except Exception as ex:
            print(f"Error al ejecutar la consulta: {ex}")
            return None

    def _find_one_by(self, filters):
        """
        Busca un registro

        Args:
            filters (dict): el diccionario con los filtros

        Returns:
            dict: el diccionario con los datos del registro
        """
        try:
            where_clause = " AND ".join([f"{key} = %s" for key in filters.keys()])
            sql = f"SELECT * FROM {self.table} WHERE {where_clause}"
            values = tuple(filters.values())
            cursor = self.connect.cursor(dictionary=True)
            cursor.execute(sql, values)
            result = cursor.fetchone()
            cursor.close()
            return result
        except Exception as ex:
            print(f"Error al ejecutar la consulta: {ex}")
            return None

    def _find_by(self, filters):
        """
        Busca un registro

        Args:
            filters (dict): el diccionario con los filtros

        Returns:
            dict: el diccionario con los datos del registro
        """
        try:
            where_clause = " AND ".join([f"{key} = %s" for key in filters.keys()])
            sql = f"SELECT * FROM {self.table} WHERE {where_clause}"
            values = tuple(filters.values())
            cursor = self.connect.cursor(dictionary=True)
            cursor.execute(sql, values)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as ex:
            print(f"Error al ejecutar la consulta: {ex}")
            return None

    def _remove(self, id):
        """
        Elimina un registro

        Args:
            id (int): el identificador

        Returns:
            boolean: True si el registro se elimina correctamente
        """
        try:
            sql = f"DELETE FROM {self.table} WHERE id = {id}"
            cursor = self.connect.cursor()
            cursor.execute(sql)
            result = self.connect.commit()
            cursor.close()
            return result
        except Exception as ex:
            print(f"Error al ejecutar la consulta: {ex}")
            return None

    def _find_all(self):
        """
        Busca todos los registros

        Returns:
            list: Lista con los registros
        """
        try:
            sql = f"SELECT * FROM {self.table} WHERE deleted_at IS NULL"
            cursor = self.connect.cursor(dictionary=True)
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as ex:
            print(f"Error al ejecutar la consulta: {ex}")
            return None
