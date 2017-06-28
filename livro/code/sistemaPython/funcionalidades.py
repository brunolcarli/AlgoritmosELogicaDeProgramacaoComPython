#sub-rotina para cadastrar um produto
def cadastro():    
    with open('produtos.txt', 'r+') as produtos: 
        produto = input("Insira o nome do produto: ") 
        preco = input("Insira o valor de venda do produto: ") 
        codigo = 0 
        for i in produtos: 
            codigo += 1           
        produtos.write(str(codigo) + " - " + produto + " - R$: " + preco + "\n")
        
#sub-rotina para ver a lista de produtos
def verProdutos():     
    with open('produtos.txt', 'r') as produtos:
        for linha in produtos:
            print(linha)
            
#sub-rotina de busca
def buscaProduto():    
    with open('produtos.txt', 'r') as produtos:
        achou = False
        produto = input("Insira o nome do produto: ") 
        for linha in produtos:   
            if produto in linha: 
                print(linha)     
                achou = True     
        if not achou:
            print("Produto nao cadastrado") 

#sub-rotina para compra                
def compra():
    total = 0
    lista = [] 
    compras = []  
    while True:
        item = input("Insira o codigo ou nome do produto: ")
        if item == 'fim':
            break
        else:
            with open('produtos.txt', 'r') as produtos: 
                for linha in produtos:
                    if item in linha:
                        compras.append(linha)
                        lista.append(float(linha[-5:-1])) 
    total = sum(lista) 
    print("Lista de compras: ")
    for produto in compras:  
        print(produto)
    print("TOTAL A PAGAR: R$ %.2f" % total)

