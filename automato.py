from typing import List

# Essa classe deixa mais claro que estamos trabalhando com transições
class Transicoes:
    def __init__(self):
        # Os estados guardam apenas as transições que possuem;
        # seus nomes estão no autômato em si
        self.transicoes = dict()

    def insere_transicao(self, estado_destino, ingrediente):
        self.transicoes[ingrediente] = estado_destino


# O autômato nada mais é do que um dicionário de dicionários, representando
# assim o grafo da máquina original como uma lista encadeada
class Automato:
    def __init__(self, estados: List[str], inicial: str, finais: List[str]):
        self.estados = dict()
        for estado in estados:
            self.estados[estado] = Transicoes()
        self.inicial = inicial
        self.finais = finais

    def insere_transicao(self, estado_partida, estado_destino, ingrediente):
        self.estados[estado_partida].insere_transicao(estado_destino, ingrediente)

    def imprime_automato(self):
        for estado in self.estados.keys():
            print(estado)
            for ing, est in self.estados[estado].transicoes.items():
                print("\t", ing, "->", est)


# Lê a especificação de um autômato do arquivo no caminho especificado
def leia_automato(nome_arquivo: str) -> Automato:
    from sys import stderr
    with open(nome_arquivo) as arq:
        # Leitura dos estados da máquina
        linha_estados = arq.readline().strip()
        if not linha_estados.startswith("Q:"):
            print(f"[!] Em {nome_arquivo}: primeira linha deve especificar os estados", file=stderr)
            print("Formato: 'Q:' seguido pela lista de estados, separados por espaços", file=stderr)
            return None
        estados = linha_estados[2:].split()

        # Leitura do estado inicial da máquina
        linha_inicial = arq.readline().strip()
        if not linha_inicial.startswith("I:"):
            print(f"[!] Em {nome_arquivo}: segunda linha deve especificar o estado inicial", file=stderr)
            print("Formato: 'I:' seguido nome do estado inicial", file=stderr)
            return None
        estado_inicial = linha_inicial[2:].lstrip()
        if not estado_inicial in estados:
            print(f"[!] Em {nome_arquivo}: estado inicial desconhecido", file=stderr)
            return None

        # Leitura dos estados finais da máquina
        linha_finais = arq.readline().strip()
        if not linha_finais.startswith("F:"):
            print(f"[!] Em {nome_arquivo}: segunda linha deve especificar os estado finais", file=stderr)
            print("Formato: 'F:' seguido pela lista de estados finais, separados por espaços", file=stderr)
            return None
        # Múltiplos estados finais são possíveis
        estados_finais = linha_finais[2:].split()
        for estado_final in estados_finais:
            if not estado_final in estados:
                print(f"[!] Em {nome_arquivo}: estado final {estado_final} desconhecido", file=stderr)
                return None

        cont_linha = 3
        print("Estados:", estados)
        auto = Automato(estados, estado_inicial, estados_finais)
        # Leitura das transições
        while True:
            # Se a gente tivesse certeza que o programa seria executado em
            # python 3.10+, daria pra usar o operador walrus (:=) aqui e seria
            # lindo. Por compatibilidade, não vou fazer isso
            cont_linha += 1
            linha = arq.readline()
            if linha == "---\n" or not linha:
                break
            trans = linha.split("->")
            if len(trans) != 2:
                print(f"[!] Transição inválida: {linha}", endl="", file=stderr)
                print("Formato: [estado] -> [estado_destino] | [ingrediente]", file=stderr)
                continue

            estado_partida = trans[0].strip()
            if estado_partida not in estados:
                print(f"[!] Em {nome_arquivo}, linha {cont_linha}: estado {estado_partida} desconhecido", file=stderr)
                continue

            saida = trans[1].split("|")
            if len(saida) != 2:
                print(f"[!] Transição inválida: {linha}", endl="", file=stderr)
                print("Formato: [estado] -> [estado_destino] | [ingrediente]", file=stderr)
                continue

            estado_destino = saida[0].strip()
            if estado_destino not in estados:
                print(f"[!] Em {nome_arquivo}, linha {cont_linha}: estado {estado_destino} desconhecido", file=stderr)
                continue

            ingrediente = saida[1].strip() # TODO: validar o ingrediente
            auto.insere_transicao(estado_partida, estado_destino, ingrediente)

        return auto
