import ListaAdjacencia as la


def main():
    
    afd = la.Automato()
    
    path = "Pocoes/"
    pocao = "receita1.txt"
    path = path + pocao
    texto = open(path)
    
    afd.constroi_automato(texto)
    afd.imprime_automato()
    
    
main()
