import os
import time
import pprint
import datetime
import time
import sys
import platform
from functools import reduce
import pickle

print(platform.system())

def system():
    name_sys = platform.system()
    if "Win" in name_sys:
        path = ("C:\\Temp\\ПРиказы")
        return path
    if "Lin" in name_sys:
        path = ("/workspace")
        return path
    if "Dar" in name_sys:
        path = ("//Users//akira//Downloads//python и pyqt5 ирм//sudoku")
        return path

# path = system()


def get_structure():
    path = system()
    # print(path)
    path = path.rstrip(os.sep)
    start = path.rfind(os.sep) + 1
    dir = {}
    w = os.walk(path)


    for a, b, v in w:

        # data = list(data)
        # # pprint.pprint(data)
        # # print(len(data))
        # a = data[0]
        # b = data[1]
        # v = data[2]
        asep = a[start:].split(os.sep)
        paths = []
        dates = []
        full_path = [paths, dates]
        for files in v:
            # full_path = (os.path.join(a,files))
            paths.append(os.path.join(a,files))
            date = (time.ctime(os.stat(os.path.join(a, files)).st_ctime))
            dates.append(date)
        # print(full_path)

            # Работает дата !!!
            # print("|-> ", full_path, "date: ", time.ctime(os.stat(full_path).st_ctime))
        # print(full_path)



        subdir = dict.fromkeys(v) # , os.stat(a.join(v)).st_ctime)



        folders = reduce(dict.get, asep[:-1], dir)
        # print(folders)

        folders[asep[-1]] = subdir

        # os.stat(   ).st_ctime
        # d = time.ctime(d)
        dumping(full_path)



    # fl = open("data/database.pcl", 'wb')
    # pickle.dump(dir, fl)
    # pickle.dump(full_path, fl)
    # return dir

def dumping(full_path):
    fl = open("data/database.pcl", 'wb')
    pickle.dump(full_path, fl)



get_structure()
fl = open("data/database.pcl", 'rb')
e = pickle.load(fl)
print(e)
