import funcionalidades     #importa o modulo de funcionalidades que criamos

while True:                #criamos um loop para o programa
    
    print('#'*34)          #fornecemos um menu de opcoes
    print(">"*11,"BEM-VINDO","<"*11)
    print("Escolha a operacao desejada")
    print("[1] Cadastrar produto")
    print("[2] Verificar produtos cadastrados")
    print("[3] Buscar produto")
    print("[4] Compra")
    print("[5] Sair do sistema")
    print("#"*34)

    entrada = input()     #recebe a entrada
    
    if entrada == '1':    #fornece a funcionalidade de acordo com a opcao
        funcionalidades.cadastro()
    elif entrada == '2':
        funcionalidades.verProdutos()
    elif entrada == '3':
        funcionalidades.buscaProdutos()
    elif entrada == '4':
        funcionalidades.compra()
    elif entrada == '5':
        break
    else:                #e uma mensagem avisando quando a entrada for invalida
        print("#"*34)
        print("Operacao invalida")
        print("#"*34)

