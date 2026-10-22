# 📊 Análise de Vendas com Python

Projeto de portfólio de Análise de Dados usando **Python, Pandas e Matplotlib**. O objetivo é transformar dados de vendas em indicadores que ajudem a compreender o desempenho comercial.



## Objetivos
- Carregar e explorar dados de vendas em CSV.
- Verificar valores ausentes e visualizar os registros.
- Calcular faturamento, quantidade vendida e ticket médio.
- Comparar resultados por produto, categoria, região, canal e mês.
- Criar gráficos para apoiar a interpretação dos resultados.

## Tecnologias
- Python 
- Pandas
- Matplotlib

## Estrutura do projeto

```text
analise_vendas_python/
├── analise_vendas.py
├── requirements.txt
├── README.md
├── dados/
│   ├── vendas.csv
│   ├── resumo_por_produto.csv
│   ├── resumo_por_categoria.csv
│   └── resumo_mensal.csv
└── graficos/
    ├── faturamento_mensal.png
    ├── faturamento_por_produto.png
    └── faturamento_por_categoria.png


## Perguntas de negócio exploradas
1. Qual é o faturamento total no período?
2. Quais produtos geram mais faturamento?
3. Quais categorias se destacam?
4. Como o faturamento varia mês a mês?
5. Quais regiões e canais apresentam maior faturamento?

## Indicadores
- **Faturamento:** soma dos valores de venda após desconto.
- **Pedidos:** quantidade de identificadores de pedido distintos.
- **Unidades vendidas:** soma das quantidades.
- **Ticket médio:** faturamento total dividido pelo número de pedidos.

## Possíveis melhorias
- Adicionar margem de lucro e custos.
- Criar filtros interativos com Streamlit.
- Conectar os dados a um banco SQL.
- Construir um dashboard no Power BI.
- Automatizar a atualização dos relatórios.

## Autor
**Romário Brito** — projeto educacional em Análise de Dados.
