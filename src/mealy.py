from receita import Receita
from alfabeto import Alfabeto

# Realização dinâmica de um diagrama de estados
class Mealy:
    def __init__(self, receita: Receita):
        self.estado_atual = receita.inicial
        self.descricoes = dict()
        self.le_mealy()

    def run(self, sigma : Alfabeto):
        primeiro = True

        while True:
            # Recebe ingrediente
            if primeiro:
                ing = input("Insira o símbolo do primeiro ingrediente: ")
                if not sigma.valida_ingrediente(ing):
                    print("Ingrediente não reconhecido...")
                    continue
                primeiro = False
            else:
                resp = input("Deseja inserir mais um ingrediente? (s/n) ")
                if resp != "s" and resp != "S":
                    break
                ing = input("Símbolo do ingrediente: ")
                if not sigma.valida_ingrediente(ing):
                    print("Ingrediente não reconhecido...")
                    continue
            print(self.descricoes[ing])

    
    def le_mealy(self):
        with open('../poções/mealy.txt') as arq:
            for line in arq:
                ing, descricao = line.split(':')
                ing = ing.strip()
                descricao = descricao.strip()
                self.descricoes.update({ing : descricao})
    def imprime_descricoes(self):
        for ing in self.descricoes:
            print(f"{ing}: {self.descricoes[ing]}")
        


        
