# Array com 5 elementos

array = [2, 3, 7, 8, 10]

# Criar a tabela de multiplicação e multiplicar cada valor por 7
print("Tabela de Multiplicação (valores multiplicados por 7):")
print("    ", end="")  # Espaço inicial para a primeira linha
for i in array:
    print(f"{i:4}", end="")  # Alinhamento de 4 espaços para as colunas
print()  # Nova linha após a impressão das colunas de título

for i in array:
    print(f"{i:2} |", end="")  # Alinha a primeira coluna
    for j in array:
        print(f"{i * j * 7:4}", end="")  # Multiplica cada resultado por 7
    print()  # Nova linha após cada linha da tabela
