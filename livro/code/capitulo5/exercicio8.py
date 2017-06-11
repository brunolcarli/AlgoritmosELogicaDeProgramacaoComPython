vetor = [] #criamos um vetor vazio

for i in range(30): #vamos contar ate 30
    #a cada contagem pedimos um numero e o colocamos no final da lista
    vetor.append(int(input("Insira um numero inteiro: ")))

vetor.reverse() #invertemos o vetor

for elemento in vetor: #para cada elemento no vetor
    print(elemento) #informe na tela o elemento

