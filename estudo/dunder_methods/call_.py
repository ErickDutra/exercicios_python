
class CallMe:
    def __init__(self, phone):
        self.phone = phone
            
    def __call__(self, name):
        print(name, "Calling", self.phone)
           
call_1 = CallMe('23988880000')
return_ = call_1('Erick')
