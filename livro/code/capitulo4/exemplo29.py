loop = 's'  #inicializamos a condicao do loop while


while loop != 'n': #enquanto loop for diferente de 'n'

    soma = 0    #inicializamos a soma

    #somar quantos numeros o usuario quiser
    maximo = int(input("Quantos numeros voce deseja somar? ")) 

    for i in range(maximo): #loop para somar a quantidade desejada
        entrada = int(input("Insira um numero para somar: "))
        soma += entrada

    #aqui ja estamos fora do loop for, mas dentro do loop while ainda
    print("O resultado da soma e: ", soma)

    #verificamos se o usuario quer continuar no programa
    loop = input("Gostaria de realizar outra soma? s/n ")
    

    
