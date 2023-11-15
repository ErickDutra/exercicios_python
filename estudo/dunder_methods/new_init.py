class A:
    def __new__(cls):
        print('before creator instance')
        instance = super().__new__(A)
        print('after creator instance')
        return instance
    
    def __init__(self):
        print('I am Init')
        
    def __repr__(self):
        return 'A()'

a = A()    
"""
a = object.__new__(A)
a.__init__()
print(a)"""