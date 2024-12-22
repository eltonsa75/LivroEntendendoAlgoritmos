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

# Adicionando os dados
hash_table = HashTable(10)
hash_table.insert("maçã", 0.67)
hash_table.insert("leite", 1.49)
hash_table.insert("abacate", 1.49)

# Exibindo a tabela hash
print("Tabela Hash:")
hash_table.display()

# Consultando os valores
print("\nValor associado à chave 'maçã':", hash_table.get("maçã"))
print("Valor associado à chave 'leite':", hash_table.get("leite"))
print("Valor associado à chave 'abacate':", hash_table.get("abacate"))

