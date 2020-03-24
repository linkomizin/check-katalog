import datetime

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

# добавляю значения по ключам
for key in db_main[1].keys():

	print(key)

from_db_dict = ['asd', 'ssd', 'dsds','dsd', '2332']
for dates in from_db_dict:
	db_dict = dates
	print (db_dict)
print(db_main[1])
# from_dict = dict(db_main[1])
# db_main[1] = from_db_dict
print ()