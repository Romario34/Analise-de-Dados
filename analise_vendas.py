"""
Projeto de portfólio: Análise de Vendas com Python
Os dados são fictícios e destinados a fins educacionais.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

PASTA_PROJETO = Path(__file__).resolve().parent
PASTA_DADOS = PASTA_PROJETO / "dados"
PASTA_GRAFICOS = PASTA_PROJETO / "graficos"
PASTA_GRAFICOS.mkdir(exist_ok=True)

def carregar_dados():
    arquivo = PASTA_DADOS / "vendas.csv"
    dados = pd.read_csv(arquivo, parse_dates=["data"])
    return dados

def analisar(dados):
    dados = dados.copy()
    dados["mes"] = dados["data"].dt.to_period("M").astype(str)

    print("\n" + "=" * 48)
    print("       RELATÓRIO DE ANÁLISE DE VENDAS")
    print("=" * 48)
    print(f"Quantidade de pedidos: {dados['pedido_id'].nunique():,}".replace(",", "."))
    print(f"Unidades vendidas: {dados['quantidade'].sum():,}".replace(",", "."))
    print(f"Faturamento total: R$ {dados['faturamento'].sum():,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    ticket = dados.groupby("pedido_id")["faturamento"].sum().mean()
    print(f"Ticket médio por pedido: R$ {ticket:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

    por_produto = dados.groupby("produto")["faturamento"].sum().sort_values(ascending=False)
    por_categoria = dados.groupby("categoria")["faturamento"].sum().sort_values(ascending=False)
    por_regiao = dados.groupby("regiao")["faturamento"].sum().sort_values(ascending=False)
    por_canal = dados.groupby("canal_venda")["faturamento"].sum().sort_values(ascending=False)
    por_mes = dados.groupby("mes")["faturamento"].sum()

    print("\nTop 5 produtos por faturamento:")
    print(por_produto.head(5).to_string())
    print("\nFaturamento por categoria:")
    print(por_categoria.to_string())
    print("\nFaturamento por região:")
    print(por_regiao.to_string())
    print("\nFaturamento por canal de venda:")
    print(por_canal.to_string())

    plt.figure(figsize=(10, 5))
    por_mes.plot(kind="line", marker="o")
    plt.title("Faturamento mensal")
    plt.xlabel("Mês")
    plt.ylabel("Faturamento (R$)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(PASTA_GRAFICOS / "faturamento_mensal.png", dpi=150)
    plt.close()

    plt.figure(figsize=(10, 5))
    por_produto.sort_values().plot(kind="barh")
    plt.title("Faturamento por produto")
    plt.xlabel("Faturamento (R$)")
    plt.ylabel("Produto")
    plt.tight_layout()
    plt.savefig(PASTA_GRAFICOS / "faturamento_por_produto.png", dpi=150)
    plt.close()

    plt.figure(figsize=(8, 5))
    por_categoria.plot(kind="bar")
    plt.title("Faturamento por categoria")
    plt.xlabel("Categoria")
    plt.ylabel("Faturamento (R$)")
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.savefig(PASTA_GRAFICOS / "faturamento_por_categoria.png", dpi=150)
    plt.close()

    print(f"\nGráficos salvos na pasta: {PASTA_GRAFICOS}")
    print("Análise concluída!")

if __name__ == "__main__":
    df = carregar_dados()
    print("\nPrévia dos dados:")
    print(df.head().to_string(index=False))
    print(f"\nValores ausentes por coluna:\n{df.isna().sum().to_string()}")
    analisar(df)
