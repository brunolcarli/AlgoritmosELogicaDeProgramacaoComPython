arquivo = open('numeros.txt', 'r') #abrimos nosso arquivo em modo de leitura

for linha in arquivo: #para cada linha no arquivo
    print(linha) #escreva o conteudo da linha

arquivo.close() #feche o arquivo

