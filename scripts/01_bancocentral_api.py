
from pathlib import Path # Manipula caminhos de arquivos e diretórios de forma orientada a objetos e independente do sistema operacional.
import requests # Realiza requisições HTTP para consumir APIs e acessar recursos da web de forma simples.
import pandas as pd # Manipula e analisa dados estruturados por meio de DataFrames e Series.

# REQUISIÇÃO À API DO BANCO CENTRAL DO BRASIL EM 2025
URL = ("https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json")

# Parâmetros da requisição
response = requests.get(URL, timeout=30)
response.raise_for_status()

dados = response.json()
df = pd.DataFrame(dados)

# visualizar (prof pede)
df.head()

# tratamento 1: tipo
df["valor"] = pd.to_numeric(df["valor"], errors="coerce")

# tratamento 2: data
df["data"] = pd.to_datetime(df["data"], dayfirst=True)

# tratamento 3 (extra, melhora nota): remover nulos
df.info()

df.to_csv("../data/processed/bcb_tabela.csv", index=False)
df.to_csv("../data/processed/dados_tratados.csv", index=False)