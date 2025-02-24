def detect_anomalies(data):
    """
    Función simple para detectar anomalías en los datos.
    Por ejemplo, si la temperatura supera un umbral, se considera una anomalía.
    """
    # Puedes ajustar el umbral o agregar más condiciones según tus necesidades.
    if data.get("temperature", 0) > 80:
        return True
    return False
