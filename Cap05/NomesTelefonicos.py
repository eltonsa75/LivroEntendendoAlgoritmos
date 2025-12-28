# Mapeamento de letras para números primos
PRIMOS = {
    'A': 2,  'B': 3,  'C': 5,  'D': 7,  'E': 11,
    'F': 13, 'G': 17, 'H': 19, 'I': 23, 'J': 29,
    'K': 31, 'L': 37, 'M': 41, 'N': 43, 'O': 47,
    'P': 53, 'Q': 59, 'R': 61, 'S': 67, 'T': 71,
    'U': 73, 'V': 79, 'W': 83, 'X': 89, 'Y': 97,
    'Z': 101
}

TAMANHO_TABELA = 10


def funcao_hash(nome: str) -> int:
    soma = 0
    for letra in nome.upper():
        soma += PRIMOS.get(letra, 0)
    return soma % TAMANHO_TABELA


class TabelaHash:
    def __init__(self):
        self.tabela = [[] for _ in range(TAMANHO_TABELA)]

    def inserir(self, nome: str, telefone: str):
        indice = funcao_hash(nome)
        self.tabela[indice].append((nome, telefone))

    def buscar(self, nome: str):
        indice = funcao_hash(nome)
        for chave, valor in self.tabela[indice]:
            if chave == nome:
                return valor
        return None

    def exibir(self):
        for i, lista in enumerate(self.tabela):
            print(f"{i}: {lista}")


agenda = TabelaHash()

agenda.inserir("Esther", "9999-1111")
agenda.inserir("Ben", "9888-2222")
agenda.inserir("Bob", "9777-3333")
agenda.inserir("Dan", "9666-4444")
agenda.inserir("Elton", "9555-5555")
agenda.inserir("William", "9444-6666")

agenda.exibir()

telefone = agenda.buscar("William")
print("Telefone do William:", telefone)

