from kafka import KafkaProducer
import json
import time
import random
from src.config.settings import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC

# Configuración del productor de Kafka para sensores
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

def generate_sensor_data():
    """
    Simula datos de sensores con múltiples parámetros, como:
    - sensor_id: Identificador del sensor.
    - temperature: Temperatura medida.
    - humidity: Humedad medida.
    - vibration: Nivel de vibración.
    - timestamp: Marca de tiempo.
    """
    data = {
        "sensor_id": random.randint(1, 50),
        "temperature": round(random.uniform(15, 100), 2),
        "humidity": round(random.uniform(20, 80), 2),
        "vibration": round(random.uniform(0, 5), 2),
        "timestamp": time.time()
    }
    return data

def run_sensor_simulator():
    """Envía datos simulados de sensores a Kafka de forma continua."""
    while True:
        sensor_data = generate_sensor_data()
        producer.send(KAFKA_TOPIC, value=sensor_data)
        print("Enviado datos del sensor:", sensor_data)
        time.sleep(random.uniform(0.5, 2.0))  # Intervalo variable para simular datos irregulares

if __name__ == "__main__":
    run_sensor_simulator()
