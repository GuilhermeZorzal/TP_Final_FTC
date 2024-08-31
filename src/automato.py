from receita import Receita
from alfabeto import Alfabeto
# Realização dinâmica de um diagrama de estados
class Automato:
    def __init__(self, receita: Receita):
        self.erro = False
        self.receita = receita
        self.estado_atual = receita.inicial
        self.pilha = []

    # Retorna o topo da pilha ou palavra vazia se ela estiver vazia
    def topo_pilha(self):
        return self.pilha.pop() if self.pilha else "_"

    # Executa uma transição
    def executa_transicao(self, ingrediente, reacoes: Alfabeto):
        if self.erro: return
        regras = self.receita.estados[self.estado_atual].regras
        if ingrediente not in regras:
            # Sem transição para o ingrediente fornecido; erro
            self.erro = True
            return
        saida = regras[ingrediente]
        if isinstance(saida, dict):
            # Transição de autômato de pilha!
            topo = self.topo_pilha()
            if topo not in saida and "_" not in saida:
                # Sem transição para o topo atual da pilha; erro
                self.erro = True
                return
            if "_" in saida and "_" != topo:
                print(f"Mmmmm essa poção parece {reacoes.descreve_reacao(topo)}\n")
                self.pilha.append(topo)
                topo = "_"
            saida, empilha = saida[topo]
            if empilha != "_":
                print(f"Mmmmm essa poção parece {reacoes.descreve_reacao(empilha)}\n")
                self.pilha.append(empilha)
            if not self.pilha:
                print(f"A poção parece boa\n")
        # Mudamos para o próximo estado!
        self.estado_atual = saida

    # Checa se a computação foi corretamente concluída
    def reconheceu(self):
        return not self.erro and self.estado_atual in self.receita.finais and not self.pilha

    def run(self, sigma : Alfabeto, nome_receita: str):
        primeiro = True
        while True:
            # Recebe ingrediente
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
            self.executa_transicao(ing, sigma)
        nome_receita = nome_receita.replace("_", " ").capitalize()
        print()
        print(f"{nome_receita} criada" if self.reconheceu() else "Falha na mistura")