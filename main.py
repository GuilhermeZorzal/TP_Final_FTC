import src.diagrama as diagramas
from src.listaIngredientes import ListaIngredientes

def main():
    dir = "Pocoes/"
    pocao = "receita1.txt"
    afd = diagramas.leia_automato(dir + pocao)
    if afd is not None:
        afd.imprime_automato()
    lista = dict()
    lista.update({"dsa":"dsafagsg"})
    # lista = ListaIngredientes()
    # lista.geraLista()
    # lista.imprimeIngredientes()
    # lista.adicionarItem("aaa", "Jarro com grito de desespero")
    # lista.imprimeIngredientes()

# Essa condicional irá executar sempre que esse arquivo for executado
# diretamente. Quando ele for incluído como uma biblioteca (no REPL, por
# exemplo), não acontecerá
if __name__ == "__main__":
    main()
