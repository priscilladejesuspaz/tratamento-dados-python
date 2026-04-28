import pandas as pd
from scipy import stats

# Configurações de exibição para o terminal
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# 1. CARGA DOS DADOS (Ajustado para ler o arquivo que você já tem)
# O erro acontecia porque aqui estava '../data/clientes_remove_outliers.csv'
df = pd.read_csv('../data/clientes_limpeza.csv')

# 2. IDENTIFICAR OUTLIERS COM Z-SCORE
# O Z-score diz quantos desvios padrão um dado está longe da média
z_scores = stats.zscore(df['idade'].dropna())
outliers_z = df[z_scores >= 3]
print("Outliers encontrados pelo Z-score:\n", outliers_z)

# 3. IDENTIFICAR OUTLIERS COM IQR (Intervalo Interquartil)
Q1 = df['idade'].quantile(0.25)
Q3 = df['idade'].quantile(0.75)
IQR = Q3 - Q1

limite_baixo = Q1 - 1.5 * IQR
limite_alto = Q3 + 1.5 * IQR

print(f'\nLimites IQR: Baixo={limite_baixo}, Alto={limite_alto}')

# 4. FILTRAR OS DADOS (Removendo o que está fora dos limites)
# Aqui mantemos apenas quem está dentro da faixa aceitável
df_filtrado = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]

# 5. SALVAR O ARQUIVO PARA O PRÓXIMO PASSO
# Agora sim, criamos o arquivo que o 'inconsistencias.py' vai precisar
df_filtrado.to_csv('../data/clientes_remove_outliers.csv', index=False)

print('\n--- Sucesso! ---')
print('Arquivo "clientes_remove_outliers.csv" gerado com os outliers removidos.')
print(f'Qtd registros antes: {len(df)} | Qtd registros agora: {len(df_filtrado)}')