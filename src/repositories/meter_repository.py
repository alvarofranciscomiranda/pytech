from src.repositories.abstract_repository import IRepository


class MeterRepository(IRepository):
    def __init__(self, connection_string):
        # initialize database connection
        self._connection_string = connection_string
        self._connection = db.connect(connection_string)

    def get_all(self):
        # query all records from database
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM meter")
        results = cursor.fetchall()
        return results

    def get_by_id(self, id):
        # query record by id from database
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM meter WHERE id=?", (id,))
        result = cursor.fetchone()
        return result if result is not None else None

    def create(self, meter):
        # insert record into database
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO meter(name) VALUES (?)", (meter['name']))
        self._connection.commit()
        meter['id'] = cursor.lastrowid
        return meter

    def update(self, meter):
        # update record in database
        cursor = self._connection.cursor()
        cursor.execute("UPDATE meter SET name=? WHERE id=?", (meter['name'], meter['id']))
        self._connection.commit()
        return cursor.rowcount > 0

    def delete(self, id):
        # delete record from database
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM meter WHERE id=?", (id,))
        self._connection.commit()
        return cursor.rowcount > 0