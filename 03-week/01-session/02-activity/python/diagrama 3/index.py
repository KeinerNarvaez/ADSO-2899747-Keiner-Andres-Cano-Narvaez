import pandas as pd
import matplotlib.pyplot as plt

# Cargar el CSV
df = pd.read_csv("diagrama 3/Coffe_sales.csv", encoding="latin-1")

# Verificar las primeras filas para conocer las columnas
print(df.head())

# Ejemplo: Graficar la peso del vehiculo de los primeros 10 vehículos
plt.figure(figsize=(12, 6))
plt.bar(df["coffee_name"][:20], df["money"][:20], color="skyblue")
plt.title("Cafe")
plt.xlabel("cafes")
plt.ylabel("Costos de cafe")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
