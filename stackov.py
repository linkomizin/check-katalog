import os
import time
import pprint
import datetime
import time
import sys
import platform

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
        path = ("/Users/akira/Downloads/python и pyqt5 ирм/sudoku/modules")
        return path

path = system()

s = {}
w = os.walk(path)
for data in w:
    data = list(data)
    # pprint.pprint(data)
    print(len(data))
    a = data[0]
    b = data[1]
    v = data[2]

    asep = a.split(os.sep)[-1]
    print(data)

    s[asep] = a ,v
    slovar = {asep: a, }




pprint.pprint(s)



