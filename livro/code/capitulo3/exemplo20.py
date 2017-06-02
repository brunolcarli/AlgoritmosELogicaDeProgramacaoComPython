#primeiro recebemos a entrada
num1 = int(input("Insira o primeiro numero "))
num2 = int(input("Insira o segundo numero "))
num3 = int(input("Insira o terceiro numero "))

if num1 > num2: #estrutura condicional externa
    
    if num1 > num3: #estrutura condicional interna (aninhada)
        print("O primeiro numero foi o maior, ", num1)
    else:
        print("O terceiro numero e o maior, ", num3)
else: 
    
    if num2 > num3:
        print("O segundo numero e o maior, ",num2)
    else:
        print("O terceiro numero e o maior, ", num3)
