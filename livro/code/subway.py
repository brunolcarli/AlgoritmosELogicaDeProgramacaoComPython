

while True:

	pao = 0
	while not pao:
		print('-' * 30)
		print("escolha o pão: \n[1]Italiano Branco\n[2]Três Queijos\n[3]Parmesão e Orégano\n[4]9 Grãos")
		print('-' * 30)
		pao = input()
		if pao == '1':
			pao = 'Italiano Branco'
		elif pao == '2':
			pao = 'Três Queijos'
		elif pao == '3':
			pao = 'Parmesão e Orégano'
		elif pao == '4':
			pao = '9 Grãos'
		else:
			pao = 0
			print("Sabor inválido")

	tamanho = 0
	while not tamanho:
		print('-' * 30)
		print("Escolha o tamanho\n[1]15cm\n[2]30cm")
		print('-' * 30)
		tamanho = input()
		if tamanho == '1':
			tamanho = '15cm'
		elif tamanho == '2':
			tamanho = '30cm'
		else:
			tamanho = 0
			print("Tamanho inválido")

	sabor = 0
	while not sabor:	
		print('-' * 30)
		print("Escolha o sabor: ")
		print("[1]BMT\n[2]Frango\n[3]Presunto\n[4]Rosbife\n[5]Carne e Queijo\n[6]Atum\n[7]Peito de Peru\n[8]Vegetariano")
		print('-' * 30)
		sabor = input()
		if sabor == '1':
			sabor = 'BMT'
		elif sabor ==  '2':
			sabor = 'Frango'
		elif sabor == '3':
			sabor = 'Presunto'
		elif sabor == '4':
			sabor = 'Rosbife'
		elif sabor == '5':
			sabor = 'Carne e Queijo'
		elif sabor == '6':
			sabor = 'Atum'
		elif sabor == '7':
			sabor = 'Peito de Peru'
		elif sabor == '8':
			sabor = 'Vegetariano'
		else:
			sabor = 0
			print('Sabor inválido')

	queijo = 0
	while not queijo:		
		print('-' * 30)
		print("Escolha o queijo ")
		print("[1]Cheddar\n[2]Prato\n[3]Suiço")
		print('-' * 30)
		queijo = input()
		if queijo == '1':
			queijo = 'Cheddar'
		elif queijo == '2':
			queijo = 'Prato'
		elif queijo == '3':
			queijo = 'Suiço'
		else:
			queijo = 0
			print("Queijo inválido")

	salada = ''
	saladas = salada
	while salada != '0':
		print('-' * 30)
		print("Escolha suas saladas")
		print("[1]Alface\n[2]Tomate\n[3]Pimentão\n[4]Cebola\n[5]Pickles\n[6]Azeitonas\n[0]Próximo")
		print('-' * 30)
		salada = input()
		if salada == '1':
			saladas += 'Alface, '
		elif salada == '2':
			saladas += 'Tomate, '
		elif salada == '3':
			saladas += 'Pimentão, '
		elif salada == '4':
			saladas += 'Cebola, '
		elif salada == '5':
			saladas += 'Pickles, '
		elif salada == '6':
			saladas += 'Azeitonas, '
		else:
			if salada != '0':
				print('Salada inexistente')
	saladas = saladas[0:-2] + '.'

	molho = ''
	molhos = molho
	while molho != '0':
		print('-' * 30)
		print("Escolha o molho")
		print("[1]Maionese\n[2]Ketchup\n[3]Mostarda\n[4]Chipotle\n[5]Agridoce\n[6]Parmesão\n[7]Barbecue\n[0]Próximo")
		print('-' * 30)
		molho = input()
		if molho == '1':
			molhos += 'Maionese, '
		elif molho == '2':
			molhos += 'Ketchup, '
		elif molho == '3':
			molhos += 'Mostarda, '
		elif molho == '4': 
			molhos += 'Chipotle, '
		elif molho == '5':
			molhos += 'Agridoce, '
		elif molho == '6':
			molhos += 'Parmesão, '
		elif molho == '7':
			molhos += 'Barbecue, '
		else:
			if molho != '0':
				print("Molho inválido")

	molhos = molhos[0:-2] + '.'

	bebida = 0
	while not bebida:
		print('-' * 30)
		print("Acompanha bebida?")
		print('[1]Refrigerante 300ml\n[2]Refrigerante 500ml\n[3]Refrigerante lata\n[4]Suco\n[5]Chá\n[0]Próximo')
		print('-' * 30)
		bebida = input()
		if bebida == '1':
			bebida = 'Refrigerante 300ml'
		elif bebida == '2':
			bebida = 'Refrigerante 500ml'
		elif bebida == '3':
			bebida = 'Refrigerante lata'
		elif bebida == '4':
			bebida = 'Suco'
		elif bebida == '5':
			bebida = 'chá'
		elif bebida == '0':
			bebida = 'Sem bebida'
		else:
			bebida = 0
			print('bebida inválida')

	cookie = ''
	cookies = cookie
	while cookie != '0':
		print('-' * 30)
		print('Cookies?')
		print('[1]Chocolate\n[2]Baunilha\n[0]Próximo')
		print('-' * 30)
		cookie = input()
		if cookie == '1':
			cookies += 'Cookie Chocolate, '
		elif cookie == '2':
			cookies +='Cookie Baunilha, '
		else:
			if cookie != '0':
				print("Opção inválida")

	cookies = cookies[0:-1] + '.'

	pedido = [sabor, tamanho, bebida, cookies]
	
	sanduiche = {
		'Pao': pao,
		'Tamanho' : tamanho,
		'Sabor' : sabor,
		'Queijo': queijo,
		'Salada' : saladas,
		'Molho' : molhos,
	}


	print('-' * 30)
	print("Seu pedido:\n")
	for itens in pedido:
		print(itens)
	print('-' * 30)
	print("Sanduiche:\n")
	for chave, valor in sanduiche.items():
		print("%s: %s" % (chave, valor))
	print('-' * 30)

	break