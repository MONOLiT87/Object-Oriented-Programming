import sys

#1
#s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#print(sys.getsizeof([]))
#print(sys.getsizeof([1]))
#print(sys.getsizeof([1, 2]))

#print(sys.getsizeof(s))

#print(sys.getsizeof(list(range (0, 100000000000000000000000))))

#2
def get_numbers(start, end, step):
    while start < end:
        yield start
        start += step
        
gen = get_numbers(0, 10, 1)
print(list(gen))
try:
    gen = get_numbers(1, 5, 2)
    for i in gen:
        print(i)
except StopIteration as e:
        print(e)
