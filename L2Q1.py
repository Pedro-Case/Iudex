class Node:
    def __init__(self, valor):
        self.valor = valor
        self.pai = None
        self.esq = None
        self.dir = None


class Arvore:
    raiz = None
    def balancear(no):
        no_acessado = no
        while no_acessado is not None:
            altura_esq = Arvore.calcula_altura(no_acessado.esq)
            altura_dir = Arvore.calcula_altura(no_acessado.dir)
            fb = altura_esq - altura_dir
            if fb < -1:
                no_acessado.dir.esq = no_acessado
                if no_acessado.pai.esq == no_acessado:
                    no_acessado.pai.esq = no_acessado.dir
                else:
                    no_acessado.pai.dir = no_acessado.dir
                no_acessado.dir = None
            elif fb > 1:
                no_acessado.esq.dir = no_acessado
                if no_acessado.pai.esq == no_acessado:
                    no_acessado.pai.esq = no_acessado.esq
                else:
                    no_acessado.pai.dir = no_acessado.esq
                no_acessado.esq = None
            no_acessado = no_acessado.pai


    def calcula_altura(no):
        if no is None:
            return -1
        no_esq_altura = Arvore.calcula_altura(no.esq)
        no_dir_altura = Arvore.calcula_altura(no.dir)
        if no_esq_altura > no_dir_altura:
            return no_esq_altura + 1
        else:
            return no_dir_altura + 1

    def busca_no(chave):
        if Arvore.raiz == None:
            return -1
        elif Arvore.raiz.valor == chave:
            return 0
        else:
            no_acessado = Arvore.raiz
            buscando = True
            nivel = 0
            while buscando:
                nivel += 1
                if chave < no_acessado.valor:
                    if no_acessado.esq:
                        no_acessado = no_acessado.esq
                    else:     
                        buscando = False
                        return nivel
                elif chave > no_acessado.valor:
                    if no_acessado.dir:
                        no_acessado = no_acessado.dir
                    else:
                        buscando = False
                        return nivel
    def adicionar(no_adicionado):
        if Arvore.raiz == None:
            Arvore.raiz = no_adicionado
        else:
            no_acessado = Arvore.raiz
            adicionando = True
            while adicionando:
                if no_adicionado.valor < no_acessado.valor:
                    if no_acessado.esq:
                        no_acessado = no_acessado.esq
                    else:
                        no_adicionado.pai = no_acessado
                        no_acessado.esq = no_adicionado
                        adicionando = False
                elif no_adicionado.valor > no_acessado.valor:
                    if no_acessado.dir:
                        no_acessado = no_acessado.dir
                    else:
                        no_adicionado.pai = no_acessado
                        no_acessado.dir = no_adicionado
                        adicionando = False
    

rodando = True
while rodando:
    entrada = input()
    if entrada == 'FIM':
        rodando = False
    else:
        funcao, argumento = entrada.split(' ')
        if funcao == 'ADICIONA':
            no_adicionado = Node(int(argumento))
            Arvore.adicionar(no_adicionado)
            Arvore.balancear(no_adicionado)

        elif funcao == 'NIVEL':
            nivel = Arvore.busca_no(int(argumento))
            if nivel != -1:
                print('Nivel de ' + argumento + ': ' + str(nivel))
            else:
                print('Valor de ' + argumento + ' inexistente')

