import os
import time
import pprint
import datetime
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
        path = ("/storage/emulated/0/Documents")
        return path
    if "Dar" in name_sys:
        path = ("//Users//akira//Downloads//python и pyqt5 ирм//sudoku")
        return path




def get_structure():
    path = system()
    # print(path)
    path = path.rstrip(os.sep)
    start = path.rfind(os.sep) + 1
    dir = {}
    w = os.walk(path)
    db_all_file = {}
    
    date_files = []

    for a, b, v in w:

        asep = a[start:].split(os.sep)

        for files in v:
            fpath = []
            fpath.append(os.path.join(a,files))
            pdata =(os.path.join(a,files))
            adate = (time.ctime(os.stat(pdata).st_ctime))
            date_files.append(adate)


            afile= dict(dict.fromkeys(fpath, adate))
            db_all_file.update(afile)

        subdir = dict.fromkeys(v) # , os.stat(a.join(v)).st_ctime)

        folders = reduce(dict.get, asep[:-1], dir)
        folders[asep[-1]] = subdir

    save_db_file(db_all_file)


    # fl = open("database.pcl", 'wb')
    # pickle.dump(dir, fl, 2)
    # pickle.dump(db_all_file, fl, 2)
    # fl.close()
    #print(fpath)
    #pprint.pprint(all_file)
#    print('/__: ', len(all_file))


    return dir

def save_db_file(db_all_file):
    fl = open("database.pcl", 'wb')
    pickle.dump(db_all_file, fl, 2)
    fl.close()







get_structure()

def load_db_file():
    fl = open("database.pcl", 'rb')
    e1 = pickle.load(fl)

    
    fl.close()
    return (e1)


def comparison_db():
    e1 = load_db_file()
    print(e1)

comparison_db()
