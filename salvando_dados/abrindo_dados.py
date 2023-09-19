import json
from salvando_dados import Pessoa

with open( 'dados.json', 'r', encoding= 'utf8' ) as arquivo:
    pessoas = json.load( arquivo )
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    print(p1.nome,p1.idade )
    print(p2.nome,p2.idade )
    