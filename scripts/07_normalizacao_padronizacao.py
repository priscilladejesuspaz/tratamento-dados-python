# versão do código Chatgpt

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Ajustes de visualização (opcional)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Carrega o dataset
df = pd.read_csv('../data/clientes_tratados.csv')

# Mantém apenas as colunas relevantes
df = df[['idade', 'salario']]

# -------------------------------
# MINMAX SCALER (0 a 1)
# -------------------------------

# Cria o scaler padrão
scaler = MinMaxScaler()

# Aplica nas duas colunas ao mesmo tempo
# Resultado: valores entre 0 e 1
df[['idade_minmax', 'salario_minmax']] = scaler.fit_transform(df[['idade', 'salario']])

# -------------------------------
# MINMAX SCALER (-1 a 1)
# -------------------------------

# Cria scaler com range customizado
scaler_mm = MinMaxScaler(feature_range=(-1, 1))

# Resultado: valores entre -1 e 1
df[['idade_mm', 'salario_mm']] = scaler_mm.fit_transform(df[['idade', 'salario']])

# -------------------------------
# STANDARD SCALER (padronização)
# -------------------------------

from sklearn.preprocessing import StandardScaler

# Cria o scaler
scaler = StandardScaler()

# Padroniza os dados:
# média = 0
# desvio padrão = 1
df[['idadeStandardScaler', 'salarioStandardScaler']] = scaler.fit_transform(df[['idade', 'salario']])

# -------------------------------
# VISUALIZAÇÃO FINAL
# -------------------------------

print(df.head())

""""""""""""
# Código original do curso 

import pandas as pd
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('../data/clientes_tratados.csv')

print(df.head())

df = df.drop(labels=['data', 'estado', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao'], axis=1)

# Normalização - MinMaxScaler.
scaler = MinMaxScaler()
df['idadeMinMaxScaler'] = scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler'] = scaler.fit_transform(df[['salario']])

min_max_scaler = MinMaxScaler(feature_range=(-1, 1))
df['idadeMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['salario']])

# Padronização - StandardScaler
scaler = StandardScaler()
df['idadeStandardScaler'] = scaler.fit_transform(df[['idade']])
df['salarioStandardScaler'] = scaler.fit_transform(df[['salario']])

# Padronização - RobustScaler
scaler = RobustScaler()
df['idadeRobustScaler'] = scaler.fit_transform(df[['idade']])
df['salarioRobustScaler'] = scaler.fit_transform(df[['salario']])

print(df.head(15))

print("MinMaxScaler (De 0 a 1):")
print("Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}".format(df['idadeMinMaxScaler'].min(), df['idadeMinMaxScaler'].max(), df['idadeMinMaxScaler'].mean(), df['idadeMinMaxScaler'].std()))
print("Salário - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}".format(df['salarioMinMaxScaler'].min(), df['salarioMinMaxScaler'].max(), df['salarioMinMaxScaler'].mean(), df['salarioMinMaxScaler'].std()))

print("\nMinMaxScaler (De -1 a 1):")
print("Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}".format(df['idadeMinMaxScaler_mm'].min(), df['idadeMinMaxScaler_mm'].max(), df['idadeMinMaxScaler_mm'].mean(), df['idadeMinMaxScaler_mm'].std()))
print("Salário - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}".format(df['salarioMinMaxScaler_mm'].min(), df['salarioMinMaxScaler_mm'].max(), df['salarioMinMaxScaler_mm'].mean(), df['salarioMinMaxScaler_mm'].std()))

print("\nStandardScaler (Ajuste a média a 0 e desvio padrão a 1):")
print("Idade - Min: {:.4f} Max: {:.4f} Mean: {:.18f} Std: {:.4f}".format(df['idadeStandardScaler'].min(), df['idadeStandardScaler'].max(), df['idadeStandardScaler'].mean(), df['idadeStandardScaler'].std()))
print("Salário - Min: {:.4f} Max: {:.4f} Mean: {:.18f} Std: {:.4f}".format(df['salarioStandardScaler'].min(), df['salarioStandardScaler'].max(), df['salarioStandardScaler'].mean(), df['salarioStandardScaler'].std()))

print("\nRobustScaler (Ajuste a mediana e IQR):")
print("Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}".format(df['idadeRobustScaler'].min(), df['idadeRobustScaler'].max(), df['idadeRobustScaler'].mean(), df['idadeRobustScaler'].std()))
print("Salário - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}".format(df['salarioRobustScaler'].min(), df['salarioRobustScaler'].max(), df['salarioRobustScaler'].mean(), df['salarioRobustScaler'].std()))