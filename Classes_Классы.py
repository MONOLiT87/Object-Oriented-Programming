class Car:
    pass

 c = Car()
 print(c, type(c))

# Классы могут иметь переменные, называемые полями


 class Room:
     number = 'Room 34'
     floor = 4

r = Room()
r1 = Room()
print(r.number, r1.number)
print(r.floor, r1.floor)

# Вы можете изменить значения:
r.number = 12
r.floor = '5 floor'
print(r.number, r1.number)
print(r.floor, r1.floor)

# Классы могут иметь функции внутри: это называется методами

class Door:
    def open(self): # обратите внимание, что «self» является объектом
    print('self is', self)
    print('Door is opened!')
    self.opened = True

d = Door()
d.opened()

# Методы могут принимать параметры

class Terminal:
    def hello(self, user_name):
        print('Я - это сам объект', self)
        print('Hello,' user_name)

t = Terminal()
t.hello('Nikita')
t.hello('Vova')

# Классы могут иметь как методы, так и поля

class Window:
    is_opened = False

    def open(self):
        self.is opened = not self.is opened
        print('Window is now', self,is_opened)

w = Window()
w1 = Window()

print('Начальное состояние', w.is_opened, w1.is_opened)

w.open()
print('Новое состояние,' w.is_opened, w1.is_opened)
