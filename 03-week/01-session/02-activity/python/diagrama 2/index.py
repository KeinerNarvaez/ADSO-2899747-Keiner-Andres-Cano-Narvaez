import pandas as pd
import matplotlib.pyplot as plt

# Cargar el CSV
df = pd.read_csv("diagrama 2/youtube_data.csv", encoding="latin-1")

# Verificar las primeras filas para conocer las columnas
print(df.head())

# Ejemplo: Graficar la peso del vehiculo de los primeros 10 vehículos
plt.figure(figsize=(12, 6))
plt.bar(df["video_id"][:20], df["likes"][:20], color="skyblue")
plt.title("Likes de los videos")
plt.xlabel("identificador de los videos")
plt.ylabel("Likes de los videos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
