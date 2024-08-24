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
        print(self.pilha.__len__())
        top_pilha = self.pilha.pop() if self.pilha.__len__() != 0 else ""
        resultado = self.diagrama.get_prox_estado(self.estado_atual, ingrediente, top_pilha)
        print("Resultado avanco de estado", resultado)
        if resultado == None:
            print("> Em Automato: não foi possivel realizar a transiçao")
            self.estado_atual = None
            return None
        if type(resultado) == tuple:
            estado_destino, empilha = resultado
            self.pilha.append(empilha) if (empilha != "") else None
        else:
            estado_destino = resultado
        self.estado_atual = estado_destino
        print(f"Avançado para estado {estado_destino}")
        return estado_destino 

    def cria_pocao(self):
        while(True):
            print("\nQual ingrediente voce deseja colocar na pocao (digite 'exit' para terminar)?\n>>> ", end="")
            ingrediente = input()
            if ingrediente == "exit":
                self.resultado_pocao()
                break
            else:
                self.atualiza_estado(ingrediente)

    def resultado_pocao(self):
        if self.estado_atual == None:
            print("Oh nao, a pocao deu errado e explodiu !!!!")
            # TODO: talvez colocar uma classe de mensagens aleatorias
        else:
            if self.estado_atual in self.diagrama.finais:
                print("pocao criada com sucesso!!!")
            else:
                print("A pocao não foi preparada corretamente!!!")

