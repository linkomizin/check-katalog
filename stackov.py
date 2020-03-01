# -*- coding: UTF-8 -*-
from os import path, listdir
from time import ctime

folder  =("//Users//akira//Downloads//")
for name in listdir(folder):
    full_name = path.join(folder, name)
    if path.isfile(full_name):
        name_, _ext = path.splitext(name)
        time_info = [ctime(fn(full_name)) for fn in (path.getatime, path.getmtime, path.getctime)]
        file = {
            'каталог': folder,
            'файл': full_name,
            'файл_имя': name_,
            'файл_расширение': _ext,
            'время последнего доступа': time_info[0],
            'время последнего изменения': time_info[1],
            'время создания': time_info[2],
        }
        print('\n'.join('{:<30} : {}'.format(*f) for f in sorted(file.items())), '\n')
