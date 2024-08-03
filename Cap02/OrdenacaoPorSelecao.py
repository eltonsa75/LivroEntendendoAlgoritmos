def buscaMenor(arr, start_index):
    # Encontra o menor elemento a partir do índice start_index
    menor = arr[start_index]
    menor_indice = start_index
    for i in range(start_index + 1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice


def ordenacao_por_selecao(arr):
    # Ordena a lista arr usando o algoritmo de ordenação por seleção
    novoArr = []
    while arr:
        # Encontra o menor elemento a partir do início da lista
        menor_indice = buscaMenor(arr, 0)
        # Remove o menor elemento da lista original e adiciona ao novoArr
        novoArr.append(arr.pop(menor_indice))
    return novoArr


print(ordenacao_por_selecao([5, 3, 6, 2, 10]))
