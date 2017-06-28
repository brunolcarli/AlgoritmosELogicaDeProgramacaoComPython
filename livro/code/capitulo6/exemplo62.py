def fatorial(numero):  #define a funcao
    if numero == 0:  #aqui temos a condicao de parada
        return 1
    else:
        return numero * fatorial(numero - 1) #e aqui a chamada recursiva


x = fatorial(5) #chamamos a funcao com argumento 5
print(x) #escrevemos o resultado

