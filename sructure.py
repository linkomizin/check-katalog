
import os, pprint
from functools import reduce

def get_struct(rootdir):

    dir = {}
    rootdir = rootdir.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    # print(rootdir)
    # print(start)

    for path, dirs, files in os.walk(rootdir):
        # отделяем имя папки от корневого каталога по разделителю
        # разделитель / или \ (os.sep) по вложенности
        folders = path[start:].split(os.sep)
        # создаем словарь по именам файлов
        # из последовательности files
        subdir = dict.fromkeys(files)
        # print(folders[:-1])
        # print(folders)
        # print(path, dirs)


        parent = reduce(dict.get, folders[:-1], dir)
        # print(parent)
        # добавление в словарь
        parent[folders[-1]] = subdir
        # print(parent)
    return dir
# pprint.pprint(get_struct("/Users/akira/Downloads/python и pyqt5 ирм/sudoku/modules"))
get_struct("/Users/akira/Downloads/python и pyqt5 ирм/sudoku/modules")






# {'modules': {'mainwindow.py': None,
#              'mylabel.py': None,
#              'previewdialog.py': None,
#              'widget.py': None}}

# {'modules': {'mainwindow.py': None,
#              'mylabel.py': None,
#              'previewdialog.py': None,
#              'vasuki': {},
#              'widget.py': None}}