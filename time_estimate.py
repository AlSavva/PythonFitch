import timeit

x = 2 + 2
print(timeit.timeit('x = 2 + 2'))
print(timeit.timeit('x = sum(range(10))'))

# синтаксис в терминале: python -m timeit -n 100 -s "import time_estimate"
# 100 loops, best of 5: 10 nsec per loop
import cProfile
def get_len(array):
    return len(array)

def get_sum(array):
    s = 0
    for i in array:
        s += i
    return s

def main():
    lst = [i for i in range(1000000)]
    a = get_len(lst)
    b = get_sum(lst)

cProfile.run('main()')