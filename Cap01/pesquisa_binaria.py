def pesquisa_binaria(lista, item):
    posicaoMaisBaixa = 0
    posicaoMaisAlto = len(lista) - 1

    while posicaoMaisBaixa <= posicaoMaisAlto:
        meio = (posicaoMaisBaixa + posicaoMaisAlto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            posicaoMaisAlto = meio - 1
        else:
            posicaoMaisBaixa = meio + 1

    return None


minha_lista = [1, 3, 5, 7, 9]

print(pesquisa_binaria(minha_lista, 3))  # => 1
print(pesquisa_binaria(minha_lista, -1))  # => None
