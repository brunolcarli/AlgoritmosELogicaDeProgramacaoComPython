def cadastro():
    with open('produtos.txt', 'r+') as produtos: #abre o arquivo em modo de leitura e escrita (r+)
        produto = input("Insira o nome do produto: ") #receba um novo produto
        preco = input("Insira o valor de venda do produto: ") #receba o valor do novo produto
        codigo = 0 #codigo para o produto
        
        for i in produtos: #o codigo e definido autimaticamente de acordo com o numero de linhas do arquivo
            codigo += 1
            
        produtos.write(str(codigo) + " - " + produto + " - R$: " + preco + "\n") #escreva o produto no arquivo

cadastro() #chamando a subrotina para testar
        
        
