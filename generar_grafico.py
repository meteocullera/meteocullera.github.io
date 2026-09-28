import json
import matplotlib.pyplot as plt

# 1. Cargar los datos del JSON recién descargado
with open('datos.json', 'r', encoding='utf-8') as f:
    datos = json.load(f)

dia = datos['dades_dia']
mes = datos['dades_mes']
any_meteo = datos['dades_any']

# 2. Preparar los datos convirtiéndolos a números flotantes
categorias = ['Hoy', 'Este Mes', 'Este Año']
maximas = [float(dia['TMax_d']), float(mes['TMax_m']), float(any_meteo['TMax_a'])]
minimas = [float(dia['TMin_d']), float(mes['TMin_m']), float(any_meteo['TMin_a'])]

# 3. Configurar el estilo del gráfico
fig, ax = plt.subplots(figsize=(7, 4.5), dpi=150)
fig.patch.set_facecolor('none')  # Fondo exterior transparente
ax.set_facecolor('#f8fafc')      # Fondo del gráfico gris muy claro

x = range(len(categorias))
width = 0.35  # Ancho de las barras

# Dibujar las barras de máximas y mínimas
barras_max = ax.bar([i - width/2 for i in x], maximas, width, label='Temp. Máxima', color='#dc2626', edgecolor='none', zorder=3)
barras_min = ax.bar([i + width/2 for i in x], minimas, width, label='Temp. Mínima', color='#2563eb', edgecolor='none', zorder=3)

# Añadir las etiquetas de texto con los grados encima de cada barra
for barra in barras_max:
    height = barra.get_height()
    ax.annotate(f'{height}°C', xy=(barra.get_x() + barra.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9, fontweight='bold', color='#1f2937')

for barra in barras_min:
    height = barra.get_height()
    ax.annotate(f'{height}°C', xy=(barra.get_x() + barra.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9, fontweight='bold', color='#1f2937')

# Personalización de ejes y diseño
ax.set_title('Rangos de Temperatura en Cullera', fontsize=14, fontweight='bold', pad=15, color='#1f2937')
ax.set_xticks(x)
ax.set_xticklabels(categorias, fontsize=11, fontweight='600', color='#4b5563')
ax.set_ylabel('Temperatura (°C)', fontsize=11, color='#4b5563')
ax.grid(axis='y', linestyle='--', alpha=0.5, zorder=0)

# Limpiar bordes innecesarios
for spine in ['top', 'right', 'left', 'bottom']:
    ax.spines[spine].set_visible(False)

ax.legend(frameon=True, facecolor='#ffffff', edgecolor='none', loc='upper left')

# Ajustar y guardar la imagen de forma estática
plt.tight_layout()
plt.savefig('grafico_temperaturas.png', bbox_inches='tight', transparent=True)
plt.close()
