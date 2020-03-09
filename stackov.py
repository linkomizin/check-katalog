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
roots = {}
folders = {}
files = {}

w = os.walk(path)
for data in w:
    data = list(data)
    # pprint.pprint(data)
    print(len(data))
    a = data[0]
    b = data[1]
    v = data[2]
    b = list(b)
    asep = a.split(os.sep)[-1]
    print(asep)
    
    
    roots = dict.fromkeys(a)
    folders = dict.fromkeys(b)

    files = dict.fromkeys(b,v)
    # print(folders)
    # print(files)
    # s[roots] = 
    s[asep] =  files

    # for root in a:
    #     s[asep] = root

    # print(data)
    # s = {asep: "data" , a: "papka", v: "file"}
    
    # slovar = {asep: a, }




pprint.pprint(s)



