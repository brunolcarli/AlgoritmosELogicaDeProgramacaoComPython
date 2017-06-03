inseridos = 0  #variavel para contar quantos numeros sera inseridos
num = 1        #variavel para controlar o loop

while num != 0: #o loop vai repetir ate que o usuario digite zero
    
    num = int(input("Insira um numero ou aperte 0 para sair: ")) #pedimos um num
    
    if num != 0: #caso a entrada seja diferente de zero aumentamos o contador
        inseridos += 1

print("Voce inseriu ", inseridos, " numeros") #escrevemos na tela
