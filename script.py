import requests
import json

url = "https://api.weatherlink.com/v1/NoaaExt.json?user=001D0AE0D724&pass=semiuncial4&apiToken=BB6FD1E154A74270A0A613E9C2CFAAEE"

try:
    response = requests.get(url, timeout=10)
    data = response.json()
    davis = data.get("davis_current_observation", {})
    
    # Importamos el mapeador secundario para evitar saturar el espacio
    import variables
    replacements = variables.generar_mapa(data, davis)

    with open("template.html", "r", encoding="utf-8") as f:
        html = f.read()

    for key, value in replacements.items():
        html = html.replace(key, str(value))

    with open("dashboard.html", "w", encoding="utf-8") as f:
        f.write(html)
        
    print("Dashboard generado correctamente en dashboard.html")

except Exception as e:
    print(f"Error procesando el script principal: {e}")
