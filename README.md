# Tratamento e Limpeza de Dados - Python

## Sobre o projeto

Conjunto de scripts que formam um **pipeline completo de preparação de dados** usando Python e pandas.
Cada script cobre uma etapa do processo, do dado bruto até o dado pronto para análise ou modelagem.

Desenvolvido durante estudos práticos com foco em Data Analytics.

## Ferramentas
- Python 3
- pandas, numpy

## Pipeline de scripts

| Script | O que faz |
|--------|-----------|
| `01_intro_tratamento_dados.py` | Primeiro contato: leitura de CSV e inspeção básica |
| `02_intro_preparacao_dados.py` | Estratégias de preparação antes da análise |
| `03_pandas_fundamentos.py` | Fundamentos de pandas: seleção, filtro, agrupamento |
| `04_inconsistencias.py` | Identificação e tratamento de inconsistências |
| `05_limpeza_dados.py` | Limpeza: valores nulos, tipos de dados, duplicatas |
| `06_outliers.py` | Detecção e remoção de outliers |
| `07_normalizacao_padronizacao.py` | Normalização (Min-Max) e padronização (Z-score) |
| `08_codificacao_variaveis_categoricas.py` | Label Encoding e One-Hot Encoding |
| `09_engenharia_features.py` | Criação de novas variáveis a partir das existentes |
| `10_estudo_lambda.py` | Uso de funções lambda com apply() |
| `11_pratica_1.py` e `12_pratica_2.py` | Exercícios práticos consolidando o pipeline |
| `13_arrecadacao_estado.py` | Aplicação real: limpeza de dados de arrecadação federal por estado |
| `14_fitness.py` | Exploração de dataset de saúde/fitness |

## Estrutura

```
03_tratamento_dados_python/
├── data/
│   ├── clientes_raw.csv              → dataset bruto de clientes
│   ├── clientes_v2.csv               → versão ampliada do dataset
│   ├── clientes_limpeza.csv          → após etapa de limpeza
│   ├── clientes_remove_outliers.csv  → após remoção de outliers
│   ├── clientes_tratados.csv         → versão final tratada
│   ├── cliente_informatica.xlsx      → dados de clientes de TI
│   ├── arrecadacao_estado_raw.csv    → arrecadação federal bruta
│   ├── arrecadacao_tratado.csv       → arrecadação tratada (pronta para SQL)
│   ├── sales.csv                     → dados de vendas
│   └── desastres_geo_hidrologicos.csv
├── scripts/        → scripts Python numerados em ordem de estudo
├── notebooks/      → notebooks Jupyter complementares
└── README.md
```

## Observação

Os scripts usam caminhos absolutos `C:/Users/Book/...`. Para rodar, atualize os caminhos de `pd.read_csv()` para apontar para a pasta `data/` local.

## Aprendizados

- Pipeline completo de limpeza: ingestão → inspeção → limpeza → transformação → exportação
- Tratamento de nulls, duplicatas, tipos incorretos e outliers
- Normalização e codificação para uso em modelos de ML
- Engenharia de features com pandas
- Aplicação em dados reais de arrecadação federal
