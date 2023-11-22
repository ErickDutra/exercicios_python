# C:\Users\CLIENTE\Desktop\sitejogo
import os

#path example
path_ = os.path.join('C:/Users', 'CLIENTE', 'Desktop', 'sitejogo')

print(path_)


for folder_ in os.listdir(path_):
    path_complete = os.path.join(path_, folder_)
    if not os.path.isdir(path_complete ):
        continue
    for itens in os.listdir(path_complete ):
        print(itens)
