from receita import Receita

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
    def executa_transicao(self, ingrediente):
        if self.erro: return
        trans = self.receita.estados[self.estado_atual]
        if ingrediente not in trans:
            # Sem transição para o ingrediente fornecido; erro
            self.erro = True
            return
        saida = trans[ingrediente]
        if isinstance(saida, dict):
            # Transição de autômato de pilha!
            topo = self.topo_pilha()
            if topo not in saida:
                # Sem transição para o topo atual da pilha; erro
                self.erro = True
                return
            saida, empilha = saida[topo]
            if empilha != "_":
                self.pilha.append(empilha)
        # Mudamos para o próximo estado!
        self.estado_atual = saida

    # Checa se a computação foi corretamente concluída
    def reconheceu(self):
        return not self.erro and self.estado_atual in self.diag.finais and not self.pilha
