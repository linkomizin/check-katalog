import datetime, time, data

db_main = []
a = ['1','2','3','4','5']
db_dict = {}
dateNow = datetime.datetime.now()
db_main.append(dateNow.strftime("%d-%m-%Y %H:%M"))

for names in a:
	slovar = dict.fromkeys(names)
	db_dict.update(slovar)

db_main.append(db_dict)



print(db_main)
db_key = db_main[1].keys()
# добавляю значения по ключам
for key in db_key:
   print(key)

