import os
import requests
import json
import time
import hmac
import hashlib

# 1. Traer los secretos guardados de GitHub
API_KEY = os.environ.get("WEATHERLINK_API_KEY")
API_SECRET = os.environ.get("WEATHERLINK_API_SECRET")
STATION_ID = os.environ.get("WEATHERLINK_STATION_ID")

# Verificar que los secretos no estén vacíos
if not API_KEY or not API_SECRET or not STATION_ID:
    print("ERROR: Faltan los Secretos en la configuración de GitHub (Settings > Secrets).")
    exit(1)

print("Conectando correctamente con WeatherLink v2...")

# 2. Configurar parámetros obligatorios para la API v2 y su firma
t = int(time.time())
params_to_hash = {
    "api-key": API_KEY,
    "t": t,
    "station-id": STATION_ID
}

# Organizar los parámetros alfabéticamente (Requisito estricto de WeatherLink)
msg = ""
for k in sorted(params_to_hash.keys()):
    msg += k + str(params_to_hash[k])

# 3. Generar la firma digital (API Signature) requerida por WeatherLink
api_signature = hmac.new(
    API_SECRET.encode('utf-8'),
    msg.encode('utf-8'),
    hashlib.sha256
).hexdigest()

# 4. Dirección oficial de datos actuales de la API v2
url = "https://api.weatherlink.com/v2/current"

# 5. Parámetros finales que se envían en la petición
params = {
    "api-key": API_KEY,
    "t": t,
    "station-id": STATION_ID,
    "api-signature": api_signature
}

# 6. Hacer la llamada al servidor
response = requests.get(url, params=params)

# 7. Guardar los datos si la conexión es exitosa
if response.status_code == 200:
    datos_clima = response.json()
    
    with open("clima.json", "w", encoding="utf-8") as archivo:
        json.dump(datos_clima, archivo, indent=4, ensure_ascii=False)
        
    print("¡Éxito! Datos guardados correctamente en clima.json")
else:
    print(f"Error del servidor. Código de estado: {response.status_code}")
    print(response.text)
    exit(1)
