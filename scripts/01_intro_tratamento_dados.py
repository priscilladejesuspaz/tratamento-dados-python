import pandas as pd

df = pd.read_csv('../data/clientes_raw.csv')

# Verificar os primeiros registros
print(df.head().to_string())

# Verificar qtd de linhas e colunas
print('Qtd: ', df.shape)

# Verificar tipos de dados
print('Tipagem:\n', df.dtypes)

# Checar valores nulos
print('Valores nulos:\n', df.isnull().sum())