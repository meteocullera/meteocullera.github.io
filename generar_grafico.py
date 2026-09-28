import json
import os
import matplotlib.pyplot as plt
from datetime import datetime

# 1. Cargar el dato actual recién descargado
with open('datos.json', 'r', encoding='utf-8') as f:
    datos_actuales = json.load(f)

act = datos_actuales['dades_act']
hora_actual = act['HORA']          # Ejemplo: "21:55"
temp_actual = float(act['TEMP'])   # Ejemplo: 24.8

# Archivo donde guardaremos el histórico de las últimas 24 horas
archivo_historico = 'historico_dia.json'

# 2. Resetear el archivo si es medianoche (comienzo del día)
if hora_actual == "00:00" or hora_actual == "00:05" or hora_actual == "00:10" or hora_actual == "00:15":
    historico = []
else:
    if os.path.exists(archivo_historico):
        with open(archivo_historico, 'r', encoding='utf-8') as f:
            try:
                historico = json.load(f)
            except:
                historico = []
    else:
        historico = []

# 3. Evitar duplicar la misma hora si la acción corre dos veces en el mismo tramo
if not historico or historico[-1]['hora'] != hora_actual:
    historico.append({'hora': hora_actual, 'temp': temp_actual})

# Guardar el registro actualizado
with open(archivo_historico, 'w', encoding='utf-8') as f:
    json.dump(historico, f, indent=4)

# 4. Extraer las listas para pintar el gráfico del día
horas = [punto['hora'] for punto in historico]
temperaturas = [punto['temp'] for punto in historico]

# 5. Diseñar el gráfico de evolución diaria
fig, ax = plt.subplots(figsize=(8, 4), dpi=150)
fig.patch.set_facecolor('none')
ax.set_facecolor('#f8fafc')

# Dibujar la línea de evolución con un degradado suave debajo si lo deseas
ax.plot(horas, temperaturas, color='#dc2626', marker='o', linewidth=2, markersize=4, label='Temperatura (°C)', zorder=3)

# Configuración visual
ax.set_title('Evolución de la Temperatura Hoy en Cullera', fontsize=12, fontweight='bold', pad=10, color='#1f2937')
ax.grid(axis='both', linestyle='--', alpha=0.4, zorder=0)

# Reducir el número de etiquetas en el eje X para que no se amontonen si hay muchos puntos
if len(horas) > 8:
    ax.set_xticks(horas[::4])  # Muestra una etiqueta cada hora (4 puntos de 15 min)
else:
    ax.set_xticks(horas)

ax.tick_params(axis='both', labelsize=9, colors='#4b5563')

for spine in ['top', 'right', 'left', 'bottom']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.savefig('grafico_dia.png', bbox_inches='tight', transparent=True)
plt.close()
