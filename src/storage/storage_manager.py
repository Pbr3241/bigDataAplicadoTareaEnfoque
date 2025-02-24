from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from src.config.settings import CASSANDRA_HOSTS, CASSANDRA_PORT, CASSANDRA_KEYSPACE

class CassandraManager:
    def __init__(self):
        # Conecta al cluster de Cassandra
        self.cluster = Cluster(CASSANDRA_HOSTS, port=CASSANDRA_PORT)
        self.session = self.cluster.connect()
        # Crea el keyspace si no existe y usa el keyspace
        self.create_keyspace()
        self.session.set_keyspace(CASSANDRA_KEYSPACE)
        # Crea la tabla de datos de sensores
        self.create_table()

    def create_keyspace(self):
        query = f"""
        CREATE KEYSPACE IF NOT EXISTS {CASSANDRA_KEYSPACE}
        WITH replication = {{'class': 'SimpleStrategy', 'replication_factor': 1}}
        """
        self.session.execute(query)

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS sensor_data (
            sensor_id int,
            timestamp timestamp,
            temperature float,
            humidity float,
            vibration float,
            PRIMARY KEY (sensor_id, timestamp)
        )
        """
        self.session.execute(query)

    def insert_data(self, data):
        """
        Inserta un registro de datos del sensor.
        Se asume que 'data' es un diccionario con las llaves:
        sensor_id, temperature, humidity, vibration y timestamp.
        """
        query = """
        INSERT INTO sensor_data (sensor_id, timestamp, temperature, humidity, vibration)
        VALUES (%s, toTimestamp(now()), %s, %s, %s)
        """
        # Puedes ajustar la inserción según si incluyes el campo timestamp o lo generas en Cassandra
        self.session.execute(query, (
            data["sensor_id"],
            data["temperature"],
            data["humidity"],
            data["vibration"]
        ))

    def close(self):
        self.cluster.shutdown()
