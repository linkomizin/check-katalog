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
        path = ("/Users/akira/Downloads/python и pyqt5 ирм/sudoku")
        return path

path = system()

s = {}
roots = {}
di ={}
files = {}

w = os.walk(path)
for data in w:

    data = list(data)
    # pprint.pprint(data)
    # print(len(data))
    a = data[0]
    b = data[1]
    v = data[2]

    # b = list(b)
    asep = a.split(os.sep)[-1]

    # roots = dict.fromkeys(a)
    folders = dict.fromkeys(b)
    # print(folders)
    files = dict.fromkeys(v)
    # print(files)

    s[asep] = folders,files





    # folders = reduce(dict.get, b, roots)



pprint.pprint(s)



