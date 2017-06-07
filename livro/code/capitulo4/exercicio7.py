casadas = 0      #primeiro inicializamos as variaveis 
solteiras = 0
viuvas = 0
divorciadas = 0


idade = int(input("Insira sua idade ou 0 para sair: "))

#o programa so funciona se  a idade for maior que zero

while idade != 0: #loop externo
    print("Informe o estado civil") #informe o usuario para que insira o estado civil
    
    estado = "" #inicilizamos a variavel do loop interno
    while estado != 'C' and estado != 'S' and estado != 'D' and estado !='V':

        #veja na string abaixo o uso de \n isso diz ao Python para pular uma linha
        estado = input("C: Casado \nS: Solteiro \nD: Divorciado \nV: Viuvo \n")

        # .upper() transforma os caracteres da string em CAIXA ALTA
        estado = estado.upper() 
    #Aqui acaba o loop interno
        
    if estado == 'C':    #Ainda dentro do loop interno fazemos a verificacao
        casadas += 1     
    elif estado == 'S':
        solteiras += 1
    elif estado == 'D':
        divorciadas += 1
    elif estado == 'V':
        viuvas += 1
    else:
        print("Algo errado")

    idade = int(input("Insira sua idade ou 0 para sair: ")) #pedimos a idade mais uma vez
    
#fim do loop externo
print("O numero de solteiros e: ", solteiras)  #informamos os resultados
print("O numero de casados e: ", casadas)
print("O numero de divorciados e: ", divorciadas)
print("O numero de viuvos e: ", viuvas)


