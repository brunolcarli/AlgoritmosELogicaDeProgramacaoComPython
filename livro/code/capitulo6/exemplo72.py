def compra():
    total = 0  #variavel com valor a pgar
    lista = [] #lista de preco dos produtos
    compras = [] #lista de compras
    
    while True: #loop para receber varios produtos
        
        item = input("Insira o codigo ou nome do produto: ") #le o produto ou codigo do produto

        if item == 'fim': #o loop funciona ate que seja inserido fim
            break
        else:
            with open('produtos.txt', 'r') as produtos: #busca o produto comprado no arquivo
                for linha in produtos:
                    if item in linha:
                        compras.append(linha) #adiciona o produto a lista de compras
                        lista.append(float(linha[-5:-1])) #adiciona somente o valor do produto a lista de precos

    total = sum(lista) #somamos o total a pagar
    print("Lista de compras: ")
    for produto in compras:  #escrevemos os produtos comprados na tela
        print(produto)

    print("TOTAL A PAGAR: R$ %.2f" % total) #escrevemos o total a pagar na tela

compra()



