class Pilha:
    def __init__(self):
        self.topo = -1
        self.base = None
        self.tamanho = 0

class Caixa:
    def __init__(self, valor, paridade):
        self.proximo = None
        self.anterior = None
        self.valor = valor
        self.paridade = paridade # 1 é impar 0 é par
def main():
    n_de_pilhas = int(input())
    for _ in range(1, n_de_pilhas + 1):
        pilha_caixas = Pilha()
        entrada = int(input())
        while entrada != 0:
            paridade = entrada % 2 
            if pilha_caixas.base == None:
                caixa = Caixa(entrada, paridade)
                pilha_caixas.base = caixa
                pilha_caixas.topo = caixa
                pilha_caixas.tamanho += 1
            else:
                # Caixa é adicionada normalmente
                caixa = Caixa(entrada, paridade)
                pilha_caixas.topo.proximo = caixa
                caixa.anterior = pilha_caixas.topo
                pilha_caixas.topo = caixa
                pilha_caixas.tamanho += 1
            entrada = int(input())
    termo_acessado = pilha_caixas.topo
    while termo_acessado.anterior != None:
        if termo_acessado.paridade == termo_acessado.anterior.paridade == 0:
        termo_acessado = termo_acessado.anterior


if __name__ == '__main__':
    main()
