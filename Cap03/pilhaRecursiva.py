def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x - 1)
resultado = fat(5)
print(resultado)