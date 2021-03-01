lista_nomes = ['Ana', 'Ana Maria', 'Pedro', 'Elena', 'Helena', 'Elen']

for nome in lista_nomes:
	new_name = "|"
	for l in nome:
		new_name += f"{l}|"
	print(new_name)