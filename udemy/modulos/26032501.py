 # Criando datas com módulo datetime
 # datetime(ano, mês, dia)
 # datetime(ano, mês, dia, horas, minutos, segundos)
 # datetime.strptime('DATA', 'FORMATO')
 # datetime.now()
 # https://pt.wikipedia.org/wiki/Era_Unix
 # datetime.fromtimestamp(Unix Timestamp)
 # https://docs.python.org/3/library/datetime.html
 # Para timezones
 # https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
 # Instalando o pytz
 # pip install pytz types-pytz
from datetime import datetime

data = datetime(2025,3,26)
print(data)

dataExata = datetime.now()
print(dataExata)