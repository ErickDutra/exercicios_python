
class Multiply:
    def __init__(self, func):
        self.func = func
        self._multipler = 10
        
    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return result * self._multipler

@Multiply
def sum_(x,y):
    return x + y 

two_more_four = sum_(2,4)
print(two_more_four)