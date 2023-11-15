def to_add_repr(cls):
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = my_repr
    return cls

@to_add_repr
class Time:
    def __init__(self, name):
        self.name = name
   
@to_add_repr     
class Planet:
    def __init__(self, name):
        self.name = name
        

brazil = Time('Brasil')
portugal = Time('portugal')

earth = Planet('earth')
mars = Planet('mars')

print(brazil)
print(portugal)
print()
print(earth)
print(mars)