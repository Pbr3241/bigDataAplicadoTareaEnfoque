from kafka import KafkaConsumer
import json
import os
os.environ["CASS_DRIVER_NO_C_EXTENSIONS"] = "1"
from src.config.settings import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC, ALERT_TEMPERATURE_THRESHOLD
from src.analysis.anomaly_detection import detect_anomalies
from src.storage.storage_manager import CassandraManager
# Configuración del consumidor de Kafka
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def run_consumer():
    print("Consumer iniciado. Esperando mensajes...")
    # Inicializa el administrador de Cassandra
    cassandra_manager = CassandraManager()
    try:
        for message in consumer:
            data = message.value
            print(f"Recibido: {data}")
            if detect_anomalies(data):
                print("¡Alerta: Se detectó una anomalía en los datos!")
            # Guarda los datos en Cassandra
            cassandra_manager.insert_data(data)
            print("Datos guardados")
    finally:
        cassandra_manager.close()

if __name__ == "__main__":
    run_consumer()
