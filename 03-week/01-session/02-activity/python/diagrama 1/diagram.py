
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el CSV
df = pd.read_csv("diagrama 1/gta_sa_vehicle_stats.csv", encoding="latin-1")

# Verificar las primeras filas para conocer las columnas
print(df.head())

# Ejemplo: Graficar la peso del vehiculo de los primeros 10 vehículos
plt.figure(figsize=(12, 6))
plt.bar(df["identifier"][:10], df["mass_(kg)"][:10], color="skyblue")
plt.title("peso del vehiculo de los 10 Primeros Vehículos en GTA San Andreas")
plt.xlabel("Vehículo")
plt.ylabel("peso del vehiculo")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
