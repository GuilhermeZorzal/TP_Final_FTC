import src.diagrama as diagramas
from src.listaIngredientes import ListaIngredientes
from src.automato import Automato

def main():
    dir = "Pocoes/"
    pocao = "receita1.txt"
    afd = diagramas.leia_automato(dir + pocao)
    if afd is not None:
        afd.imprime_automato()
    auto = Automato(afd)
    auto.cria_pocao()

# Essa condicional irá executar sempre que esse arquivo for executado
# diretamente. Quando ele for incluído como uma biblioteca (no REPL, por
# exemplo), não acontecerá
if __name__ == "__main__":
    main()
