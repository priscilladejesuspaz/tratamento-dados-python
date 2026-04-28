import pandas as pd
# As barras invertidas no caminho não funciona, e com isso é necessário alterar parar /
df = pd.read_csv('../data/clientes_v2.csv')

# Boas práticas 
# Visualizar o cabeçalho do dataframe
print(df.head().to_string())
#Visualizar os 5 primeiros registros e os 5 últimos
print(df.tail().to_string())
# Converter a data para formato padrão
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

# Informação dos dados 
print('Veriicação inicial:')
print(df.info())

print('Analise de dados nulos: \n', df.isnull().sum())
print('Porcentagem % dos dados nulos: \n', df.isnull().mean() * 100)
df.dropna(inplace=True) # Exlcuindo os dados nulos 
print('Confirmar remoção dos dados nulos: \n', df.isnull().sum().sum())

print('Analise dados duplicados:\n' , df.duplicated().sum())

print('Analise de dados únicos: \n', df.nunique())

print('Estatisticas dos dados: \n', df.describe()) # Std é desvio padrão

# Criação de um novo dataframe, removendo alguns dados desnecessários
df = df[['idade', 'data', 'estado', 'salario', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao']]
print(df.head().to_string())

df.to_csv('clientes-vs-tratados.csv', index=False)