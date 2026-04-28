import pandas as pd

# Configuração de visualização
pd.set_option('display.width', None)

# 1. Carga dos dados
df = pd.read_csv('../data/clientes_raw.csv')
print("Dados Iniciais:\n", df.head())

# 2. Remoção de dados desnecessários
# Removendo coluna 'pais' e a linha de índice 2
df.drop(labels='pais', axis=1, inplace=True)
df.drop(labels=2, axis=0, inplace=True)

# 3. Normalização de campos de texto
df['nome'] = df['nome'].str.title()
df['endereco'] = df['endereco'].str.lower()
df['estado'] = df['estado'].str.strip().str.upper()

# 4. Tratamento de valores nulos (Ausentes)
# Substituindo nulos por valores padrão ou cálculos
df['estado'] = df['estado'].fillna('DESCONHECIDO')
df['endereco'] = df['endereco'].fillna('Endereço não informado')
df['idade'] = df['idade'].fillna(df['idade'].mean())

# Removendo registros onde o CPF é essencial e está nulo
df.dropna(subset=['cpf'], inplace=True)

# Tratar formato de daods
# 5. Conversão de tipos de dados (Cast)
# Convertendo idade para inteiro e data para datetime
df['idade'] = df['idade'].astype(int)
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

# 6. Tratamento de dados duplicados
print(f'\nQtd registros antes de remover duplicados: {len(df)}')
df.drop_duplicates(subset='cpf', inplace=True)
print(f'Qtd registros após remover duplicados: {len(df)}')

# 7. Finalização e Exportação
print("\n--- Dados Limpos ---")
print(df.head())

# Verificação final de nulos
print("\nCheck final de valores nulos:\n", df.isnull().sum())

# Salvando o resultado
df.to_csv('../data/clientes_limpeza.csv', index=False)
print("\nArquivo '../data/clientes_limpeza.csv' gerado com sucesso!")

