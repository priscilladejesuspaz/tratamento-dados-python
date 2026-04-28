import pandas as pd

# O Dataframe "df" é o elemento essencial no pandas, pois é uma tabela dentro dele.
dados = {
    "Nome": ["Ana", "Bruno", "Carlos"], 
    "Idade": [25, 47, 32], 
}

# Selecção do df acima dos dados, pd referenciando ao panda 
df = pd.DataFrame(dados)
# Exibe os dados do código 
print(df)

# As colunas do pandas são chamadas de "series"
# ✅ CORRIGIDO: antes estava df = ["Nome"], o que sobrescrevia o df com uma lista comum
serie_nome = df["Nome"]
print(serie_nome)

# Criação de uma série (coluna) do zero 
valores = [10, 20, 30]
s = pd.Series(valores)
print(s)

# Importar uma planilha do excel 
df = pd.read_excel('../data/cliente_informatica.xlsx')
print(df)

# Filtrar por colunas da tabela
cols = df[["Nome", "Idade"]]
print(cols)

# ✅ CORRIGIDO: antes estava df = ["Salário"] * 12, o que sobrescrevia o df com uma lista
# Adicionar uma nova coluna com o salário anual
df["Salário anual"] = df["Salário"] * 12
print(df)

# Comparações com valores booleanos 
df["Idade"] > 30  # Retornará "True" ou "False"

# ✅ CORRIGIDO: "idade" -> "Idade" (Python é case-sensitive)
# Trazer somente valores maiores que 30 
df_filtrado = df[df["Idade"] > 30]
print(df_filtrado)

# Filtrando duas condições  
filtro_idade = df["Idade"] > 30 
filtro_salario = df["Salário"] > 5000 

# Combinando os dois filtros - O & comercial tem a mesma função que o filtro "AND"
df[filtro_idade & filtro_salario]

# Caso queira filtrar uma condição ou outra, | tem a mesma função do OR
df[filtro_idade | filtro_salario]

# Inverter o filtro, utiliza-se o ~ retornando os salários menor que 5000
df[~filtro_salario]

# Tratamento de dados nulos - Forma de representar valores nulos = NaN
df_nulos = pd.read_excel("../data/cliente_informatica.xlsx", sheet_name="Email_nulos")
print(df_nulos)

# Remover linhas nulas 
df_nulos.dropna()

# Remover valores nulos de uma coluna específica 
df_nulos.dropna(subset=["Idade"])

# Preencher valores nulos com a média de idade
media_idade = df_nulos["Idade"].mean()
df_nulos["Idade"].fillna(media_idade)

# Transformando valor decimal em valor inteiro 
df_nulos["Idade"].astype(int)

# Para arredondar o número antes de converter para inteiro
df_nulos["Idade"].round().astype(int)

# Para sobrescrever o valor da coluna com os valores arredondados
df_nulos["Idade"] = df_nulos["Idade"].round().astype(int)

# Ordenar os valores de forma decrescente
df.sort_values(by="Salário", ascending=False)

# Contagem dos dados - conta os valores True/False de uma coluna booleana
df["Ativo"].value_counts()

# Utiliza-se o normalize para exibir a proporção e não o valor bruto 
df["Ativo"].value_counts(normalize=True)

# Caso queira calcular o percentual 
df["Ativo"].value_counts(normalize=True) * 100

# Agregações - média salarial por departamento
df.groupby("Departamento")["Salário"].mean()

# Soma dos salários 
df.groupby("Departamento")["Salário"].sum()

# Agrupar por várias colunas
grupos = ["Departamento", "Ativo"]
df.groupby(grupos)["Salário"].sum()

# ✅ CORRIGIDO: faltava vírgula após o primeiro argumento do agg
# Calcular diversas agregações ao mesmo tempo
df.groupby("Departamento").agg(
    idade_media=("Idade", "mean"),
    salario_medio=("Salário", "mean"),
)

# ✅ CORRIGIDO: faltava vírgula após o primeiro argumento
# Calcular a idade da pessoa mais velha e salário médio
df.groupby("Departamento").agg(
    idade_func_mais_velho=("Idade", "max"),
    salario_medio=("Salário", "mean"),
)

# ✅ CORRIGIDO: faltavam vírgulas entre os argumentos
# Olhar para três coisas ao mesmo tempo 
df.groupby("Departamento").agg(
    idade_func_mais_velho=("Idade", "max"),
    idade_media=("Idade", "mean"),
    salario_medio=("Salário", "mean"),
)

# Diversas operações em uma linha:
# 1. Filtra funcionários ativos
# 2. Agrupa por departamento
# 3. Agrega número de funcionários, idade média, salário mínimo e máximo
# 4. Ordena de forma decrescente por número de funcionários
filtro = df["Ativo"]  # já é valores True/False

# ✅ CORRIGIDO: "salario_minimo" usava "Idade" como coluna — corrigido para "Salário"
# ✅ CORRIGIDO: "ascendig" -> "ascending"
df[filtro].groupby("Departamento").agg(
    n_funcionarios=("Idade", "count"),
    idade_media=("Idade", "mean"),
    salario_minimo=("Salário", "min"),
    salario_maximo=("Salário", "max"),
).sort_values(by="n_funcionarios", ascending=False)