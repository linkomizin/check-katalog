import datetime, time, data

db = []
a = ['1','2','3','4','5']

dateNow = datetime.datetime.now()
db.append(dateNow.strftime("%d-%m-%Y %H:%M"))

for names in a:
	slovar = dict.fromkeys(names)
	db.append(slovar)




print(db)
