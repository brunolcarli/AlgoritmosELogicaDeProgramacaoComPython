def buscaProduto():
    with open('produtos.txt', 'r') as produtos:
        achou = False #o produto precisa ser encontrado
        
        produto = input("Insira o nome do produto: ") #solicita um produto

        for linha in produtos:   #busca em cada linha do arquivo
            if produto in linha: #se o produto estiver em uma destas linhas
                print(linha)     #escreva esta linha
                achou = True     #achamos o produto

        if not achou:  #se nao achou o produto
            print("Produto nao cadastrado") #informe que o produto nao existe

buscaProduto()

