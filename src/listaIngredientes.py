class ListaIngredientes:
    def __init__(self) -> None:
        self.lista = dict()
        pass
    
    def geraLista(self, path='Pocoes/ingredientes.txt'):
        with open(path) as arq:
            for line in arq:
                chave, ingrediente = line.split(":")
                chave = chave.strip()
                ingrediente = ingrediente.strip()
                if len(chave) > 4 or not chave:
                    print("> Em listaIngredientes.py: o formato de entrada não é válido: a chave dos elementos deve ter no máximo 3 caracteres")
                    return
                if '\n' in ingrediente:
                    print("> Em lsitaIngredientes.py: formato de ingrediente não permitido. Veja mais intruções no README")
                    return
                self.lista.update({chave : ingrediente})

    def adicionarItem(self, chave, ingrediente):
        self.lista.update({chave : ingrediente})
    
    def imprimeIngredientes(self):
        print("======================")
        print("LISTA DE INGREDIENTES:")
        print("======================")
        for ingrediente in self.lista.keys():
            print(ingrediente, ":", self.lista[ingrediente])
            print("----------------------------")
    def removeItem(self, chave):
        self.lista.pop(chave)
    def getItem(self, chave):
        if chave not in self.lista.keys():
            print("> Em listaIngredientes.py: chave não encontrada")
            return None
        return self.lista[chave]
