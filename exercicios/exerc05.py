 # Itens: (nome, peso, valor)
itens = [
    ("agua", 3, 10),
    ("livro", 1, 3),
    ("comida", 2, 9),
    ("casaco", 2, 5),
    ("camera", 1, 6)
]

capacidade = 6
n = len(itens)

# Matriz DP
dp = [[0] * (capacidade + 1) for _ in range(n + 1)]

# Preenchendo a tabela
for i in range(1, n + 1):
    nome, peso, valor = itens[i - 1]
    for w in range(capacidade + 1):
        if peso <= w:
            dp[i][w] = max(
                dp[i - 1][w],                 # não pega o item
                dp[i - 1][w - peso] + valor  # pega o item
            )
        else:
            dp[i][w] = dp[i - 1][w]

# Recuperando os itens escolhidos
w = capacidade
itens_escolhidos = []

for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        nome, peso, valor = itens[i - 1]
        itens_escolhidos.append(nome)
        w -= peso

# Resultados
print("Itens escolhidos:", itens_escolhidos[::-1])
print("Valor máximo:", dp[n][capacidade])
