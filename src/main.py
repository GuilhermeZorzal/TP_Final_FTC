import automato as a
import alfabeto as s
import leitura as l
import os
import platform
import mealy as m
from sound import sound_game_over, sound_pocao_criada, sound_add_ingrediente, sound_background, stop_background_sound
from terminal import print_title, print_menu

# Antes de tudo rode o comando pip install pygame

def run_case1(sigma):
    nome_receita = input("Insira o nome da receita desejada (sem .txt)\n>> ")
    dir = "pocoes/"
    arq_receita = dir + nome_receita + ".txt"
    
    receita = l.carrega_receita(arq_receita, sigma)
    if receita is not None:
        print(f"Receita lida do arquivo {dir}{arq_receita}\n")
        if input("Deseja ver a receita? [s/n]\n>> ") == 's':
            receita.imprime()
        
    if input("Deseja ver os ingredientes disponíveis? [s/n]\n>> ") == 's':
        sigma.lista_ingredientes()
    
    primeiro = True
    auto = a.Automato(receita)
    
    while True:
        if primeiro:
            ing = input("Insira o símbolo do primeiro ingrediente: ")
            if not sigma.valida_ingrediente(ing):
                print("Ingrediente não reconhecido...\nI")
                sound_game_over()  # Toca o som de game over para ingredientes inválidos
                continue
            primeiro = False
        else:
            resp = input("Deseja inserir mais um ingrediente? (s/n) ")
            if resp.lower() != "s":
                break
            ing = input("Símbolo do ingrediente: ")
            if not sigma.valida_ingrediente(ing):
                print("Ingrediente não reconhecido...\nI")
                sound_game_over()  # Toca o som de game over para ingredientes inválidos
                continue
        auto.executa_transicao(ing, sigma)
        sound_add_ingrediente()  # Toca o som quando um ingrediente é adicionado
    
    nome_receita = nome_receita.replace("_", " ").capitalize()
    print()
    if auto.reconheceu():
        print(f"{nome_receita} criada")
        sound_pocao_criada()  # Toca o som quando a poção é criada
    else:
        print("Falha na mistura")
        sound_game_over()  # Toca o som de game over se a mistura falhar

def main():
    sound_background()  # Começa a música de fundo
    
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

    print_title()
    print_menu()
    
    resp = int(input("Escolha uma opção:\n>> "))

    dir = "pocoes/"
    arq_ingredientes = dir + "ingredientes.txt"
    arq_reacoes = dir + "reacoes.txt"

    try:
        sigma = s.Alfabeto(arq_ingredientes, arq_reacoes)
    except Exception as e:
        print(f"> alfabeto.py: [!] Erro ao criar o alfabeto. Erro: {e}")
        exit(1)

    match resp:
        case 1:
            run_case1(sigma)
        case 2:
            mealy = m.Mealy()
            mealy.run(sigma)

    # Para a música de fundo ao final
    stop_background_sound()

if __name__ == "__main__":
    main()
