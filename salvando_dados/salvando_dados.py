import json


class Pessoa:
    ano_atual = 2022
     
    def __init__(self,nome,idade):
         self.nome = nome
         self.idade = idade
         
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
    

p1 = Pessoa('Joao', 35)
p2 = Pessoa('Erick', 25)

bd = [vars(p1), vars(p2)]


def fazer_dump():
    with open('dados.json', 'w', encoding='utf-8') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)
        
        
if __name__ == '__main__':
    fazer_dump()





