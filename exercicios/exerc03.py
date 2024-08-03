def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        if i == 1:
            print(f"Passo {i}: {resultado}")
        else:
            print(f"Passo {i}: {resultado} x {i} = {resultado * i}")
        resultado *= i
    return resultado


# Calculando o fatorial de 5
resultado_final = fatorial(5)
print(f"O fatorial de 5 é: {resultado_final}")
