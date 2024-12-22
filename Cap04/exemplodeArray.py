# def quicksort(array):
#     # Caso base: se o array tem 0 ou 1 elementos, ele já está ordenado
#     if len(array) < 2:
#         return array
    
#     # Escolher o pivô; aqui, o pivô é o primeiro elemento
#     pivot = array[0]
    
#     # Particionar o array em três partes:
#     # - Menores que o pivô
#     # - Igual ao pivô
#     # - Maiores que o pivô
#     less = [x for x in array[1:] if x <= pivot]
#     equal = [x for x in array if x == pivot]
#     greater = [x for x in array[1:] if x > pivot]
    
#     # Aplicar o quicksort recursivamente nas partes menores e maiores e concatenar os resultados
#     return quicksort(less) + equal + quicksort(greater)

# # Testando a função
# print(quicksort([3, 6, 8, 10, 1, 2, 1]))

### Exemplo 02
def quicksort(array):
    # Caso base: se o array tem 0 ou 1 elementos, ele já está ordenado
    if len(array) < 2:
        return array
    
    # Escolher o pivô como 33
    pivot = 33
    
    # Particionar o array em três partes:
    # - Menores que o pivô
    # - Igual ao pivô
    # - Maiores que o pivô
    less = [x for x in array if x < pivot]
    equal = [x for x in array if x == pivot]
    greater = [x for x in array if x > pivot]
    
    # Aplicar o quicksort recursivamente nas partes menores e maiores e concatenar os resultados
    sorted_less = quicksort(less)
    sorted_greater = quicksort(greater)
    
    return sorted_less + equal + sorted_greater

# Testando a função
print(quicksort([3, 6, 33, 8, 10, 1, 33, 2, 33, 1]))



