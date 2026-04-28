import pandas as pd

pd.set_option('display.width', None)


# ============================================================
# 1. CARGA DOS DADOS
# ============================================================
df = pd.read_csv('../data/arrecadacao_estado_raw.csv', sep=';', encoding='latin-1')

print(df.head())
