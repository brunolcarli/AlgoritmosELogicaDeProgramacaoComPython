nome = input("Insira seu nome: ") #ler nome
idade = int(input("Insira sua idade: ")) #ler idade

if idade < 18: #verifica se a idade e menor que 18
    print(nome, " voce e menor de idade")
    
elif idade >= 18 and idade < 65: #senao verifica se a idade est entre 18 e 65
    print(nome, " voce e maior de idade")
    
else: #senao for nenhuma das acima, entao e idoso
    print(nome, " voce ja e idoso")


