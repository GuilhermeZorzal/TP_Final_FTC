#Essa classe deixa mais claro que estamos trabalhando com transições
class Transicoes:
	def __init__(self) -> None:
     	# os estados guardam apenas as transições que faz, visto que o nome dos ingredientes estão no autõmato
		self.transicoes = dict()
  
	def insere_transicao(self, ingrediente, transicao) -> None :
		self.transicoes.update({transicao: ingrediente})

#o autômato nada mais é do que um dicionário de dicionários
class Automato:
    def __init__(self) -> None:
        # dicionário contendo nome dos ingredientes (estados): transições
        # só reforçando aqui, o nome dos ingredientes são as keys() do dicionário
        self.dict_estados = dict()
        self.inicial = None
        self.final = list()
    
    # usado na leitura da linha Q para inserir os estados que o automato terá
    def insere_estado(self, ingrediente) ->None:
        #aqui é iniciado o dicionário das transições que esse autômato terá
        transicoes = Transicoes()
        self.dict_estados.update({ingrediente: transicoes})
    
    # com todos os estados já inseridos, vamos adicionar as transições
    def atualiza_transicoes(self, ingrediente_partida, transicao, ingrediente_chegada)->None:
        self.dict_estados[ingrediente_partida].insere_transicao(transicao, ingrediente_chegada)
    
    def insere_inicial(self, inicial):
        self.inicial = inicial
    
    def insere_final(self, final):
        self.final.append(final)
    
    def imprime_automato(self):
        for i in self.dict_estados.keys():
            print(i)
            for value, key in self.dict_estados[i].transicoes.items():
                print("\t", key, "->", value)

    def constroi_automato(self, texto):
        for linha in texto:
            linha = linha.rstrip()
            if linha[0:2] == "Q:":
                linha = linha.replace("Q: ", "")
                for ingrediente in linha.split():
                    self.insere_estado(ingrediente)
            elif linha[0:2] == "I:":
                linha = linha.replace("I: ", "")
                self.insere_inicial(linha)
            elif linha[0:2] == "F:":
                linha = linha.replace("F: ", "")
                self.insere_final(linha)
            else:
                linha = linha.split()
                ingrediente_partida = linha[0]
                transicao = linha[4]
                ingrediente_chegada = linha[2]
                self.atualiza_transicoes(ingrediente_partida, transicao, ingrediente_chegada)
        