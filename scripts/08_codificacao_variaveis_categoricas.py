import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.width', None)

# O SEP organiza o CSV, nesse caso é ';'
df = pd.read_csv('../data/clientes_v2.csv')
                 
print(df.head())

# Visualiza sem truncar o endereço
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
print(df.head())

# Classificação one_hot para 'estado civil'
df = pd.concat([df, pd.get_dummies(df['estado_civil'], prefix='estado_civil')], axis=1)

print("\nDataframe codificação onee_hot para 'estado_civil':\n", df.head())

# Codificação ordinal para 'nivel_educacao'
educacao_ordem = {'Ensino Fundamental': 1, 'Ensino Médio': 2, 'Ensino Superior': 3, 'Pós-Graduação': 4}
df['nivel_educacao_ordinal'] = df['nivel_educacao'].map(educacao_ordem)

# Transformar 'area_atuacao' em categorias codificadas usando o metódo .cat.codes
df['area_atuacao'] = df['area_atuacao'].astype('category').cat.codes

print("\nDataframe após transformar 'area_atuacao' em códigos númericos:\n", df.head())

# LabelEncoder para 'estado'
# LabelEncoder converte cada valor único em número de 0 a n_classes-1
label_encoder = LabelEncoder()
df['estado_cod'] = label_encoder.fit_transform(df['estado'])

print("\nDataframe após codificar 'estado' com LabelEncoder:\n", df.head())
