from datetime import datetime


#nasc = input('Digite a data de nascimento (00/00/0000): ')
nasc = "06/10/1994"
nasc = datetime.strptime(nasc, '%d/%m/%Y')
hoje = datetime.today()

anos = hoje.year - nasc.year - ((hoje.month, hoje.day) < (nasc.month, nasc.day))

print(anos)