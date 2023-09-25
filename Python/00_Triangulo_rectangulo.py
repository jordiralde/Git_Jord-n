import pandas as pd

# Cargar el conjunto de datos desde un archivo CSV
#df = pd.read_csv("glosario.csv")

url = 'https://drive.google.com/uc?id=1MqW2EpcIAnmffzu64-bq4kBv-07y9ILT'
df = pd.read_csv(url)

print (df)