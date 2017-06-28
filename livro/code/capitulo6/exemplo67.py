arquivo = open('numeros.txt', 'a')  #abre o arquivo em modo append

letras = ['a', 'b', 'c'] #novos itens a serem adicionados

for letra in letras:
    arquivo.write('\n'+letra)

arquivo.close() #feche o modo de escrita

arquivo = open('numeros.txt', 'r') #abra o modo de leitura
for linha in arquivo: #leia o conteudo
    print(linha)

arquivo.close()

