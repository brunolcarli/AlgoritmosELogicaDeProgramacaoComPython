meus_dados = [] #criamos uma lista vazia

nome = input("Insira seu nome: ") #pedimos que o usuario escreva o nome
meus_dados.append(nome) #inserimos o nome na lista

idade = int(input("Insira sua idade: ")) #pedimos a idade
meus_dados.append(idade) #inserimos a idade na lista

altura = float(input("Insira sua altura: ")) #pedimos a altura
meus_dados.append(altura) #inserimos a altura na lista

print(meus_dados)  #escrevemos o conteudo da lista
