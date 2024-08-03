from prettytable import PrettyTable #Importa a classe PrettyTabel para criar e formatar
from termcolor import colored #Importa a função colored para colorir o texto no terminal

 # Função para realizar a busca binária em uma lista ordenada
def binary_search02(arr, x):

    left, right = 0, len(arr) - 1 # Define os limites inicial e final da busca

    while left <= right: # enquanto o limite esquerdo não ultrapassar o direito
        mid = (left + right) // 2 # Calcula o índice do meio 
        mid_val = arr[mid] # Obtém o valor no índice

        if mid_val == x: # se o valor do meio é igual ao valor procurado, retorna o índice
            return mid
        elif mid_val < x: # Se o valor do meio é menor que o valor procurado, ajusta o limite esquerdo
            left = mid + 1
        else: # Se o valor do meio é maior que valor procurado, ajusta o limite direito
            right = mid - 1

    return -1 # retorna -1 se o valor não for encontrado


# Lista de nomes ordenadas
names = ["Alice", "Bob", "Charlie", "David", "Eve",
         "Frank", "Grace", "Hannah", "Ivy", "Jhon"]


# Nome a ser pesquisado
search_name = "Grace"

# Executar a pesquisa binária para encontrar o nome na lista
result = binary_search02(names, search_name)

# criar uma tabela para exibir os resultados
table = PrettyTable()
table.filed_names = ["Posição", "Nome"] # Define os cabeçalhos das colunas da tabela


# Adicionar os nomes á tabela, destancando o nome encontrado
for i, name in enumerate(names):
    if i == result: #Se o índice correspopnde ao resultado da busca
        table.add_row([i, colored(name, 'red')]) # Destaca o nome em vermelho
    else:
        table.add_row([i, name]) # Adiciona o nome normalmente

#imprime a tabela no terminal 
print(table)

# Exibe uma mensagem indiciando se o nome foi encotrnado e sua posição
if result != -1:
    print(f"Nome '{search_name}' econtrado na posição {result}.")
else:
    print(f" Nome '{search_name}' não econtrado.")
