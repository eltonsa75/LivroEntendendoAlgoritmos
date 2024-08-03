import math


def binary_search(arr, target):
    # inicializa os índices da busca
    left, right = 0, len(arr) - 1
    # contador de etapas
    steps = 0

    # Enquanto o índice da esquerda for menor ou igual ao da direita
    while left <= right:
        # Incrementa o contador de etapas
        steps += 1
        # Calcula o índice do meio
        mid = (left + right) // 2
        # Se o elemento do meio é o alvo, retorna o índice e as etapas
        if arr[mid] == target:
            return mid, steps
        # Se o lemento do meio que o alvo, ajusta o índice da esquerda
        elif arr[mid] < target:
            left = mid + 1
            # Se o elemento do meio é maior que o alvo, ajusta o índdice da direita
        else:
            right = mid - 1

    # Se o alvo não for encontrado, retorna -1 e as etapas
    return -1, steps


# Número de elementos na lista
n = 256
# Calculando o número máximo de etapas
max_steps = math.ceil(math.log2(n))

# Lista com 128 nomes ordenados
names = [f"name{i}" for i in range(n)]

# nome a ser buscado
target_name = "Name64"

# Chama a função de busca binária
index, steps_taken = binary_search(names, target_name)


# imprime se o nome foi encontrado, a posição e as etapas necessárias
print(f"O nome '{target_name}' foi {'entrado' if index != -
      1 else 'não encontrado'} na posição {index}.")
print(f"Etapas necessárias: {steps_taken}")
# imprime o número máximo de etapas possíveis
print(f"Máximo de etapas possiveis: {max_steps}")
