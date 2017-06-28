def verProdutos():
    with open('produtos.txt', 'r') as produtos:
        for linha in produtos:
            print(linha)

verProdutos()
