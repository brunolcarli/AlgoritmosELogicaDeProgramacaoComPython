def formatar(nome, sobrenome):         #definimos a funcao
    formatado = nome + " " + sobrenome #processamento da funcao 
    return formatado.title()           #retorno da funcao

meu_nome = "bruno" #string com nome
meu_sobrenome = "LUVIZotto CARLi" #string com sobrenome

nome_completo = formatar(meu_nome, meu_sobrenome) #chamada da funcao

print("Meu nome e ", nome_completo) #saida

