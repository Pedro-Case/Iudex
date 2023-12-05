class Pilha:
    def __init__(self):
        self.topo = None
        self.base = None
        self.tamanho = 0

class Caixa:
    def __init__(self, valor):
        self.proximo = None
        self.anterior = None
        self.valor = valor


def resolve(pilha_caixas):
    while pilha_caixas.topo != pilha_caixas.base and pilha_caixas.topo.anterior.valor % 2 == pilha_caixas.topo.valor % 2:
            diferenca = pilha_caixas.topo.anterior.valor - pilha_caixas.topo.valor
            if diferenca < 0:
                diferenca *= -1
            pilha_caixas.topo = pilha_caixas.topo.anterior
            pilha_caixas.topo.valor = diferenca
            pilha_caixas.topo.proximo = None
            pilha_caixas.tamanho -= 1

def main():
    cont_pilha = 0
    n_de_pilhas = int(input())
    while cont_pilha < n_de_pilhas:
        pilha_caixas = Pilha()
        entrada = input()
        while entrada != 0:
            entrada = int(input()) 
            if entrada != 0:
                if pilha_caixas.base == None:
                    caixa = Caixa(entrada)
                    pilha_caixas.base = caixa
                    pilha_caixas.topo = caixa
                    pilha_caixas.tamanho += 1
                else:
                    caixa = Caixa(entrada)
                    pilha_caixas.topo.proximo = caixa
                    caixa.anterior = pilha_caixas.topo
                    pilha_caixas.topo = caixa
                    pilha_caixas.tamanho += 1
                    resolve(pilha_caixas)
        cont_pilha += 1
        print("Pilha " + str(cont_pilha) + ": " + str(pilha_caixas.tamanho) + " " + str(pilha_caixas.topo.valor))


if __name__ == '__main__':
    main()
