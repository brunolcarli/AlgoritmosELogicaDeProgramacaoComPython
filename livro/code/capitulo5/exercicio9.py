lista = list(range(10)) #criar uma lista com 10 posicoes

for pos in lista: #para cada posicao na lista
    lista[pos] = int(input("Insira um numero: ")) #entre com um inteiro e atribua a posicao

for i in range(10): # vamos contar de um a 10, i sera o contador
    j = i+1         # j sera o contador para o numero vizinho
    for j in range(10):
        if lista[i] < lista[j]: #se o indice de posicao i for menor que o indice de posicao j
            troca = lista[i]    #fazemos uma troca, guardamos o numnero na posicao i
            lista[i] = lista[j] #colocamos o numero de posicao j no lugar da posicao i
            lista[j] = troca    #colocamos o numero da posicao i no lugar da posicao j

for numero in lista: #escreva os itens da lista ordenada
    print(numero)


