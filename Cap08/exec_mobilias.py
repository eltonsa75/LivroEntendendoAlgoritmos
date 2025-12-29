def carregar_caminhao(capacidade, caixas):
    caixas.sort(reverse=True)
    carregadas = []
    espaco_restante = capacidade

    for caixa in caixas:
        if caixa <= espaco_restante:
            carregadas.append(caixa)
            espaco_restante -= caixa

    return carregadas, espaco_restante

capacidade = 100
caixas = [50, 40, 30, 20, 10]

print(carregar_caminhao(capacidade, caixas))
