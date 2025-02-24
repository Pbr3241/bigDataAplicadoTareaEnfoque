from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.storage.storage_manager import CassandraManager  # Usaremos CassandraManager para recuperar datos


app = FastAPI()
# Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringirlo a ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("App cargada correctamente")
@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Big Data Aplicado"}

@app.get("/sensor-data")
def get_sensor_data():
    """
    Este endpoint conecta a Cassandra, recupera los datos de la tabla sensor_data
    y devuelve los primeros 10 registros.
    """
    cassandra_manager = CassandraManager()
    query = "SELECT * FROM sensor_data LIMIT 10;"
    rows = cassandra_manager.session.execute(query)
    data = []
    for row in rows:
        # Convertimos cada fila a diccionario para que FastAPI lo devuelva en formato JSON.
        data.append(dict(row._asdict()))
    cassandra_manager.close()
    return data

# Puedes añadir más endpoints, por ejemplo, para alertas o análisis de anomalías.
