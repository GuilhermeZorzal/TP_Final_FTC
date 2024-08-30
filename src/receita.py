# Regras de transição para um único estado
class Regras:
    def __init__(self, nome):
        self.regras = dict()
        self.nome_estado = nome

    def insere(self, estado_destino, ingrediente, desempilha=None, empilha=None):
        """
        Insere um transição qualquer, decidindo se ela é de AFD ou de APD
        baseando-se na presença ou ausência dos argumentos empilha e desempilha
        """
        if not desempilha and not empilha:
            self.insere_afd(estado_destino, ingrediente)
            return
        self.insere_apd(estado_destino, ingrediente, desempilha, empilha)

    def insere_afd(self, estado_destino, ingrediente):
        """
        Insere uma transição de AFD, em que a leitura de um ingrediente
        leva do estado atual para um estado de destino.
        """
        if ingrediente in self.regras or ingrediente == "_":
            print(f"[!] A transição \"{ingrediente}\" no estado {self.nome_estado} "
                  f"é compatível, por favor verificar determinismo")    
            exit()
        self.regras[ingrediente] = estado_destino

    def insere_apd(self, estado_destino, ingrediente, desempilha, empilha):
        """
        Insere uma transição de APD, em que a leitura de um ingrediente e o
        símbolo no topo da pilha ("desempilha") levam do estado atual para um
        estado de destino, empilhando um símbolo ("empilha")
        """
        # verificando se a transição é compatível
        if "_" in self.regras:
            if desempilha == "_":
                print(f"[!] A transição \"{ingrediente}, {desempilha} / {empilha}\" "
                    f"é compatível com a transição \"_,"
                    f" {(list(self.regras['_'].keys())[0])} \""
                    f" no estado {self.nome_estado}\nPor favor verificar determinismo")    
                exit()
        if ingrediente in self.regras:
            if desempilha in self.regras[ingrediente] or desempilha == "_" or "_" in self.regras[ingrediente]:
                print(f"[!] A transição \"{ingrediente}, {desempilha} / {empilha}\" "
                    f"é compatível com a transição \"{ingrediente},"
                    f" {list(self.regras[ingrediente].keys())[0]} \""
                    f" no estado {self.nome_estado}\nPor favor verificar determinismo")    
                exit()
        elif ingrediente == "_":
            for ing in self.regras:
                for des in self.regras[ing]:
                    if "_" == des:
                        print(f"[!] A transição \"{ingrediente}, {desempilha} / {empilha}\" "
                        f"é compatível com a transição \"{ing}, {des} \","
                        f" no estado {self.nome_estado}\nPor favor verificar determinismo")    
                    exit()
        if ingrediente not in self.regras:
            self.regras[ingrediente] = dict()
        elif not isinstance(self.regras[ingrediente], dict):
            # Caso particular meio complicado aqui. Pode ser que uma transição
            # para esse ingrediente tenha sido inserida como AFD. Precisamos
            # converter a posição na lista desse ingrediente em um dicionário
            # antes de mais nada
            estado_destino = self.regras[ingrediente]
            self.regras[ingrediente] = dict()
            self.regras[ingrediente]["_"] = (estado_destino, "_")    
        self.regras[ingrediente][desempilha] = (estado_destino, empilha)
# A receita nada mais é do que a especificação de um autômato
class Receita:
    def __init__(self, estados, inicial, finais):
        self.estados = dict()
        for estado in estados:
            self.estados[estado] = Regras(estado)
        self.inicial = inicial
        self.finais = finais

    def insere_transicao(self, estado_partida, estado_destino, ing,
                         desempilha=None, empilha=None):
        self.estados[estado_partida].insere(estado_destino, ing,
                                            desempilha, empilha)

    def imprime(self):
        for estado in self.estados:
            print(estado)
            for ing, saida in self.estados[estado].regras.items():
                if not isinstance(saida, dict):
                    # Transição de AF: simples e direta
                    print(f"\t{ing} -> {saida}")
                    continue
                # Múltiplas transições de AP
                for desempilha, (estado_destino, empilha) in saida.items():
                    print(f"\t{ing}, {desempilha} -> {estado_destino} / {empilha}")
            print()
