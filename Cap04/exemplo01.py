# def soma(lista):
#     total = 0
#     for x in lista:
#         total += x
#     return total

# print(soma([1, 2, 3]))

## Transformando em função Recursiva
def soma(lista):
    # Caso base: se a lista estiver vazia, a soma é 0
    if not lista:
        return 0
    # Caso recursivo: soma o primeiro elemento com a soma do restante da lista
    return lista[0] + soma(lista[1:])

print(soma([2, 4, 6]))


    
