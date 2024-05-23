from Services.Mysql.Database import db

class BaseRepository:
    def __init__(self, table):
        self.table = table
        self.connect = db()
        self.cursor = self.connect.cursor()

    def _findAll(self):
        try:
            sql = "SELECT * FROM %s" % self.table
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as ex:
            print("Error al ejecutar la consulta %s" % ex)
            return None
        finally:
            self.connect.close()
            self.cursor.close()

    def _findOne(self, id):
        try:
            sql = "SELECT * FROM %s WHERE id = %s" % (self.table, id)
            self.cursor.execute(sql)
            return self.cursor.fetchone()
        except Exception as ex:
            print("Error al ejecutar la consulta %s" % ex)
            return None
        finally:
            self.connect.close()
            self.cursor.close()

    def _save(self, data):
        try:
            field = ', '.join(data.keys())
            value = ', '.join(['%s'] * len(data))
            sql = f"INSERT INTO {self.table} ({field}) VALUES ({value})"
            self.cursor.execute(sql, tuple(data.values()))
            self.connect.commit()
            return True
        except Exception as ex:
            print("Error al ejecutar la consulta %s" % ex)
            return None
        finally:
            self.connect.close()
            self.cursor.close()

