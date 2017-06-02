peso = float(input("Insira seu peso: ")) #receber o valor do peso
altura = float(input("Insira sua altura: ")) #receber o valor da altura

imc = peso/(altura**2) #calcular o imc

if imc < 20: #se o imc for menor que 20
    print("Abaixo do peso ideal")

else: # senao
    if imc <= 25: #se for menor que 25
        print("Seu imc esta normal")
    else: #senao
        if imc <= 30: #se for menor que 30
            print("Excesso de peso")         
        elif imc > 30 and imc <= 35: #ou se for maior que 30 e menor que 35
            print("Obesidade")
        else: #ou entao se for mairo que isso
            print("Obesidade morbida")

print("Seu imc e: ", imc) #finalmente mostramos o imc



