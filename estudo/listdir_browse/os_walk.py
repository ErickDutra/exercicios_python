# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
# C:\Users\CLIENTE\Desktop

import os
from itertools import count 

path_ = os.path.join('C:/Users','CLIENTE','Desktop','area','roms')
counter = count()


for root, dirs, files in os.walk(path_):
    the_counter = next(counter)
    print(the_counter,'path current:', root)
    
    for dir_ in dirs:
        print('  ', the_counter, 'Dir: ', dir_)
        
    for file_ in files:
        path_complete_folder = os.path.join(root, file_)
        print('  ', the_counter, 'FILE:', path_complete_folder)
    
    