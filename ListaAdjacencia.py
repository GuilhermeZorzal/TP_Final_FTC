class Transicoes:
	def __init__(self) -> None:
     	# os estados guardam apenas as transições que faz, visto que o nome dos ingredientes estão no autõmato
		self.transicoes = dict()
  
	def insere_transicao(self, ingrediente, transicao) -> None :
		self.transicoes.update({transicao: ingrediente})

class Automato:
    def __init__(self) -> None:
        #dicionário contendo nome dos ingredientes (estados): transições
        self.dict_estados = dict()
        self.inicial = None
        self.final = None
                
    def insere_estado(self, ingrediente) ->None:
        transicoes = Transicoes()
        self.dict_estados.update({ingrediente: transicoes})
        
    def atualiza_transicoes(self, ingrediente_partida, transicao, ingrediente_chegada)->None:
        self.dict_estados[ingrediente_partida].insere_transicao(transicao, ingrediente_chegada)
        
    def insere_inicial_final(self, inicial, final):
        self.final = final
        self.inicial = inicial
    
    def imprime_automato(self):
        for i in self.dict_estados.keys():
            print(i)
            for value, key in self.dict_estados[i].transicoes.items():
                print("\t", key, "->", value)
        
afd = Automato()

afd.insere_estado("I")
afd.insere_estado("ing1")
afd.insere_estado("ing2")
afd.insere_estado("ing3")
afd.insere_estado("erro")
afd.insere_estado("F")
afd.atualiza_transicoes("I", "a", "ing1")
afd.atualiza_transicoes("ing1", "p", "ing2")
afd.atualiza_transicoes("ing1", "o", "erro")
afd.atualiza_transicoes("ing2", "p", "F")
afd.atualiza_transicoes("ing2", "o", "erro")
afd.atualiza_transicoes("F", "o", "erro")
afd.imprime_automato()