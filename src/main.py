import receita as r
import automato as a

# Lê a lista de ingredientes válidos
def carrega_ingredientes(nome_arq='ingredientes.txt'):
    num_linha = 0
    ingredientes = {}
    with open(nome_arq) as arq:
        for line in arq:
            num_linha += 1
            # Cada linha do arquivo com a lista de ingredientes deve estar
            # estruturada no formato <nome-ingrediente> : <descrição>
            nome, desc = line.split(":")
            nome = nome.strip()
            desc = desc.strip()
            if len(nome) > 4 or not nome:
                print(f"Na linha {num_linha}, lista de ingredientes {nome_arq}:"
                      "nome de ingrediente deve ter no máximo 3 caracteres")
                exit(1)
            ingredientes[nome] = desc
    return ingredientes

def main():
    dir = "poções/"
    arq_receita = "receita1.txt"
    ingredientes = carrega_ingredientes()
    receita = r.carrega_receita(f"{dir}{arq_receita}", ingredientes)
    if receita is not None:
        receita.imprime()

    # Criação de poção
    primeiro = True
    auto = a.Automato(receita)
    while True:
        if primeiro:
            ing = input("Insira o símbolo do primeiro ingrediente: ")
            if ing not in ingredientes:
                print("Ingrediente não reconhecido...")
                continue
            primeiro = False
        else:
            resp = input("Deseja inserir mais um ingrediente? (s/n) ")
            if resp != "s" and resp != "S":
                break
            ing = input("Símbolo do ingrediente: ")
            if ing not in ingredientes:
                print("Ingrediente não reconhecido...")
                continue
        auto.executa_transicao(ing)
    print("aceita" if auto.reconheceu() else "rejeita")

# Essa condicional irá executar sempre que esse arquivo for executado
# diretamente. Quando ele for incluído como uma biblioteca (no REPL, por
# exemplo), não acontecerá
if __name__ == "__main__":
    main()
