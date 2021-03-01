from datetime import datetime


#nasc = input('Digite a data de nascimento (00/00/0000): ')
nasc = "06/10/1994"
nasc = datetime.strptime(nasc, '%d/%m/%Y')
print(datetime.today() - nasc)