from contextlib import contextmanager


@contextmanager
def my_open(path_lib, mode):
    try:
        print('open file')
        lib = open(path_lib, mode, encoding='utf-8')
        yield lib
    except Exception as e:
        print('there was an error opening', e)
        
    finally:
        print('Close file')
        lib.close()
    
    
    
with my_open('context_class.txt', 'w') as lib:
    lib.write('line 1\n')
    print('WITH',lib)