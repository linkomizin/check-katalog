import os
import time
import pprint
import datetime
import time
import sys




path =("//Users//akira//Downloads//python и pyqt5 ирм")
scandiretories = os.listdir(path)
time_item = os.stat(path).st_ctime
time_item = time.ctime(int(time_item))

# my_string = ("__".join(times))
# pprint.pprint(my_string)

# d = os.stat(file).st_ctime

w = os.walk(path, topdown=True)

a =[]
for cata, dir, file in w:
    data = {}
    print(cata)
    # data.update({"name_catalog": cata})
    for catalog_directory in cata:
        data.update({"name": catalog_directory})
#    print(data)
    a.append(data)
print(data)


def scaner1():
    for f in scandiretories:

        # print(f)
        print(path + f)
        aas = os.stat(path + f).st_ctime
        aas = time.ctime(aas)
        print(aas)


def scaner2():
    for entry in os.scandir(path):
        d = entry.path
        d = os.stat(d).st_ctime
        d = time.ctime(d)
        print(entry.path)
        print(d)

        # print(entry.path, entry.name, entry.stat())






# for filename in os.listdir(path):
#     info = os.stat(filename)
#     pprint.pprint (info)


# a = os.path.getatime(path)  # время последнего доступа
# b = os.path.getmtime(path)  # время последнего изменения
# c = os.path.getctime(path)  # время создания (Windows), время последнего изменения (Unix)
# print([time.ctime(x) for x in [a, b, c]])

# Необходимо отсортировать в коде файлы по дате создания, помог код:


# path = "/path/to/folder/"
# Sort file names with path
# file_list = os.listdir(path)
# full_list = [os.path.join(path, i) for i in file_list]
# time_sorted_list = sorted(full_list, key = os.path.getmtime)

# pprint.pprint(time_sorted_list)
