from diagrama import Diagrama

# Realização dinâmica de um diagrama de estados
class Automato:
    def __init__(self, diag: Diagrama):
        self.erro = False
        self.diagrama = diag
        self.estado_atual = diag.inicial
        self.pilha = []

    # Retorna o topo da pilha ou palavra vazia se ela estiver vazia
    def topo_pilha(self):
        if not self.pilha:
            return "_"
        return self.pilha.pop()

    # Executa uma transição
    def executa_transicao(self, ingrediente):
        if self.erro: return
        trans = self.diagrama.estados[self.estado_atual]
        if ingrediente not in trans:
            # Sem transição para o ingrediente fornecido; erro
            self.erro = True
            return
        saida = trans[ingrediente]
        if saida is dict:
            # Transição de autômato de pilha!
            topo = self.topo_pilha()
            if topo not in saida:
                # Sem transição para o topo atual da pilha; erro
                self.erro = True
                return
            saida, empilha = saida[topo]
            self.pilha.append(empilha)
        # Mudamos para o próximo estado!
        self.estado_atual = saida

    # Checa se a computação foi concluída
    def terminou(self):
        return (self.estado_atual in self.diag.finais) and (not self.pilha)

