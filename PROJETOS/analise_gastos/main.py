import pandas as pd
import matplotlib.pyplot as plt

# carregar dados
df = pd.read_csv("data\gastos.csv")

# converter data
df["data"] = pd.to_datetime(df["data"])

print("\nDados carregados:")
print(df)

# total gasto
total = df["valor"].sum()
print("\nTotal gasto:", total)

# média de gastos
media = df["valor"].mean()
print("Média de gastos:", round(media, 2))

# maior gasto
maior = df.loc[df["valor"].idxmax()]
print("\nMaior gasto:")
print(maior)

# gastos por categoria
categoria = df.groupby("categoria")["valor"].sum()

print("\nGastos por categoria:")
print(categoria)

# ordenar por data
df = df.sort_values("data")

# =========================
# GRÁFICOS (AGORA CORRETO)
# =========================

# gráfico 1 - categoria
plt.figure()
categoria.plot(kind="bar")
plt.title("Gastos por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Valor")
plt.tight_layout()
plt.savefig("graphs/gastos_categoria.png")

# gráfico 2 - evolução
plt.figure()
plt.plot(df["data"], df["valor"], marker='o')
plt.title("Evolução dos Gastos")
plt.xlabel("Data")
plt.ylabel("Valor")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graphs/evolucao_gastos.png")

# MOSTRAR TODOS OS GRÁFICOS DE UMA VEZ
plt.show()
