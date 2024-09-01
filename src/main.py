import automato as a
import alfabeto as s
import leitura as l
import os
import platform
import mealy as m

def run_case1(sigma):
    nome_receita = input("Insira o nome da receita desejada (sem .txt)\n>> ")
    dir = "pocoes/"
    arq_receita =  dir + nome_receita + ".txt"
    
    receita = l.carrega_receita(arq_receita, sigma)
    if receita is not None:
        print(f"Receita lida do arquivo {dir}{arq_receita}\n")
        if(input("Deseja ver a receita? [s/n]\n>> ") == 's'):
            receita.imprime()
        
    if(input("Deseja ver os ingredientes disponíveis? [s/n]\n>> ") == 's'):
            sigma.lista_ingredientes()
    # Criação de poção
    primeiro = True
    auto = a.Automato(receita)
    
    while True:
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
        auto.executa_transicao(ing, sigma)
    nome_receita = nome_receita.replace("_", " ").capitalize()
    print()
    print(f"{nome_receita} criada" if auto.reconheceu() else "Falha na mistura")

def main():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
        
    resp = int(input("Qual tipo de máquina você deseja usar?\n1 - Automato Determinístico(tipo é determinado pela entrada)\n2 - Máquina de Mealy \n>> "))

    dir = "pocoes/"
    arq_ingredientes = dir + "ingredientes.txt"
    arq_reacoes = dir + "reacoes.txt"

    try:
        # Criação do alfabeto pode falhar, se um dos arquivos não existir.
        # Não tenho certeza se essa foi a melhor forma de arquitetar esse
        # comportamento; inicializadores que leem arquivos e lançam exceções
        # são um pouco estranhos. Mas funciona
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

# Essa condicional irá executar sempre que esse arquivo for executado
# diretamente. Quando ele for incluído como uma biblioteca (no REPL, por
# exemplo), não acontecerá
if __name__ == "__main__":
    main()
