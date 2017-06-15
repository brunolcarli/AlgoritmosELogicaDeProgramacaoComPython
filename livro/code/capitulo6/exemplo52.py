def soma(a, b):   #definimos um procedimento para soma com dois parametros
    print("O resultado e: ", a + b)  #o procedimento informa a soma dos dois parametros


def subt(a, b):   #tambem definimos um procedimento para subtracao
    print("O resultado e: ", a - b)  #que informa a subtracao entre os parametros


num1 = int(input("Insira o primeiro numero ")) #leia o primeiro numero
num2 = int(input("Insira o segundo numero "))  #leia o segundo numero

print("Qual operacao deseja realizar?")  #informe as opcoes de operacoes
print("[1] Soma \n[2]Subtracao")
escolha = int(input())        #leia a opcao desejada

if escolha == 1:      #se escolher soma
    soma(num1, num2)  #chame o procedimento de soma e passe os numeros como argumento
    
elif escolha == 2:   #se escolher subtracao
    subt(num1, num2) #chame o procedimento de subtracao e passe os numeros como argumento
    

else: #senao            
    print("Escolha invalida") #informe uma mensagem de erro




    
