def append(fila, objeto):
    if fila.primeiro == None:
        fila.primeiro = objeto
        fila.ultimo = objeto
    else:
        fila.ultimo.anterior = objeto
        fila.ultimo = objeto

class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

class Carro:
    def __init__(self, comprimento):
        self.anterior = None
        self.comprimento = comprimento

def main():
    casos = int(input())
    cont_casos = 0
    while cont_casos < casos:
        numero_viagens = 0
        fila_esquerda = Fila()
        fila_direita = Fila()
        cont_casos += 1
        entrada = input().split(' ')
        comprimento_balsa = espaco_disponivel = int(entrada[0]) * 100
        n_carros = int(entrada[1])
        while 0 < n_carros :
            n_carros -= 1
            tamanho_carro, lado_carro = input().split(' ')
            if lado_carro == 'esquerdo':
                append(fila_esquerda, Carro(int(tamanho_carro)))
            elif lado_carro == 'direito':
                append(fila_direita, Carro(int(tamanho_carro)))
        lado_esquerdo = True
        while fila_esquerda.primeiro != None or fila_direita.primeiro != None:
            if lado_esquerdo:
                if fila_esquerda.primeiro != None: 
                    if fila_esquerda.primeiro.comprimento <= espaco_disponivel:
                        espaco_disponivel -= fila_esquerda.primeiro.comprimento
                        fila_esquerda.primeiro = fila_esquerda.primeiro.anterior
                        if fila_esquerda.primeiro == None:
                            numero_viagens += 1
                            lado_esquerdo = False
                            espaco_disponivel = comprimento_balsa
                    else:
                        numero_viagens += 1
                        lado_esquerdo = False
                        espaco_disponivel = comprimento_balsa
                elif fila_direita.primeiro != None or espaco_disponivel < comprimento_balsa:
                    numero_viagens += 1
                    lado_esquerdo = False
                    espaco_disponivel = comprimento_balsa
            else:
                if fila_direita.primeiro != None:
                    if fila_direita.primeiro.comprimento <= espaco_disponivel:
                        espaco_disponivel -= fila_direita.primeiro.comprimento
                        fila_direita.primeiro = fila_direita.primeiro.anterior
                        if fila_direita.primeiro == None:
                            numero_viagens += 1
                            lado_esquerdo = True
                            espaco_disponivel = comprimento_balsa
                    else:
                        numero_viagens += 1
                        lado_esquerdo = True
                        espaco_disponivel = comprimento_balsa
                elif fila_esquerda.primeiro != None or espaco_disponivel < comprimento_balsa:
                    numero_viagens += 1
                    lado_esquerdo = True
                    espaco_disponivel = comprimento_balsa
            
        print("Caso " + str(cont_casos) + ": " + str(numero_viagens))
        

if __name__ == '__main__':
    main()