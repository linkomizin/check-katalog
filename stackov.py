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


def second_step():
    if (os.path.exists('database.pcl')) == False:
        get_structure(1)
    else:
        comparison_db()

def get_structure(save_db):
    path = system()
   
    path = path.rstrip(os.sep)
    w = os.walk(path)
    
    db_all_file = {}
    date_files = []

    for a, b, v in w:

        for files in v:
            fpath = []
            fpath.append(os.path.join(a,files))
            pdata =(os.path.join(a,files))
            adate = (time.ctime(os.stat(pdata).st_ctime))
            date_files.append(adate)

            afile= dict(dict.fromkeys(fpath, adate))
            db_all_file.update(afile)

    
    if save_db == 1:
        save_db_file(db_all_file)
    elif save_db == 2:
        return(db_all_file)


def save_db_file(db_all_file):
    fl = open("database.pcl", 'wb')
    pickle.dump(db_all_file, fl, 2)
    fl.close()



def load_db_file():
    fl = open("database.pcl", 'rb')
    e1 = pickle.load(fl)
    fl.close()
    return (e1)


def comparison_db():
    e1 = load_db_file()
    e2 = get_structure(2)
    print(e2)
    


