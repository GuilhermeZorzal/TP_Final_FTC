from node import Node

class ListaLigada:
    def __init__(self):
        self.primeiro_no = None
        self.ultimo_no = None
        self.tamanho = 0


    def inserir(self, elemento):
        novo_no = Node(elemento)
        if self.primeiro_no is None:
            self.primeiro_no = novo_no
            self.ultimo_no = novo_no
        else:
            self.ultimo_no.proximo = novo_no
            self.ultimo_no = novo_no
        self.tamanho += 1

    def inserir_elemento_posicao_especifica(self, elemento, posicao):
        if posicao == 0:
            novo_no = No(elemento)
            novo_no.proximo = self.__primeiro_no
            self.__primeiro_no = novo_no
        elif posicao == self.__tamanho:
            novo_no = No(elemento)
            self.__ultimo_no.proximo = novo_no
            self.__ultimo_no = novo_no
        else:
            no_anterior = self.recuperar_no(posicao - 1)
            no_atual = self.recuperar_no(posicao)
            novo_no = No(elemento)
            novo_no.proximo = no_atual
            no_anterior.proximo = novo_no
        self.__tamanho += 1

    def recuperar_no(self, posicao):
        resultado = 0
        for i in range(posicao + 1):
            if i == 0:
                resultado = self.__primeiro_no
            else:
                resultado = resultado.proximo
        return resultado

    def recuperar_elemento_no(self, posicao):
        no = self.recuperar_no(posicao)
        if no is not None:
            return no.elemento
        else:
            return None

    def contem(self, elemento):
        for i in range(self.__tamanho):
            if elemento == self.recuperar_elemento_no(i):
                return True
        return False

    def indice(self, elemento):
        for i in range(self.__tamanho):
            if elemento == self.recuperar_elemento_no(i):
                return i
        return None

    def remover_pos(self, posicao):
        if posicao == 0:
            self.__primeiro_no = self.__primeiro_no.proximo
            self.__tamanho -= 1
        elif posicao == (self.__tamanho - 1):
            self.__ultimo_no = self.recuperar_no(posicao - 1)
            self.__ultimo_no.proximo = None
            self.__tamanho -= 1
        elif posicao >= self.__tamanho:
            print('Posição invalida')
        else:
            no_anterior = self.recuperar_no(posicao - 1)
            no_posterior = self.recuperar_no(posicao + 1)
            no_anterior.proximo = no_posterior
            self.__tamanho -= 1

    def remover_elemento(self, elemento):
        if self.indice(elemento) != None:
            self.remover_pos(self.indice(elemento))
        else:
            print('Elemento não existe na lista')

