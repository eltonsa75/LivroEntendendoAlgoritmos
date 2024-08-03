def procure_pela_chave(caixa_principal):
    pilha = caixa_principal.crie_uma_pilha_para_buscar()
    while not pilha.vazia():
        caixa = pilha.pegue_caixa()
        for item in caixa:
            if item.e_uma_caixa():
              pilha.append(item)
            elif item.e_uma_chave():
                print ("achei a chave!")
                return

def procure_pela_chave(caixa):
    for item in caixa:
        if item.e_uma_caixa():
            procure_pela_chave(item)
        elif item.e_uma_chave():
            print ("Achei a chave!")

def regressiva(i):
    print (i)
    if i <= 1:
        return
    else:
        regressiva(i-1)