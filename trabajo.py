import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
df = pd.read_csv('salario.csv')

# Visualización 1: Edad vs Estudio
plt.figure(figsize=(10, 6))
plt.scatter(df['edad'], df['estudio'], alpha=0.5)
plt.title('Edad vs Estudio')
plt.xlabel('Edad')
plt.ylabel('Estudio')
plt.grid(True)
plt.show()

# Visualización 2: Estudio vs Ingreso
plt.figure(figsize=(10, 6))
df_grouped = df.groupby('estudio')['ingreso'].mean().reset_index()
plt.bar(df_grouped['estudio'], df_grouped['ingreso'])
plt.title('Estudio vs Ingreso Promedio')
plt.xlabel('Estudio')
plt.ylabel('Ingreso Promedio')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()