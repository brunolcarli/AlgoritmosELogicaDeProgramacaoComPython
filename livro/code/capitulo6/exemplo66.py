arquivo = open('numeros.txt', 'w') 

numeros = [999, 998, 997] #nivis numeros a serem adicionados

for numero in numeros:
    arquivo.write(str(numero))

arquivo.close() #feche o modo de escrita

arquivo = open('numeros.txt', 'r') #abra o modo de leitura
for linha in arquivo: #leia o conteudo
    print(linha)

arquivo.close()
