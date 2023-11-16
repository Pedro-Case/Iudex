class Pilha:
    def __init__(self):
        self.topo = -1
        self.base = None
        self.tamanho = 0

class Caixa:
    def __init__(self, valor):
        self.proximo = None
        self.anterior = None
        self.valor = valor
def main():
    n_de_pilhas = int(input())
    for _ in range(1, n_de_pilhas + 1):
        pilha_caixas = Pilha()
        entrada = input()
        while entrada != 0:
            entrada = int(input()) 
            if pilha_caixas.base == None:
                caixa = Caixa(entrada)
                pilha_caixas.base = caixa
                pilha_caixas.topo = caixa
                pilha_caixas.tamanho += 1
            else:
                caixa = Caixa(entrada)
                if caixa.valor % 2 == pilha_caixas.topo.valor % 2:
                    if caixa.valor > pilha_caixas.topo.valor:
                            diferenca = caixa.valor - pilha_caixas.topo.valor
                    else:
                        diferenca = pilha_caixas.topo.valor - caixa.valor
                    pilha_caixas.topo.valor = diferenca
                else:
                    pilha_caixas.topo.proximo = caixa
                    caixa.anterior = pilha_caixas.topo
                    pilha_caixas.topo = caixa
                    pilha_caixas.tamanho += 1
    termo_acessado = pilha_caixas.topo
    while termo_acessado.anterior != None:
        if termo_acessado.paridade == termo_acessado.anterior.paridade == 0:


if __name__ == '__main__':
    main()
