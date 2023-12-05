class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None
        self.FB = 0

class Arvore:
    def __init__(self):
        self.raiz = None
    def adicionar(self, no_adicionado):
        if self.raiz == None:
            self.raiz = no_adicionado
        else:
            no_acessado = self.raiz
            adicionando = True
            while adicionando:
                if no_adicionado.valor < no_acessado.valor:
                    if no_acessado.esq:
                        no_acessado = no_acessado.esq
                    else:     
                        no_acessado.esq = no_adicionado
                        adicionando = False
                elif no_adicionado.valor > no_acessado.valor:
                    if no_acessado.dir:
                        no_acessado = no_acessado.dir
                    else:
                        no_acessado.dir = no_adicionado
                        adicionando = False
    

rodando = True
arvore = Arvore()
while rodando:
    entrada = input()
    if entrada == 'FIM':
        rodando = False
    else:
        funcao, argumento = entrada.split(' ')
        if funcao == 'ADICIONA':
            no_adicionado = Node(int(argumento))
            arvore.adicionar(no_adicionado)

