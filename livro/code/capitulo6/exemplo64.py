numeros = list(range(100))  #criamos uma lista com 100 numeros

arquivo = open('numeros.txt', 'w') #criamos um arquivo 0km em modo de escrita

for numero in numeros:   #para cada numero na lista de numeros
    arquivo.write(str(numero)) #escreva cada numero em forma de string no arquivo

arquivo.close() #feche o arquivo depois


