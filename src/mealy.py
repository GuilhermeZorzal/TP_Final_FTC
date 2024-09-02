from receita import Receita
from alfabeto import Alfabeto
import time
import os
import platform
from sound import sound_add_ingrediente, sound_game_over, sound_pocao_criada
import terminal

dir = ''
if platform.system() == "Windows":
    dir = '../pocoes/'
    os.system('cls')
else:
    dir = 'pocoes/'
    os.system('clear')
# Realização dinâmica de um diagrama de estados
class Mealy:
    def __init__(self):
        self.descricoes = dict()
        self.le_mealy()

    def run(self, sigma : Alfabeto):
        primeiro = True
        cont = 0
        poder = 0
        sabor = 0
        while True:
            # Recebe ingrediente
            cont+=1
            if primeiro:
                ing = input("Insira o símbolo do primeiro ingrediente: ")
                if not sigma.valida_ingrediente(ing):
                    print("Ingrediente não reconhecido...")
                    continue
                primeiro = False
                sound_add_ingrediente()
            else:
                resp = input("Deseja inserir mais um ingrediente? (s/n) ")
                if resp != "s" and resp != "S":
                    break
                ing = input("Símbolo do ingrediente: ")
                if not sigma.valida_ingrediente(ing):
                    print("Ingrediente não reconhecido...")
                    continue
                sound_add_ingrediente()
            # print(self.descricoes[ing])
            sabor += int(self.descricoes[ing][1])
            poder += int(self.descricoes[ing][2])                
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
        for i in range(4):
            print("O corvo provador pegou uma colherada e está avaliado o sabor" + "." * i)
            terminal.print_corvo()
            
            time.sleep(0.5)
            if platform.system() == "Windows":
                os.system('cls')
            else:
                os.system('clear')
        
        if sabor < 0:
            print("O corvo desmaiou defido ao gosto terrível da poção")
            terminal.print_corvo()
            input("Aperte enter para continuar")
            return
        if cont > 10:
            print("O corvo gralhou, disse que a poção ficou muito misturada e nao conseguiu provar direito")
            terminal.print_corvo()
            input("Aperte enter para continuar")
            if platform.system() == "Windows":
                os.system('cls')
            else:
                os.system('clear')
            return        
        if poder >= 400:
            print("O pocao é muito poderosa. O poder do corvo provador ultrapassa seu próprio poder! ele pega o caldeirão com as próprias garras e sai voando com ele pela janela!!!")
            terminal.corvo_poderoso()
            input("Aperte enter para continuar")
            if platform.system() == "Windows":
                os.system('cls')
            else:
                os.system('clear')
            return
        terminal.print_corvo()
        self.avalia_sabor(sabor)
        self.avalia_poder(poder)
        input("Aperte enter para continuar")
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
        
        return

    
    def le_mealy(self):
        with open(dir + 'mealy.txt') as arq:
            for line in arq:
                ing, descricao = line.split(':')
                ing = ing.strip()
                descricao = descricao.split("|")
                for i in descricao:
                    i = i.strip()
                self.descricoes.update({ing : descricao})
    def imprime_descricoes(self):
        for ing in self.descricoes:
            print(f"{ing}: {self.descricoes[ing][0]}")
        
    def avalia_sabor(self,sabor):
        if sabor == 0:
            print("O corvo provador disse que sua poção ficou aguada")
            return
        elif sabor < 10:
            print("O corvo provador disse que sua pocao ficou meio sem graça")
            return
        elif sabor < 20:
            print("O corvo provador disse que sua pocao ficou muito boa")
            return
        elif sabor < 40:
            print("O corvo provador disse que sua pocao ficou espetacular")
            return
        elif sabor >= 60:
            print("O corvo provador disse que voce deveria largar a bruxaria e virar chefe de cozinha")
            return
    def avalia_poder(self,poder):
        if poder < 0:
            print("O corvo provador desmaiou de fraqueza")
            return
        elif poder == 0:
            print("O corvo provador disse que sua pocao nao tem poder algum")
            return
        elif poder < 50:
            print("O corvo provador disse que sua pocao tem um poder mediano")
            return
        elif poder < 100:
            print("O corvo provador disse que sua pocao é bastante poderosa")
            return
        elif poder < 200:
            print("O corvo provador disse que sua pocao é extremamente poderosa!!!")
            return
        



        
