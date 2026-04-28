import pandas as pd
import numpy as np
from scipy import stats 

pd.set_option('display.width', None)

df = pd.read_csv('../data/clientes_tratados.csv')

print(df.head())

# Transformação Logarítimica 
df['salario_log'] = np.log1p(df['salario']) # Log1p é usado para evitar problemas com valores zero ou negativos 

print("\n'Dataframe após a transofrmação logarítmica no salário':n/", df.head())

# Codificação de frequência para 'estado'
estado_freq = df['estado'].value_counts() / len(df)
df['estado_freq'] = df['estado'].map(estado_freq)

print("\n'Datafram após codificação de frequência por 'estado':\n", df.head())

# Interações 

print("\n'Dataframe após criação de interações entre 'idade' e 'filhos':\n", df.head())