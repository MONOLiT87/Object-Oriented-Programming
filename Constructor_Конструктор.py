# Конструктор вызывается при создании нового экземпляра

#1
class TestClass:
def __init__(self):
    print('Конструктор называется!')
    print('Я - это сам объект!', self)

t = TestClass()
t1 = TestClass()

#2
class Car:
    def __init__(self):
        self.color = 'red'

t = Car()
t1 = Car()

#2.1
class Car:
    engine = 'V8 Turbo'
    def __init__(self, requested_color):
        self.color = requested_color

t = Car('red')
t1 = Car('white')


# Конструктор может иметь параметры

class Table:
    def __init__(self, number_of_legs): # кол-во ножек
        print('У нового стола {} ножки в полях!'.format(
            number_of_legs))

t = Table(4)
t1 = Table(3)

# Но нам нужно сохранить их в полях!

class Chair:
    def __init__(self, color):
        self.color = color

c = Chair('green')
print(c, c.color)

c1 = Chair('Red')
print(c1.color)
print('переменная с не изменилась!', c.color)
