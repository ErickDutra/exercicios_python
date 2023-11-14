


class Carro:
    def __init__(self , nome):
        self.nome = nome

    def fabrica(self, fabricante, motor):
        print(f'carro: {self.nome} fabricado: {fabricante} com motor: {motor}')
        
class Motor:
    def __init__(self , nome):
        self.nome = nome
    
    
class Fabricante:
    def __init__(self , nome):
        self.nome = nome
        
        
fabricante = Fabricante('Fiat')
carro = Carro('Toro')
motor = Motor('V8')
carro.fabrica(vars(fabricante), vars(motor))

