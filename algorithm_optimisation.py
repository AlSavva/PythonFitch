import cProfile
import functools


def test_fib(func):
    """Функция тестирующая функции по вычислению чисел Фибоначчи"""
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    for index, item in enumerate(lst):
        assert item == func(index)
        print(f'Test {index} OK')


def my_fib(n):
    """Функция нахождения n-ого числа Фибоначчи при помощи рекурсии."""
    if n < 2:
        return n
    return my_fib(n - 1) + my_fib(n - 2)


# cProfile.run('my_fib(10)')


# test_fib(my_fib)
# "algorithm_optimisation.my_fib(10)"
# 1000 loops, best of 5: 31.3 usec per loop

# "algorithm_optimisation.my_fib(15)"
# 1000 loops, best of 5: 210 usec per loop

# "algorithm_optimisation.my_fib(20)"
# 1000 loops, best of 5: 2.34 msec per loop

# "algorithm_optimisation.my_fib(25)"
# 1000 loops, best of 5: 25.9 msec per loop

# cProfile.run('my_fib(10)')
# 180 function calls (4 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     177/1    0.000    0.000    0.000    0.000 algorithm_optimisation.py:12(my_fib)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('my_fib(15)')

# 1976 function calls (4 primitive calls) in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#    1973/1    0.000    0.000    0.000    0.000 algorithm_optimisation.py:12(my_fib)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('my_fib(20)')
# 21894 function calls (4 primitive calls) in 0.005 seconds
# 21891/1    0.005    0.000    0.005    0.005 algorithm_optimisation.py:12(my_fib)

# выводы: быстрый в написании код, однако, скорость алгоритма О(2**n)

def fib_dict(n):
    """Вычисление n-ного числа Фибоначчи, с сохранением промежуточного
    результа в словарь."""
    fib_d = {0: 0, 1: 1}
    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]
        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_d[n]
    return _fib_dict(n)

# test_fib(fib_dict)

# fib_dict(10)
# 1000 loops, best of 5: 3.9 usec per loop

# "algorithm_optimisation.fib_dict(20)"
# 1000 loops, best of 5: 7.51 usec per loop

# "algorithm_optimisation.fib_dict(100)"
# 1000 loops, best of 5: 37.4 usec per loop

# "algorithm_optimisation.fib_dict(200)"
# 1000 loops, best of 5: 75.8 usec per loop

# "algorithm_optimisation.fib_dict(500)"
# 1000 loops, best of 5: 205 usec per loop

# cProfile.run('fib_dict(20)')

# cProfile.run('fib_dict(10)')
# 23 function calls (5 primitive calls) in 0.000 seconds
# 19/1    0.000    0.000    0.000    0.000 algorithm_optimisation.py:67(_fib_dict)

# cProfile.run('fib_dict(20)')
# 43 function calls (5 primitive calls) in 0.000 seconds
# 39/1    0.000    0.000    0.000    0.000 algorithm_optimisation.py:67(_fib_dict)

# cProfile.run('fib_dict(100)')
# 203 function calls (5 primitive calls) in 0.000 seconds
# 199/1    0.000    0.000    0.000    0.000 algorithm_optimisation.py:67(_fib_dict)

# cProfile.run('fib_dict(200)')
# 403 function calls (5 primitive calls) in 0.000 seconds
# 399/1    0.000    0.000    0.000    0.000 algorithm_optimisation.py:67(_fib_dict)

# cProfile.run('fib_dict(500)')
# 1003 function calls (5 primitive calls) in 0.001 seconds
# 999/1    0.001    0.000    0.001    0.001 algorithm_optimisation.py:67(_fib_dict)

# cProfile.run('fib_dict(1000)')
# RecursionError: maximum recursion depth exceeded

# Время исполнения алгоритма О(n)

def fib_list(n):
    """Вычисление n-ного числа Фибоначчи, с сохранением промежуточного
    результа в список."""
    fib_l = [None]*10000
    fib_l[:2] = [0, 1]
    def _fib_list(n):
        if fib_l[n] is None:
            fib_l[n] = _fib_list(n - 1) + _fib_list(n - 2)
        return fib_l[n]
    return _fib_list(n)

# test_fib(fib_list)

# "algorithm_optimisation.fib_list(10)"
# 1000 loops, best of 5: 7.47 usec per loop

# "algorithm_optimisation.fib_list(20)"
# 1000 loops, best of 5: 10.9 usec per loop

# "algorithm_optimisation.fib_list(100)"
# 1000 loops, best of 5: 37.7 usec per loop

# "algorithm_optimisation.fib_list(200)"
# 1000 loops, best of 5: 71.5 usec per loop

# "algorithm_optimisation.fib_list(500)"
# 1000 loops, best of 5: 191 usec per loop

# cProfile.run('fib_list(10)')
# 23 function calls (5 primitive calls) in 0.000 seconds
# 19/1    0.000    0.000    0.000    0.000 algorithm_optimisation.py:123(_fib_list)

# cProfile.run('fib_list(20)')
# 43 function calls (5 primitive calls) in 0.000 seconds
# 39/1    0.000    0.000    0.000    0.000 algorithm_optimisation.py:123(_fib_list)

# cProfile.run('fib_list(100)')
# 203 function calls (5 primitive calls) in 0.000 seconds
# 199/1    0.000    0.000    0.000    0.000 algorithm_optimisation.py:123(_fib_list)

# cProfile.run('fib_list(200)')
# 403 function calls (5 primitive calls) in 0.000 seconds
# 399/1    0.000    0.000    0.000    0.000 algorithm_optimisation.py:123(_fib_list)

# cProfile.run('fib_list(500)')
# 1003 function calls (5 primitive calls) in 0.001 seconds
# 999/1    0.001    0.000    0.001    0.001 algorithm_optimisation.py:123(_fib_list)

# cProfile.run('fib_list(992)')
# 1987 function calls (5 primitive calls) in 0.002 seconds
# 1983/1    0.002    0.000    0.002    0.002 algorithm_optimisation.py:123(_fib_list)

# Время исполнения алгоритма О(n) однако, при одинаковости способов со
# словарем и списком, предпочтительнее список, т.к. он занимает меньше памяти,
# чем словарь

def fib_loop(n):
    """Функция нахождения n-ого числа Фибоначчи при помощи цикла."""
    if n < 2:
        return n
    first, second = 0, 1
    for i in range(2, n + 1):
        first, second = second, first + second
    return second

# test_fib(fib_loop)

# 1000 loops, best of 5: 714 nsec per loop      10
# 1000 loops, best of 5: 1.19 usec per loop     20
# 1000 loops, best of 5: 5.38 usec per loop     100
# 1000 loops, best of 5: 10.8 usec per loop     200
# 1000 loops, best of 5: 30.8 usec per loop     500
# 1000 loops, best of 5: 67 usec per loop       1000
# 1000 loops, best of 5: 1.57 msec per loop     10000

# cProfile.run('fib_loop(10000)') даёт постоянный результатб т.к. функция не
# рекурсивная.

# попробуем улучшить простую рекурсивную функцию my_fib(n) используя
# инструменты библиотеки functools
# lru_cache() действует по методу мемоизации(хранит в памяти какие значения n
# передаются функции и запоминает возвращаемый результат по аналогии со словарями
# и списками

@functools.lru_cache()
def my_fib1(n):
    """Функция нахождения n-ого числа Фибоначчи при помощи рекурсии."""
    if n < 2:
        return n
    return my_fib1(n - 1) + my_fib1(n - 2)

# 1000 loops, best of 5: 86.3 nsec per loop     10
# 1000 loops, best of 5: 88.5 nsec per loop     100
# 1000 loops, best of 5: 84.2 nsec per loop     200
# 1000 loops, best of 5: 85.2 nsec per loop     400
# RecursionError: maximum recursion depth exceeded in comparison 500

# Данный декоратор существенно повышает скоростьб но не избавляет от проблемы 
# переполнения стека вызовов.

# cProfile.run('my_fib1(10)')
# 14 function calls (4 primitive calls) in 0.000 seconds
# 11/1    0.000    0.000    0.000    0.000 algorithm_optimisation.py:202(my_fib1)

# cProfile.run('my_fib1(100)')
# 104 function calls (4 primitive calls) in 0.000 seconds
# 101/1    0.000    0.000    0.000    0.000 algorithm_optimisation.py:202(my_fib1)

# cProfile.run('my_fib1(200)')
# 204 function calls (4 primitive calls) in 0.000 seconds
# 201/1    0.000    0.000    0.000    0.000 algorithm_optimisation.py:202(my_fib1)

# cProfile.run('my_fib1(400)')
# 404 function calls (4 primitive calls) in 0.001 seconds
# 401/1    0.001    0.000    0.001    0.001 algorithm_optimisation.py:202(my_fib1)

# По итогамб самый оптимальный алгоритм - цикл.

# print(fib_loop(50000))