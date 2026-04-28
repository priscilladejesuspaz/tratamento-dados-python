import requests
import pandas as pd

url = "https://servicodados.ibge.gov.br/api/v1/localidades/regioes"

response = requests.get(url)
data = response.json()

df_ibge = pd.json_normalize(data)

df_ibge.head()