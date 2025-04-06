while True:	
	print('       Calculadoura     ')
	print('--'*15)
	print()

	nu1 = int(input('Digite o primeiro número: '))
	oq = input('Do que é a conta? (+ - x / xx // %): ')
	nu2 = int(input('Digite o outro número: '))

	print()

	if oq == '+' or oq == 'mais' or oq == 'Mais':
		print('{} + {} = {}'.format(nu1, nu2, nu1+nu2))
	
	elif oq == '-' or oq == 'menos' or oq == 'Menos':
		print('{} - {} = {}'.format(nu1, nu2, nu1-nu2))
	
	elif oq == 'x' or oq == 'X' or oq =='*' or oq =='vezes' or oq == 'Vezes':
		print('{} x {} = {}'.format(nu1, nu2, nu1*nu2))
	
	elif oq == '/' or oq == 'dividido' or oq == 'Dividido':
		print('{} / {} = {}'.format(nu1, nu2, nu1/nu2))
	
	elif oq == 'xx' or oq == 'XX' or oq == '**' or oq == 'elevado' or oq == 'Elevado':
		print('{} xx {} = {}'.format(nu1, nu2, nu1**nu2))
	
	elif oq == '//' or oq == 'divisão inteira' or oq == 'Divisão inteira':
		print('{} // {} = {}'.format(nu1, nu2, nu1//nu2))	  	  

	elif oq == '%' or oq == 'resto da divisão' or oq == 'Resto da divisão':
		print('{} % {} = {}'.format(nu1, nu2, nu1%nu2))
		
	else:
		print('forma de conta invalida')
	
	print('--'*15)
