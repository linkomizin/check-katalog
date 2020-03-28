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

# for bb in from_db_dict:
# 	reduce(db_dict.update({key: bb}), from_db_dict)

def rasschet(arg1, arg2):
    print(arg1, ' ---> ', arg2)
    new_dict =  dict.fromkeys(arg1, arg2)
    len(new_dict)


puh = map(rasschet, db_dict, from_db_dict)

for isd in puh:
    print(isd)
print(db_dict)



# print(db_dict)
# print(db_main[1])
# from_dict = dict(db_main[1])
# db_main[1] = from_db_dict
# print(list(enumerate(from_db_dict)))
