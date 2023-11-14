from src.repositories.abstract_repository import IRepository


class InverterRepository(IRepository):
    def __init__(self, connection_string):
        # initialize database connection
        self._connection_string = connection_string
        self._connection = db.connect(connection_string)

    def get_all(self):
        # query all records from database
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM inverter")
        results = cursor.fetchall()
        return results

    def get_by_id(self, id):
        # query record by id from database
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM inverter WHERE id=?", (id,))
        result = cursor.fetchone()
        return result if result is not None else None

    def create(self, inverter):
        # insert record into database
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO inverter(name) VALUES (?)", (inverter['name']))
        self._connection.commit()
        inverter['id'] = cursor.lastrowid
        return inverter

    def update(self, inverter):
        # update record in database
        cursor = self._connection.cursor()
        cursor.execute("UPDATE inverter SET name=? WHERE id=?", (inverter['name'], inverter['id']))
        self._connection.commit()
        return cursor.rowcount > 0

    def delete(self, id):
        # delete record from database
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM inverter WHERE id=?", (id,))
        self._connection.commit()
        return cursor.rowcount > 0