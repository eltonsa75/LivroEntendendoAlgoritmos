votaram = {}

valor = votaram.get("tom")

voted = {}

def verifica_eleitor(nome):
    if votaram.get(nome):
        print ("Mande embora!")
    else:
        voted[nome] = True
        print ("Deixe votar!")


verifica_eleitor("tom")

verifica_eleitor("mike")