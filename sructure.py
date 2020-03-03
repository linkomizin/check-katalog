
import os, pprint
from functools import reduce

def get_struct(rootdir):

    dir = {}
    rootdir = rootdir.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = reduce(dict.get, folders[:-1], dir)
        parent[folders[-1]] = subdir
    return dir
pprint.pprint(get_struct("/Users/akira/Downloads/python и pyqt5 ирм"))