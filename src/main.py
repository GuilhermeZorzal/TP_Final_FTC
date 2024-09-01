import automato as a
import alfabeto as s
import leitura as l
import os
import platform
import mealy as m
from sound import sound_game_over, sound_pocao_criada, sound_add_ingrediente, sound_background, stop_background_sound
import terminal as te

# Antes de tudo rode o comando pip install pygame

def run_case1(sigma):
    while 1:
        nome_receita = input(te.blue("Insira o nome da receita desejada (sem .txt)\n>> "))
        dir = "pocoes/"
        arq_receita = dir + nome_receita + ".txt"
        try:
            receita = l.carrega_receita(arq_receita, sigma)
            break
        except Exception as e:
            print(te.red(f"[!] Erro ao carregar a receita. Erro: {e}"))
            continue
        
    if receita is not None:
        print(te.yellow(f"Receita lida do arquivo {dir}{arq_receita}\n"))
        if input(te.blue("Deseja ver a receita? [s/n]\n>> ")) == 's':
            receita.imprime()
        
    if input(te.blue("Deseja ver os ingredientes disponíveis? [s/n]\n>> ")) == 's':
        sigma.lista_ingredientes()
    
    primeiro = True
    auto = a.Automato(receita)
    
    te.print_criandoPoceos()
    
    while True:
        if primeiro:
            ing = input(te.yellow("Insira o símbolo do primeiro ingrediente: "))
            if not sigma.valida_ingrediente(ing):
                print(te.red("Ingrediente não reconhecido...\nEstado I"))
                sound_game_over()  # Toca o som de game over para ingredientes inválidos
                continue
            primeiro = False
        else:
            resp = input(te.green("\nDeseja inserir mais um ingrediente? (s/n) "))
            if resp.lower() != "s":
                break
            ing = input(te.yellow("Símbolo do ingrediente: "))
            if not sigma.valida_ingrediente(ing):
                print(te.red("Ingrediente não reconhecido...\nEstado I"))
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
        te.print_perde()
        sound_game_over()  # Toca o som de game over se a mistura falhar
        exit(1)

def main():
    sound_background()  # Começa a música de fundo
    
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

    te.print_title()
    te.print_menu()
    
    resp = int(input(te.blue("Escolha uma opção:\n>> ")))

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

    te.print_fim() 
    # Para a música de fundo ao final
    stop_background_sound()

if __name__ == "__main__":
    main()
