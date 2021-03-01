lista_frases = ['Eu gosto de batatas', 'Eu estava andando de moto']
lista_frases += ['Ele estava comendo no restaurante']
lista_frases += ['O cachorro está passeando pelo parque']

for frase in lista_frases:
	for palavra in frase.split(" "):
		if palavra.endswith("ando") or palavra.endswith("endo") or palavra.endswith("indo"):
			print(palavra)