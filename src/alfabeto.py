# Carrega um alfabeto de um arquivo sabendo sua natureza (ingredientes, reações, etc.)
# Cada entrada no arquivo deve ter a forma <símbolo>:<descrição>
def carrega_alfabeto(nome_arq, natureza):
    num_linha = 0
    alfabeto = {}
    with open(nome_arq) as arq:
        for line in arq:
            num_linha += 1
            # Cada linha do arquivo com a lista de ingredientes deve estar
            # estruturada no formato <nome>:<descrição>
            sim, desc = line.split(":")
            sim = sim.strip()
            desc = desc.strip()
            if len(sim) >= 4 or not sim:
                print(f"Na linha {num_linha}, lista de {natureza} '{nome_arq}':"
                      "símbolo deve ter entre 1 e 3 caracteres")
                exit(1)
            alfabeto[sim] = desc
    return alfabeto

# Classe que agrupa todos os símbolos permitidos no programa, incluindo
# ingredientes e reações. Usado para validação
class Alfabeto:
    def __init__(self, arq_ingredientes, arq_reacoes):
        try:
            self.ingredientes = carrega_alfabeto(arq_ingredientes, "ingredientes")
        except FileNotFoundError:
            print(f"[!] Não foi possível abrir o arquivo {arq_ingredientes}")
            raise ValueError
        try:
            self.reacoes = carrega_alfabeto(arq_reacoes, "reações")
        except FileNotFoundError:
            print(f"[!] Não foi possível abrir o arquivo {arq_reacoes}")
            raise ValueError

    def valida_ingrediente(self, ing):
        return ing == "_" or ing in self.ingredientes

    def descreve_ingrediente(self, ing):
        return self.ingredientes.get(ing, "")

    def valida_reacao(self, re):
        return re == "_" or re in self.reacoes

    def descreve_reacao(self, re):
        return self.reacoes.get(re, "")
    
    def lista_ingredientes(self):
        print("\tIngredientes na mesa:")
        for chave, valor in self.ingredientes.items():
            print(f"{chave}: {valor}")
        print()
