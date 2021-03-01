lista_antiga = [('Pessoa1', 20), ('Pessoa 2', 21), ('Pessoa 3', 22)]
lista_nova = [('Pessoa1', 20), ('Pessoa 2', 21), ('Pessoa 3', 22), ('Pessoa 4', 23), ('Pessoa 5', 24)]

def extrair_novos_registros(lista_antiga, lista_nova):
	return list(set(lista_nova) - set(lista_antiga))


lista_novos_registros = extrair_novos_registros(lista_antiga, lista_nova)
print(lista_novos_registros)