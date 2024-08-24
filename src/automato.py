from typing import List
from src.listaIngredientes import ListaIngredientes
from src.diagrama import Diagrama

# O autômato nada mais é do que um dicionário de dicionários, representando
# assim o grafo da máquina original como uma lista de adjacência
# FIXME: alguns prints foram deixados para depuração. Depois se for conveniente tirar, nós retiramos
class Automato:
    def __init__(self, diagrama: Diagrama):
        self.diagrama = diagrama
        self.estado_atual = self.diagrama.inicial # O estado de erro será com o estado_atual = None
        self.pilha = [] # Usando append e pop o vetor funciona como pilha
    
    def atualiza_estado(self, ingrediente):
        if self.estado_atual == None:
            print("> Em automato: O automato está preso no estado de erro")
            return None # Vai continuar preso ao estado atual
        resultado = self.diagrama.get_prox_estado(self.estado_atual, ingrediente, self.pilha.pop())
        if resultado == None:
            print("> Em Automato: não foi possivel realizar a transiçao")
            self.estado_atual = None
            return None
        if type(resultado) == tuple:
            estado_destino, empilha = resultado
        self.pilha.append(empilha) if (empilha != "") else None
        self.estado_atual = estado_destino
        return estado_destino 

    def cria_pocao(self):
        pass





