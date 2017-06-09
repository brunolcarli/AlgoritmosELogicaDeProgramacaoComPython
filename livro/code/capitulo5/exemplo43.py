matriz = ['1 dimensao da matriz', #abrimos uma lista
         ['2 dimensao da matriz',#abrimos uma lista dentro da lista
          ['3 dimensao da matriz',#abrimos uma lista na lista da lista
           ['4 dimensao da matriz']#abrimos uma lista na lista da lista na lista
           ]]] #feche todas as listas

#vamos acessar as listas pelo indice

print(matriz[0]) #acesso a primeira dimensao da matriz
print(matriz[1][0]) #acesso a segunda dimensao da matriz
print(matriz[1][1][0]) #acesso a terceira dimensao da matriz
print(matriz[1][1][1][0]) #acesso a quarta dimensao da matriz


