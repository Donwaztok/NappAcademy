from datetime import datetime


jogo = datetime.strptime("08/07/2014", '%d/%m/%Y')
print(datetime.today() - jogo)