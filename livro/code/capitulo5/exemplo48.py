aluno = {          #abrimos um dicionario com identificador de aluno
    'nome' : '',   #definimos uma chave nome com valor em branco
    'nota1' : 0,   #definimos uma chave nota1 com valor zero
    'nota2' : 0,   #definimos uma chave nota2 com valor zero
    'nota3' : 0,   #definimos uma chave nota3 com valor zero
    'nota4' : 0,   #definimos uma chave nota4 com valor zero
    'media' : 0    #definimos uma chave media com valor zero
    }

aluno['nome'] = input("Insira o nome do aluno: ") #solicita o nome do aluno
aluno['nota1'] = float(input("Insira a primeira nota: ")) #solicita as notas
aluno['nota2'] = float(input("Insira a segunda nota: "))
aluno['nota3'] = float(input("Insira a terceira nota: "))
aluno['nota4'] = float(input("Insira a quarta nota: "))

#calcula a media
aluno['media'] = (aluno['nota1'] + aluno['nota2'] + aluno['nota3'] + aluno['nota4']) / 4

#informe os dados
print("Aluno: ", aluno['nome'])
print("Media: %.1f" % aluno['media'])

