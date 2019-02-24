#   Инкаплуляция.
#  Инкапсуляция позволяет скрывть реализацию методов,
# что делает их использование намного удобнее.

class Example(object):
    def __init__(self):
        self.a = 1      # обычная переменная (значение)
        self._b = 2     # работать можно с _b, но лучше не трогать
        self,__c = 3    # нейзменяемое значение
        print('{} {} {}'.format(
            self.a, self._b, self. __c))

    def call(self):
        print('Called!')

example = Example()
print(example.a)
print(example._b)

try:
    print(example.__c)
except AttributeError as ex:
    print(ex)
