import diagrama as d

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
    dir = "Pocoes/"
    pocao = "receita1.txt"
    ingredientes = carrega_ingredientes()
    diag = d.carrega_diagrama(f"{dir}{pocao}", ingredientes)
    if diag is not None:
        diag.imprime_automato()

# Essa condicional irá executar sempre que esse arquivo for executado
# diretamente. Quando ele for incluído como uma biblioteca (no REPL, por
# exemplo), não acontecerá
if __name__ == "__main__":
    main()
