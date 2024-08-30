import automato as a
import alfabeto as s
import leitura as l
import os
import platform


def main():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
    
    nome_receita = input("Insira o nome da receita desejada\n>> ")
    
    dir = "poções/"
    arq_receita = dir + nome_receita + ".txt"
    arq_ingredientes = dir + "ingredientes.txt"
    arq_reacoes = dir + "reações.txt"

    try:
        # Criação do alfabeto pode falhar, se um dos arquivos não existir.
        # Não tenho certeza se essa foi a melhor forma de arquitetar esse
        # comportamento; inicializadores que leem arquivos e lançam exceções
        # são um pouco estranhos. Mas funciona
        sigma = s.Alfabeto(arq_ingredientes, arq_reacoes)
    except: exit(1)

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

# Essa condicional irá executar sempre que esse arquivo for executado
# diretamente. Quando ele for incluído como uma biblioteca (no REPL, por
# exemplo), não acontecerá
if __name__ == "__main__":
    main()
