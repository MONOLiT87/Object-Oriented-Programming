# Простой декоратор, который ничего не делает кроме как : принимает-возвращает функцию
def decorate(func):
    print('Decorate')
    return func


a = decorate(str)
print(a==str)
print(a(123))
 

# Другая реализация декоратора:

import time

def decorate(func):
    
    
    def fake(value):
        start = time.clock()
        result = func(value)
        
        end = time.clock()
        print('Time is ', end - start)
        return result 
    
    
    return fake
@decorate
def my_str(value):
    return str(value)


#my_str = decorate(my_str)
print(my_str(123))
print(my_str([]))
print(my_str({})) 
