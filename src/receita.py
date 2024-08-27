# Transições para um único estado
class Transicoes:
    def __init__(self):
        # Os estados guardam apenas as transições que possuem;
        # seus nomes estão no autômato em si
        self.transicoes = dict()

    def insere_transicao(self, estado_destino, ingrediente,
                         desempilha=None, empilha=None):
        """
        Insere um transição qualquer, decidindo se ela é de AFD ou de APD
        baseando-se na presença ou ausência dos argumentos empilha e desempilha
        """
        if not desempilha and not empilha:
            self.insere_transicao_afd(estado_destino, ingrediente)
            return
        self.insere_transicao_apd(estado_destino, ingrediente,
                                  desempilha, empilha)

    def insere_transicao_afd(self, estado_destino, ingrediente):
        """
        Insere uma transição de AFD, em que a leitura de um ingrediente
        leva do estado atual para um estado de destino.
        """
        self.transicoes[ingrediente] = estado_destino

    def insere_transicao_apd(self, estado_destino, ingrediente,
                             desempilha, empilha):
        """
        Insere uma transição de APD, em que a leitura de um ingrediente e o
        símbolo no topo da pilha ("desempilha") levam do estado atual para um
        estado de destino, empilhando um símbolo ("empilha")
        """
        if ingrediente not in self.transicoes:
            self.transicoes[ingrediente] = dict()
        elif not isinstance(self.transicoes[ingrediente], dict):
            # Caso particular meio complicado aqui. Pode ser que uma transição
            # para esse ingrediente tenha sido inserida como AFD. Precisamos
            # converter a posição na lista desse ingrediente em um dicionário
            # antes de mais nada
            estado_destino = self.transicoes[ingrediente]
            self.transicoes[ingrediente] = dict()
            self.transicoes[ingrediente]["_"] = (estado_destino, "_")

        self.transicoes[ingrediente][desempilha] = (estado_destino, empilha)


# A receita nada mais é do que a especificação de um autômato
class Receita:
    def __init__(self, estados, inicial, finais):
        self.estados = dict()
        for estado in estados:
            self.estados[estado] = Transicoes()
        self.inicial = inicial
        self.finais = finais

    def insere_transicao(self, estado_partida, estado_destino, ing,
                         desempilha=None, empilha=None):
        self.estados[estado_partida].insere_transicao(estado_destino, ing,
                                                      desempilha, empilha)

    def imprime(self):
        for estado in self.estados:
            print(estado)
            for ing, saida in self.estados[estado].transicoes.items():
                if not isinstance(saida, dict):
                    # Transição de AF: simples e direta
                    print(f"\t{ing} -> {saida}")
                else:
                    # Múltiplas transições de AP
                    for desempilha, (estado_destino, empilha) in saida.items():
                        print(f"\t{ing}, {desempilha} -> {estado_destino} / {empilha}")


# Imprime formato de uma transição
def imprime_formato():
    print("Formato: {estado} -> {estado_destino} | {ingrediente}"
          " [, {topo-pilha} / {empilha}]")

# Lê a especificação de um autômato do arquivo no caminho especificado
def carrega_receita(nome_arq: str, ingredientes) -> Receita:
    with open(nome_arq) as arq:
        # Leitura dos estados da máquina
        linha_estados = arq.readline().strip()
        if not linha_estados.startswith("Q:"):
            print(f"[!] Em {nome_arq}: primeira linha deve especificar"
                  " os estados\nFormato: 'Q:' seguido pela lista de estados,"
                  " separados por espaços")
            return None
        estados = linha_estados[2:].split()

        # Leitura do estado inicial da máquina
        linha_inicial = arq.readline().strip()
        if not linha_inicial.startswith("I:"):
            print(f"[!] Em {nome_arq}: segunda linha deve especificar o"
                  " estado inicial\nFormato 'I:' seguido do nome do estado"
                  " inicial")
            return None
        estado_inicial = linha_inicial[2:].lstrip()
        if not estado_inicial in estados:
            print(f"[!] Em {nome_arq}: estado inicial desconhecido")
            return None

        # Leitura dos estados finais da máquina
        linha_finais = arq.readline().strip()
        if not linha_finais.startswith("F:"):
            print(f"[!] Em {nome_arq}: segunda linha deve especificar"
                  " os estado finais\nFormato 'F' seguido pela lista de"
                  " estados finais, separados por espaços")
            return None
        # Múltiplos estados finais são possíveis
        estados_finais = linha_finais[2:].split()
        for estado_final in estados_finais:
            if not estado_final in estados:
                print(f"[!] Em {nome_arq}: estado final {estado_final}"
                      " desconhecido")
                return None

        num_linha = 3
        receita = Receita(estados, estado_inicial, estados_finais)
        # Leitura das transições
        while True:
            # Se a gente tivesse certeza que o programa seria executado em
            # python 3.10+, daria pra usar o operador walrus (:=) aqui e seria
            # lindo. Por compatibilidade, não vou fazer isso
            num_linha += 1
            linha = arq.readline()
            if linha == "---\n" or not linha:
                break

            trans = linha.split("->")
            if len(trans) != 2:
                print(f"[!] Transição inválida: {linha}", endl="")
                imprime_formato()
                continue

            estado_partida = trans[0].strip()
            if estado_partida not in estados:
                print(f"[!] Em {nome_arq}, linha {num_linha}: estado"
                      f" {estado_partida} desconhecido")
                continue

            saida = trans[1].split("|")
            if len(saida) != 2:
                print(f"[!] Transição inválida: {linha}", endl="")
                imprime_formato()
                continue

            estado_destino = saida[0].strip()
            if estado_destino not in estados:
                print(f"[!] Em {nome_arq}, linha {num_linha}: estado"
                      f"{estado_destino} desconhecido")
                continue

            entrada = saida[1].strip().split(',', maxsplit=1)
            if len(entrada) == 1:
                # Transição de AFD: é só um ingrediente
                ingrediente = entrada[0]
                desempilha = None
                empilha = None
            else:
                # Deveria ser uma transição de APD:
                # ingrediente, desempilha / empilha
                ingrediente = entrada[0]
                entrada = entrada[1].split('/', maxsplit=1)
                if len(entrada) == 1:
                    print(f"[!] Em {nome_arq}, linha {num_linha}: transição de"
                          " de AP sem propriedade a ser empilhada. Caso deseje"
                          " que nenhuma propriedade seja empilha, use o símbolo '_'")
                    imprime_formato()
                    continue
                desempilha = entrada[0]
                empilha = entrada[1]

            # Validação do ingrediente
            if ingrediente not in ingredientes:
                print(f"[!] Em {nome_arq}, linha {num_linha}:"
                      f" ingrediente {entrada} não reconhecido")
                continue
            receita.insere_transicao(estado_partida, estado_destino,
                                     ingrediente, desempilha, empilha)
        return receita
