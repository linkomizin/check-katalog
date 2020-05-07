import os
import time
import pprint
from datetime import datetime

import sys
import platform
from functools import reduce
import pickle

print(platform.system())

print(os.getcwd())

def system():
    name_sys = platform.system()
    if "Win" in name_sys:
        path = ("C:\\Temp\\ПРиказы")
        return path
    if "Lin" in name_sys:
        path = (r"/storage/emulated/0/Documents")
        return path
    if "Dar" in name_sys:
        path = (r"/Users/akira/Downloads/python и pyqt5 ирм/sudoku")
        return path


def second_step():
    if (os.path.exists('database.pcl')) == False:
        get_structure(1)
    elif(os.path.exists('database.pcl')) == True:
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
            # adate = (time.ctime(os.stat(pdata).st_ctime))
            adate = ((os.stat(pdata).st_ctime))
            adate = datetime.fromtimestamp(adate).strftime("%d-%m-%Y %H:%M")
            # date_files.append(adate)
            size = os.path.getsize(pdata)

            data = [adate, size]
            print(data)
            f = dict.fromkeys(fpath, data)
            # afile = {f: data}
            db_all_file.update(f)

    print(db_all_file)
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
    return (dict(e1))

def get_name_file(args):
    if isinstance(args, set):
        list=[]
        for strting in args:
            strting = str(strting)
            file_name = strting.rsplit(os.sep, maxsplit=1)
            list.append(file_name[1])
        return list
    elif isinstance(args, dict):
        list=[]
        for key in args:
            list.append(key.rsplit(os.sep, maxsplit=1)[1])
        return list




def comparison_db():
    '''
    здесь производится сравнение ключей двух словарей.
    ключи переводятся в множество.
    дальнейшие опрации сравнения основывываются на множествах
    '''
    e1 = load_db_file()
    e2 = get_structure(2)

    e1_keys = set(e1.keys())
    e2_keys = set(e2.keys())

    removed_keys = e1_keys - e2_keys
    if removed_keys:
        get_name_file(removed_keys)
        print('были удалены:\n', get_name_file(removed_keys), '\n')
    added_keys = e2_keys - e1_keys
    if added_keys:
        get_name_file(added_keys)
        print('были добавлены:\n', get_name_file(added_keys) )

    print(len(added_keys), '|--| ', len(removed_keys) )

    # пересечения
    intersect_keys = e1_keys.intersection(e2_keys)
    if intersect_keys:
        print('\nбыли найдены совпадения:\n', get_name_file(intersect_keys),'\n')
    # print(('пересечения\n', intersect_keys))

    # проверка на изменения файла
    modififed = {o:(e1[o], e2[o]) for o in intersect_keys if e1[o] != e2[o] }
    if modififed:
        print('\nбыли найдены изменения:' ,get_name_file(modififed), '\n')
        # sravnenie(modififed)



def sravnenie(data):

    for  keys, values in data:
        print(values)
        if values[1] > values[0]:
            print('новое' )

second_step()