class Regras:
    def __init__(self, nome, saida):
        """
        Inicializa as regras de transição para um estado de uma máquina de Moore.
        :param nome: Nome do estado
        :param saida: Saída associada ao estado
        """
        self.regras = dict()
        self.nome_estado = nome
        self.saida = saida  # Saída associada ao estado

    def insere(self, estado_destino, ingrediente):
        """
        Insere uma transição para um estado de destino dado um ingrediente.
        :param estado_destino: Estado para onde a transição leva
        :param ingrediente: Símbolo de entrada que causa a transição
        """
        if ingrediente in self.regras:
            print(f"[!] Transição para o ingrediente \"{ingrediente}\" já existe no estado {self.nome_estado}.")
            exit()
        self.regras[ingrediente] = estado_destino

class Receita:
    def __init__(self, estados, inicial, finais, saidas):
        """
        Inicializa a máquina de Moore.
        :param estados: Lista de estados da máquina
        :param inicial: Estado inicial
        :param finais: Lista de estados finais
        :param saidas: Saídas associadas a cada estado
        """
        self.estados = dict()
        if len(estados) != len(saidas):
            print("[!] O número de estados deve corresponder ao número de saídas.")
            exit()

        for estado, saida in zip(estados, saidas):
            self.estados[estado] = Regras(estado, saida)
        self.inicial = inicial
        self.finais = finais

    def insere_transicao(self, estado_partida, estado_destino, ingrediente):
        """
        Insere uma transição de um estado para outro dado um ingrediente.
        :param estado_partida: Estado onde a transição começa
        :param estado_destino: Estado para onde a transição leva
        :param ingrediente: Símbolo de entrada que causa a transição
        """
        if estado_partida not in self.estados or estado_destino not in self.estados:
            print(f"[!] Um dos estados {estado_partida} ou {estado_destino} não existe.")
            exit()
        self.estados[estado_partida].insere(estado_destino, ingrediente)

    def define_saida(self, estado, saida):
        """
        Define ou altera a saída associada a um estado.
        :param estado: Estado para o qual a saída deve ser definida
        :param saida: Saída a ser associada ao estado
        """
        if estado in self.estados:
            self.estados[estado].saida = saida
        else:
            print(f"[!] Estado {estado} não encontrado.")

    def imprime(self):
        """
        Imprime a descrição completa da máquina de Moore, incluindo transições e saídas.
        """
        for estado in self.estados:
            print(f"Estado: {estado}, Saída: {self.estados[estado].saida}")
            for ingrediente, estado_destino in self.estados[estado].regras.items():
                print(f"\t{ingrediente} -> {estado_destino}")
            print()

import re

def processa_entrada(arquivo):
    with open(arquivo, 'r') as file:
        linhas = file.readlines()

    # Processando a lista de estados e saídas
    estados_line = linhas[0].strip().split()
    estados = estados_line[1:]
    
    saídas_line = linhas[1].strip().split()
    saidas = saídas_line[1:]

    # Processando o estado inicial e os finais
    estado_inicial = linhas[2].strip().split()[1]
    estados_finais = linhas[3].strip().split()[1:]

    # Processando as transições
    transicoes = linhas[4:]

    receita = Receita(estados, estado_inicial, estados_finais, saidas)

    for transicao in transicoes:
        match = re.match(r'(\w+) -> (\w+) \| (.)', transicao.strip())
        if match:
            estado_partida, estado_destino, ingrediente = match.groups()
            receita.insere_transicao(estado_partida, estado_destino, ingrediente)
        else:
            print(f"[!] Transição mal formatada: {transicao.strip()}")

    return receita

# Exemplo de uso
arquivo_entrada = '../pocoes/receitand2.txt.txt'  # Substitua pelo caminho do seu arquivo
automato = processa_entrada(arquivo_entrada)
automato.imprime()