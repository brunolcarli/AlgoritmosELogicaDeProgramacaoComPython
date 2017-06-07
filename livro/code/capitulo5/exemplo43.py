lista = ['1 dimensao da lista', #abrimos uma lista
         ['2 dimensao da lista',#abrimos uma lista dentro da lista
          ['3 dimensao da lista',#abrimos uma lista na lista da lista
           ['4 dimensao da lista']#abrimos uma lista na lista da lista na lista
           ]]] #feche todas as listas

#vamos acessar as listas pelo indice

print(lista[0]) #acesso a primeira dimensao da lista
print(lista[1][0]) #acesso a segunda dimensao da lista
print(lista[1][1][0]) #acesso a terceira dimensao da lista
print(lista[1][1][1][0]) #acesso a quarta dimensao da lista


