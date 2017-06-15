def quadrado(numero): #a definicao de uma funcao e igual a de um procedimento
    return numero**2  #usamos a instrucao return para retornar um valor

entrada = int(input("Insira um numero: ")) #pedimos um numero

quad = quadrado(entrada) #chamamos a funcao e guardamos o retorno em quad

print("O quadrado de %i e %i" % (entrada, quad)) #escrevemos o resultado

print("O quadrado do quadrado e ", quadrado(quad)) #o retorno tambem pode ser impresso

