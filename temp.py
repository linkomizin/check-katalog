import datetime
from functools import reduce

db_main = []
a = ['1', '2', '3', '4', '5']
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

from_db_dict = ['asd', 'ssd', 'dsds', 'dsd', '2332']
for keys, dates in db_dict.items():
    print(dates)



def rasschet(arg1, arg2):

    new_dict =  dict.fromkeys(arg1, arg2)
    return(new_dict)

puh = map(rasschet, db_dict, from_db_dict)

for isd in puh:
    db_dict.update(isd)
    print(isd)

fol = reduce(rasschet, from_db_dict , db_dict)
print(fol)