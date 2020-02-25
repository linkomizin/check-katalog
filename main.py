import os
import time
import pprint
import datetime

path =("Z:\\ue video\\")
scandiretories = os.listdir(path)
time_item = os.stat(path).st_ctime_ns
times = []

# for d in scandiretories():
#     time_item = os.stat(d).st_ctime
#     time_item.append(times)
# pprint.pprint(scandiretories)
# print (time_item)


for entry in os.scandir(path):
    print((datetime.datetime(int(entry.stat().st_ctime)).strtime))
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
file_list = os.listdir(path)
full_list = [os.path.join(path, i) for i in file_list]
time_sorted_list = sorted(full_list, key = os.path.getmtime)

# pprint.pprint(time_sorted_list)
