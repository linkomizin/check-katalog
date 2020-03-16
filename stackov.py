import os
import time
import pprint
import datetime
import time
import sys
import platform
from functools import reduce

print(platform.system())

def system():
    name_sys = platform.system()
    if "Win" in name_sys:
        path = ("C:\\Temp\\ПРиказы")
        return path
    if "Lin" in name_sys:
        path = ("Home")
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
        subdir = dict.fromkeys(v)

        # print(asep)

        folders = reduce(dict.get, asep[:-1], dir)
        # print(folders)

        folders[asep[-1]] = subdir
    return dir



print(get_structure())


#



