
# cada nó possui um nome e as transições possíveis
class Aresta:
    def __init__(self, nodeDestino, transicao):
        self.nodeDestino = nodeDestino
        self.transicao = transicao
        self.proximo = None
        
        
class ListaAdj:
    def __init__(self):
        # lista que guarda os nós e suas transições
        self.lista = list()
        