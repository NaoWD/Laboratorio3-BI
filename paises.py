import matplotlib.pyplot as plt

# Datos para Perú
x_peru = [2012, 2022, 2025, 2028]
y_peru = [42, 43, 45, 47]

# Datos para Colombia
x_colombia = [2012, 2022, 2025, 2028]
y_colombia = [42, 48, 49, 50]

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(x_peru, y_peru, marker='o', label='Perú', linestyle='-', color='b')
plt.plot(x_colombia, y_colombia, marker='o', label='Colombia', linestyle='-', color='g')

# Etiquetas y título
plt.xlabel('Año')
plt.ylabel('Población (en millones)')
plt.title('Población de Perú y Colombia (2012-2028)')

# Leyenda
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()
