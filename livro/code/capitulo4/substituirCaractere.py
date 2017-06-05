entrada = input("Insira sua altura: ")  #pedimos uma altura

for caracter in entrada:
    if caracter == ',':
        entrada = float(entrada.replace(',', '.'))

print(entrada)
