import os
import time
import pprint
import datetime
import time
import sys




path =("//Users//akira//Downloads//")
scandiretories = os.listdir(path)
time_item = os.stat(path).st_ctime
time_item = time.ctime(int(time_item))
times = []
times.append(scandiretories)
# my_string = ("__".join(times))
# pprint.pprint(my_string)


# d = os.stat(file).st_ctime

for f in times:
    k = len(f)
    print(k)
    # print(path + f)
    # aas = os.stat(path + str(f)).st_ctime
    # print(aas)
    # time_item = os.stat(d).st_ctime
#     time_item.append(times)
# pprint.pprint(scandiretories)
print(f)

# print (scandiretories)
# print (scandiretories, time_item)


# for entry in os.scandir():
#     print((time.ctime(int(entry.stat().st_ctime))))
#     scandiretories = os.listdir(entry)
#     print (scandiretories)
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
