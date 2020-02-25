import os
import time

path =("Z:\\ue video")
scandiretories = os.listdir.getctime(path)
print(scandiretories)


  

# a = os.path.getatime(path)  # время последнего доступа
# b = os.path.getmtime(path)  # время последнего изменения
# c = os.path.getctime(path)  # время создания (Windows), время последнего изменения (Unix)
# print([time.ctime(x) for x in [a, b, c]])