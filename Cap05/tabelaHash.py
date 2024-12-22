

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = []
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

    def delete(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            self.table[index] = [(k, v) for k, v in self.table[index] if k != key]

    def display(self):
        for i, entries in enumerate(self.table):
            print(f"Index {i}: {entries}")

# Criação de um dicionário (tabela hash nativa do Python)
caderno = {}

# Inserindo dados
caderno["maçã"] = 0.67
caderno["leite"] = 1.49
caderno["abacate"] = 1.49

# Exibindo a tabela hash
print("Tabela Hash (dicionário):")
for chave, valor in caderno.items():
    print(f"Chave: {chave}, Valor: {valor}")

# Recuperando valores associados às chaves
print("\nValores recuperados:")
print(f"Valor associado à chave 'maçã': {caderno['maçã']}")
print(f"Valor associado à chave 'leite': {caderno['leite']}")
print(f"Valor associado à chave 'abacate': {caderno['abacate']}")

