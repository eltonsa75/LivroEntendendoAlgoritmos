import pandas as pd

# Criando a tabela de avaliações
dados = {
    "PRIYANKA": [3, 4, 4, 1, 4],
    "JUSTIN":   [4, 3, 5, 1, 5],
    "MORPHEUS": [2, 5, 1, 3, 1]
}

generos = ["Comedia", "Acao", "Drama", "Terror", "Romance"]

df = pd.DataFrame(dados, index=generos)

print(df)
