caixa = 72 #definimos uma variavel com um valor

caixa = str(type(caixa)) #verificamos seu tipo e guardamos como string

if 'str' in caixa:
    print("Essa varivel e do tipo String (Literal)")
    
elif 'int' in caixa:
    print("Essa variavel e do tipo Inteiro")
    
elif 'float' in caixa:
    print("Essa variavel e do tipo float")
    
elif 'bool' in caixa:
    print("Essa variavel e do tipo bool")
    
else:
    print("Outro")



