# Funções relacionadas à leitura de autômatos

from receita import Receita

# Imprime formato de uma regra de transição
def imprime_formato():
    print("Formato: {estado} -> {estado_destino} | {ingrediente}"
          " [, {topo-pilha} / {empilha}]")

# Lê uma receita de um arquivo dado um alfabeto que deve ser reconhecido
def carrega_receita(nome_arq, sigma):
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
            processa_regra(nome_arq, sigma, receita, linha, num_linha)
        return receita

# Processa uma regra
def processa_regra(nome_arq, sigma, receita, linha, num_linha):
    ok = True
    # Divisão da transição entre estado de partida e restante
    trans = linha.split("->")
    if len(trans) != 2:
        print(f"[!] Transição inválida: {linha}", endl="")
        imprime_formato()
        return

    # Validação do estado de partida
    estado_partida = trans[0].strip()
    if estado_partida not in receita.estados:
        print(f"[!] Em {nome_arq}, linha {num_linha}: estado"
              f" {estado_partida} desconhecido")
        return

    # Divisão do restante em estado de destino e restante
    saida = trans[1].split("|")
    if len(saida) != 2:
        print(f"[!] Transição inválida: {linha}", endl="")
        imprime_formato()
        return

    # Validação do estado de destino
    estado_destino = saida[0].strip()
    if estado_destino not in receita.estados:
        print(f"[!] Em {nome_arq}, linha {num_linha}: estado"
              f"{estado_destino} desconhecido")
        ok = False

    # O restante é simplesmente um ingrediente (AFD) ou uma descrição mais
    # complexa que inclui entrada e saída (APD)
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
            return

        # Valida reação a ser desempilhada
        desempilha = entrada[0].strip()
        if not sigma.valida_reacao(desempilha):
            print(f"[!] Em {nome_arq}, linha {num_linha}:"
                  f" reação {desempilha} não reconhecida")
            exit()

        # Valida reação a ser empilhada
        empilha = entrada[1].strip()
        if not sigma.valida_reacao(empilha):
            print(f"[!] Em {nome_arq}, linha {num_linha}:"
                  f" reação {empilha} não reconhecida")
            exit()
    # Validação do ingrediente
    if not sigma.valida_ingrediente(ingrediente):
        print(f"[!] Em {nome_arq}, linha {num_linha}:"
              f" ingrediente {entrada} não reconhecido")
        return
    if not ok: return
    receita.insere_transicao(estado_partida, estado_destino,
                                     ingrediente, desempilha, empilha)
    return receita
