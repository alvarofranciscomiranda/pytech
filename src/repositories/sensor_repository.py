from src.repositories.abstract_repository import IRepository


class SensorRepository(IRepository):
    def __init__(self, engine):
        # initialize database connection
        self._connection = engine

    def get_all(self):
        # query all records from database
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM sensor")
        results = cursor.fetchall()
        return results

    def get_by_id(self, id):
        # query record by id from database
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM sensor WHERE id=?", (id,))
        result = cursor.fetchone()
        return result if result is not None else None

    def create(self, sensor):
        # insert record into database
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO sensor(farm_id, name, created_at) VALUES (?, ?, ?)",
                       (sensor.farm_id, sensor.name, sensor.created_at))
        self._connection.commit()
        sensor['id'] = cursor.lastrowid
        return sensor

    def update(self, sensor):
        # update record in database
        cursor = self._connection.cursor()
        cursor.execute("UPDATE sensor SET farm_id=?, name=?, created_at=? WHERE id=?",
                       (sensor.farm_id, sensor.name, sensor.created_at, sensor.id))
        self._connection.commit()
        return cursor.rowcount > 0

    def delete(self, id):
        # delete record from database
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM sensor WHERE id=?", (id,))
        self._connection.commit()
        return cursor.rowcount > 0