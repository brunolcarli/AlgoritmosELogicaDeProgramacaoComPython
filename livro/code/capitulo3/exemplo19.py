
#solicitamos o nome da disciplina
disciplina = input("Insira o nome da disciplina: ")

#solicitamos as notas de cada bimestre
nota1 = float(input("Insira a nota do 1 Bimestre: "))
nota2 = float(input("Insira a nota do 2 Bimestre: "))
nota3 = float(input("Insira a nota do 3 Bimestre: "))
nota4 = float(input("Insira a nota do 4 Bimestre: "))

#calculamos a media
media = (nota1 + nota2 + nota3 + nota4) / 4

#exibimos a media e a disciplina
print("Disciplina: ", disciplina)
print("Media: ", media)

if media >= 7.0: #se a media for menor que 7.0 o aluno e reprovado
    print("Aprovado")

elif media >= 6.0 and media <= 6.9: # se a media for entre 6.0 e 6.9 recuperacao
    print("Recuperacao")

else: # senao e aprovado
    print("Reprovado")



    

