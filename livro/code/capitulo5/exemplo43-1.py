#vamos criar uma lista com 3 listas de cinco numeros de 0 a 4
matriz = [[numeros for numeros in range(5)] for numeros in range(3)]

print("A matriz:")
print(matriz) #podemos acessar a matriz toda

print("As listas:")
for listas in matriz: #ou acessar cada lista 
    print(listas)

print("Os numeros:") #ou acessar cada dado de cada lista
for lista in matriz:
    for numero in lista:
        print(numero)

#ou acessar pelo indice com ja vimos anteriormente


