import pandas as pd

pd.set_option('display.width', None) 
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('../data/arrecadacao_estado_raw.csv', sep=';', encoding='latin-1')

print(df.head().to_string())

print('Qtd', df.shape)

print('Tipagem, \n', df.dtypes)

print('Valores nulos:\n', df.isnull().sum())

print(df[['Ano', 'UF', 'IMPOSTO SOBRE IMPORTAÇÃO', 'IMPOSTO SOBRE EXPORTAÇÃO', 'IRPF','COFINS', 'RECEITA PREVIDENCIÁRIA', 'IRRF - RENDIMENTOS DO TRABALHO'
]].head(10).to_string())

colunas = [
    'IMPOSTO SOBRE IMPORTAÇÃO',
    'IMPOSTO SOBRE EXPORTAÇÃO',
    'IRPF',
    'COFINS',
    'RECEITA PREVIDENCIÁRIA',
    'IRRF - RENDIMENTOS DO TRABALHO'

]

df[colunas] = df[colunas].apply(pd.to_numeric, errors='coerce')

df['Ano'] = df['Ano'].astype(str).str.replace('.0','', regex=False).str.zfill(4)

print((df['Ano'].head(10)))

df = df.dropna(subset=['Ano', 'Mês', 'UF', 'IMPOSTO SOBRE IMPORTAÇÃO', 'IMPOSTO SOBRE EXPORTAÇÃO', 'IRPF', 'IRRF - RENDIMENTOS DO TRABALHO'])
df['COFINS'] = df['COFINS'].fillna(0)
df['RECEITA PREVIDENCIÁRIA'] = df['RECEITA PREVIDENCIÁRIA'].fillna(0)

# Deletar colunas zeradas
df = df.drop(columns=['Unnamed: 45'])


print(df[['Ano', 'UF', 'IMPOSTO SOBRE IMPORTAÇÃO', 'IMPOSTO SOBRE EXPORTAÇÃO', 'IRPF','COFINS', 'RECEITA PREVIDENCIÁRIA', 'IRRF - RENDIMENTOS DO TRABALHO']].head(1000).to_string())

pd.set_option('display.float_format', '{:.2f}'.format)

print(df[['Ano', 'Mês', 'UF', 'IMPOSTO SOBRE IMPORTAÇÃO', 'IMPOSTO SOBRE EXPORTAÇÃO', 'IRPF','COFINS', 'RECEITA PREVIDENCIÁRIA', 'IRRF - RENDIMENTOS DO TRABALHO']].head(10).to_string())

# Exporta o CSV tratado para importar no MySQL
df[['Ano', 'Mês', 'UF',
    'IMPOSTO SOBRE IMPORTAÇÃO',
    'IMPOSTO SOBRE EXPORTAÇÃO',
    'IRPF',
    'COFINS',
    'RECEITA PREVIDENCIÁRIA',
    'IRRF - RENDIMENTOS DO TRABALHO'
]].to_csv('../data/arrecadacao_tratado.csv', index=False, sep=';', encoding='latin-1')