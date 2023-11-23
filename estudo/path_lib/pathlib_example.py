from pathlib import Path


path_project = Path()

#arquivo atual, pasta absoluta
print(path_project.absolute())

#caminho absoluto do arquivo atual "absolute()"
path_file = Path(__file__)
print(path_file)

#uso parent para achar pasta a cima 
print(path_file.parent)

#exemplo:

#pasta a frente, usado para gerar caminhos
history = path_file.parent / 'history.txt'
print(history)

#home do desktop
print(Path.home())

#Possibilidades, exemplo:
#Path.home() / 'Desktop'

#Criar arquivo:
history.touch()

#escrever no arquivo
history.write_text('Historia incrivel')

#ler arquivo
print(history.read_text())

#sobrescreve arquivo
history.write_text('Historia incrivel 2, o retorno')
print(history.read_text())

#apagar arquivo:
history.unlink()

# varias linhas
with history.open('a+') as file:
    file.write('tudo comecou...\n')
    file.write('num dia... \n')
    
print(history.read_text())
history.unlink()
