class MyError(Exception):
    ...
    
class OtherError(Exception):
    ...
    
    
def rise_():
    exception_ = MyError('a', 'b', 'c')
    exception_.add_note('Olha a nota')
    exception_.add_note('errou')
    raise exception_

try:
    rise_()
except (MyError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OtherError('Lançar novamente')
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('mais uma vez')
    raise exception_ from error 
    