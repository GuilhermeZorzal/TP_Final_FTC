import automato as a
import alfabeto as s
import leitura as l
import os
import platform
import mealy as m


def main():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
    
    resp = int(input("Qual tipo de máquina você deseja usar?\n1 - Automato Determinístico(tipo é determinado pela entrada)\n2 - Máquina de Mealy \n>> "))
    dir = "../poções/"

    arq_ingredientes = dir + "ingredientes.txt"
    arq_reacoes = dir + "reações.txt"

    try:
        # Criação do alfabeto pode falhar, se um dos arquivos não existir.
        # Não tenho certeza se essa foi a melhor forma de arquitetar esse
        # comportamento; inicializadores que leem arquivos e lançam exceções
        # são um pouco estranhos. Mas funciona
        sigma = s.Alfabeto(arq_ingredientes, arq_reacoes)
    except: exit(1)

    match resp:
        case 1:
            nome_receita = input("Insira o nome da receita desejada\n>> ")
            arq_receita = dir + nome_receita + ".txt"

            receita = l.carrega_receita(arq_receita, sigma)
            if receita is not None:
                print(f"Receita lida do arquivo {arq_receita}\n")
                if(input("Deseja ver a receita? [s/n]\n>> ") == 's'):
                    receita.imprime()
                
            if(input("Deseja ver os ingredientes disponíveis? [s/n]\n>> ") == 's'):
                    sigma.lista_ingredientes()
                    automato = a.Automato(receita)  
                    automato.run(sigma, nome_receita)
        case 2:
            mealy = m.Mealy()
            mealy.run(sigma)
    



# Essa condicional irá executar sempre que esse arquivo for executado
# diretamente. Quando ele for incluído como uma biblioteca (no REPL, por
# exemplo), não acontecerá
if __name__ == "__main__":
    main()

