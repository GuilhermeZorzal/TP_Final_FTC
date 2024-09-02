from receita import Receita
from alfabeto import Alfabeto
import time
import os
import platform
from sound import sound_add_ingrediente, sound_game_over, sound_pocao_criada
import terminal as te  

dir = ''
if platform.system() == "Windows":
    dir = '../pocoes/'
    os.system('cls')
else:
    dir = 'pocoes/'
    os.system('clear')

def clean():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


# Realização dinâmica de um diagrama de estados
class Mealy:
    def __init__(self):
        self.descricoes = dict()
        self.le_mealy()

    def run(self, sigma: Alfabeto):
        primeiro = True
        cont = 0
        poder = 0
        sabor = 0
        while True:
            print()
            # Recebe ingrediente
            cont += 1
            if primeiro:
                ing = input(te.blue("Insira o símbolo do primeiro ingrediente: "))
                if not sigma.valida_ingrediente(ing):
                    print(te.red("Ingrediente não reconhecido..."))
                    continue
                primeiro = False
            else:
                resp = input(te.blue("Deseja inserir mais um ingrediente? (s/n) "))
                if resp.lower() != "s":
                    break
                ing = input(te.blue("Símbolo do ingrediente: "))
                if not sigma.valida_ingrediente(ing):
                    print(te.red("Ingrediente não reconhecido..."))
                    continue

            print(te.yellow(self.descricoes[ing][0]))
            sound_add_ingrediente()

            sabor += int(self.descricoes[ing][1])
            poder += int(self.descricoes[ing][2])

        clean()

        for i in range(4):
            print(te.yellow("O corvo provador pegou uma colherada e está avaliando o sabor" + "." * i))
            te.print_corvo()
            time.sleep(0.5)
            clean()
            
        if sabor < 0:
            print(te.red("O corvo desmaiou devido ao gosto terrível da poção"))
            te.print_corvo()
            input(te.white("Aperte enter para continuar..."))
            return

        if cont > 10:
            print(te.red("O corvo gralhou, disse que a poção ficou muito misturada e não conseguiu provar direito"))
            te.print_corvo()
            input(te.green("Aperte enter para continuar"))
            clean()
            return

        if poder >= 400:
            print(te.magenta("A poção é muito poderosa. O poder do corvo provador ultrapassa seu próprio poder! Ele pega o caldeirão com as próprias garras e sai voando com ele pela janela!!!"))
            te.corvo_poderoso()
            input(te.green("Aperte enter para continuar"))
            clean()
            return

        te.print_corvo()
        self.avalia_sabor(sabor)
        self.avalia_poder(poder)
        input(te.green("Aperte enter para continuar"))
        clean()

        return

    def le_mealy(self):
        with open(dir + 'mealy.txt') as arq:
            for line in arq:
                ing, descricao = line.split(':')
                ing = ing.strip()
                descricao = descricao.split("|")
                for i in descricao:
                    i = i.strip()
                self.descricoes.update({ing: descricao})

    def imprime_descricoes(self):
        for ing in self.descricoes:
            print(te.blue(f"{ing}: {self.descricoes[ing][0]}"))

    def avalia_sabor(self, sabor):
        print(te.blue("\n" + "="*50 + "\n"))
        for i in range(4):
            print(te.magenta("O corvo provador está avaliando o sabor da poção"+ "." * i))
            time.sleep(0.5)
        
        # Avaliação do sabor com formatação
        if sabor == 0:
            print(te.blue("💧 O corvo provador disse que sua poção ficou aguada. A poção carece de sabor."))
        elif sabor < 10:
            print(te.white("😐 O corvo provador disse que sua poção ficou meio sem graça. Está faltando um pouco mais de tempero."))
        elif sabor < 20:
            print(te.green("👍 O corvo provador disse que sua poção ficou muito boa. O sabor está agradável."))
        elif sabor < 40:
            print(te.blue("🌟 O corvo provador disse que sua poção ficou espetacular. Um verdadeiro deleite!"))
        else:
            print(te.red("👨‍🍳 O corvo provador disse que você deveria largar a bruxaria e virar chefe de cozinha. A poção está fantástica!"))

        print(te.blue("\n" + "="*50 + "\n"))
        time.sleep(0.8)
        

    def avalia_poder(self, poder):
        print(te.cyan("\n\n" + "="*50 + "\n"))
        
        for i in range(4):
            print(te.magenta("O corvo provador está avaliando o poder da poção"+ "." * i))
            time.sleep(0.5)
        
        if poder < 0:
            print(te.red("😵 O corvo provador desmaiou de fraqueza. A poção é extremamente fraca."))
        elif poder == 0:
            print(te.yellow("🌀 O corvo provador disse que sua poção não tem poder algum."))        
        elif poder < 50:
            print(te.orange("🔮 O corvo provador disse que sua poção tem um poder mediano."))
        elif poder < 100:
            print(te.green("⚡ O corvo provador disse que sua poção é bastante poderosa."))
        elif poder < 200:
            print(te.green("💪 O corvo provador disse que sua poção é extremamente poderosa!!!"))
        else:
            print(te.green("🌟 O corvo provador está maravilhado com o poder da poção e a considera lendária!"))

        print(te.cyan("\n" + "="*50 + "\n"))
        time.sleep(0.8)
        

