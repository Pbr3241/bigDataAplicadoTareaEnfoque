# Configuración global del proyecto

# Servidores y tópico de Kafka
KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']  # Lista de brokers de Kafka
KAFKA_TOPIC = 'iot-data'                      # Tópico para los datos IoT

# Umbral para generar alerta en caso de temperaturas elevadas
ALERT_TEMPERATURE_THRESHOLD = 80

# Configuración para la API
API_HOST = "127.0.0.1"
API_PORT = 8000

# Configuración para la base de datos (ejemplo usando Cassandra)
CASSANDRA_HOSTS = ['127.0.0.1']   # Dirección(es) del/los nodo(s) de Cassandra
CASSANDRA_PORT = 9042             # Puerto por defecto de Cassandra
CASSANDRA_KEYSPACE = 'bigdata'    # Keyspace a utilizar para almacenar los datos
