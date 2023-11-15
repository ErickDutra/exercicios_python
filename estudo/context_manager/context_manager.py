
# EX:
# with open('aula123.txt', 'w') as file:



class MyContextManager:
    def __init__(self, path_file, mod):
        self.path_file = path_file
        self.mod = mod
        self._file = None
        print('Initializing context manager')
        
    def __enter__(self):
        print('Enter context manager')
        print('Open File')
        self._file = open(self.path_file, self.mod, encoding= 'utf8' )
        return self._file
        
    def __exit__(self, class_exception, exception_, traceback_):
        print('close file')
        print('Exit context manager')
        self._file.close()
        
        
instance = MyContextManager('class123.txt', 'w')
    
with instance as file:
    file.write('Line 1')
    print('WITH ', file)
    

#with instance as context_manager:
 #   print('Whit', context_manager) #('Enter': 123  or None )