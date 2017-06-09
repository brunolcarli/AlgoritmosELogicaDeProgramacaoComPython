#entrar com a disciplina
disciplina = input("Insira sua disciplina: ")
#Entrar com a quantidade de alunos da turma
quantidade = int(input("Insira o numero de alunos da turma: "))

#a turma e uma lista com tamanho igual a quantidade informada
turma = [alunos for alunos in range(quantidade)]

#para cada aluno na turma
for aluno in turma:

    #informe os dados do aluno e guarde em um dicionario
    turma[aluno] = {'nome':input("Insira o nome do aluno: "), 
                    'notas':[float(input("Insira a nota: ")) for notas in range(4)],
                    'media':0, 
                    'sit': '',
                    }
    
    #calcule a media referenciaando-a pelo indice
    turma[aluno]['media'] = ( 
        turma[aluno]['notas'][0] + turma[aluno]['notas'][1] +
        turma[aluno]['notas'][2] + turma[aluno]['notas'][3]) / 4
        #as notas estao dentro de uma lista no dicionario que esta dentro da lista da turma

    #agora vamos verificar se o aluno esta aprovado
    if turma[aluno]['media'] < 6.0: 
        turma[aluno]['sit'] = 'Reprovado'
        
    elif turma[aluno]['media'] > 6.0 and turma[aluno]['media'] < 7.0:
        turma[aluno]['sit'] = 'Recuperacao'
        
    else:
        turma[aluno]['sit'] = 'Aprovado'
        
#depois que seu loop receber todos os alunos vamos informar os resultados na tela
print("Disciplina: %s" % disciplina) #escreva a disciplina        
for aluno in turma:  #para cada aluno na turma
    print("Nome: %s " % aluno['nome'].capitalize()) #escreva o nome
    
    bi = 1 #vamos usar este bi para indicar o bimestre
    
    for notas in aluno['notas']: #aninhamos um for para contar as notas na lista do dicionario

        print("Nota %i : %.1f" % (bi, notas)) #Eescreva as notas da lista de notas
        bi += 1 #incremenete o bimestre
        
    print("Media Final: %.1f" % aluno['media']) #mostre a media final
    print("Resultado: %s" % aluno['sit'])     #mostre o resultado
