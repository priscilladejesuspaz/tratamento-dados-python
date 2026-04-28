import pandas as pd
import numpy as np

# --- CONFIGURAÇÃO DE AMBIENTE ---
# Garante que o print no terminal mostre todas as colunas sem cortar o texto
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# 1. CARGA DOS DADOS
# Lendo o CSV que já passou pelas etapas de limpeza e outliers
df = pd.read_csv('../data/clientes_remove_outliers.csv')

print("Dados originais (Início):\n", df.head())

# 2. PRIVACIDADE / LGPD (Mascarar CPF)
# Esconde o meio do CPF para proteger os dados do cliente
# Pega os 3 primeiros caracteres + asteriscos + os 2 últimos
df['cpf_mascara'] = df['cpf'].apply(lambda cpf: f'{str(cpf)[:3]}.***.***-{str(cpf)[-2:]}')

# 3. TRATAMENTO DE DATAS (Onde a maioria erra)
# Transforma o texto da coluna 'data' em um objeto de data real do Python
df['data'] = pd.to_datetime(df['data'], errors='coerce')
data_atual = pd.to_datetime('today')

# REGRA DE CONSISTÊNCIA: Se a data for no futuro ou muito antiga (antes de 1900),
# substitui por uma data padrão para não quebrar os cálculos.
df['data_atualizada'] = df['data'].where(df['data'] <= data_atual, pd.to_datetime('1900-01-01'))

# 4. CÁLCULO PRECISO DE IDADE
# Passo 1: Diferença simples entre o ano atual e o ano de nascimento
df['idade_ajustada'] = data_atual.year - df['data_atualizada'].dt.year

# Passo 2: Ajuste de aniversário (verifica se a pessoa JÁ FEZ aniversário este ano)
# Se não fez, subtrai 1 da idade. O .astype(int) transforma Verdadeiro/Falso em 1/0.
df['idade_ajustada'] -= ((data_atual.month <= df['data_atualizada'].dt.month) & (data_atual.day < df['data_atualizada'].dt.day)).astype(int)

# REGRA: Se após o cálculo a idade for impossível (>100), limpamos (NaN)
df.loc[df['idade_ajustada'] > 100, 'idade_ajustada'] = np.nan

# 5. DIVISÃO DE INFORMAÇÕES (Endereço, Bairro, Estado)
# O split('\n') quebra o texto onde tem o "Enter". 
# [0] pega a primeira linha (Rua), [1] pega a segunda (Bairro)
df['endereco_curto'] = df['endereco'].apply(lambda x: str(x).split('\n')[0].strip())

df['bairro'] = df['endereco'].apply(
    lambda x: str(x).split('\n')[1].strip() if len(str(x).split('\n')) > 1 else 'Desconhecido'
)

# Pega o Estado que vem depois da barra '/' no final do endereço
df['estado_sigla'] = df['endereco'].apply(
    lambda x: str(x).split('/')[-1].strip().upper() if '/' in str(x) else 'Desconhecido'
)

# 6. VALIDAÇÃO DE CAMPOS (Regras de Negócio)
# Verifica se o endereço não ficou curto demais ou longo demais
df['endereco_curto'] = df['endereco_curto'].apply(
    lambda x: 'Endereço inválido' if len(x) > 50 or len(x) < 5 else x
)

# Verifica se o CPF tem exatamente 14 caracteres (formato 000.000.000-00)
df['cpf_valido'] = df['cpf'].apply(lambda x: x if len(str(x)) == 14 else 'CPF inválido')

# Lista oficial de estados para conferir se a sigla extraída existe
estados_br = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
df['estado_sigla'] = df['estado_sigla'].apply(lambda x: x if x in estados_br else 'Desconhecido')

# 7. UNIFICAÇÃO E LIMPEZA DO DATAFRAME
# Substituímos as colunas velhas pelas novas tratadas
df['cpf'] = df['cpf_mascara']
df['idade'] = df['idade_ajustada']
df['endereco'] = df['endereco_curto']
df['estado'] = df['estado_sigla']

# Selecionamos apenas as colunas que interessam para o resultado final
df_salvar = df[['nome', 'cpf', 'idade', 'data', 'endereco', 'bairro', 'estado']]

# 8. EXPORTAÇÃO
# Salva o arquivo final pronto para ser usado em Dashboards/Relatórios
# O 'utf-8-sig' é o segredo para o Excel entender os acentos no Windows
df_salvar.to_csv('../data/clientes_tratados.csv', index=False, encoding='utf-8-sig')

print('\n--- Dados Tratados com Sucesso! ---')
print(df_salvar.head())