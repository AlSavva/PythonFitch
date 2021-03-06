def gen_list(n, m, l):
    """Функция генерирует список заданной длинны l из случайных целых чисел в
    диапазоне от n до m."""
    from random import randint
    return [randint(n, m) for _ in range(l)]


def my_sum(list):
    if list == []:
        return 0
    return list[0] + my_sum(list[1:])


def my_len(list):
    if list == []:
        return 0
    return 1 + my_len(list[1:])


def my_maxlst(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = my_maxlst(list[1:])
    return sub_max if sub_max > list[0] else list[0]


# Дано натуральное число n. Выведите все числа от 1 до n.
def my_numbers(n):
    if n == 1:
        return n
    else:
        return str(my_numbers(n - 1)) + ' ' + str(n)


# Даны два целых числа A и В (каждое в отдельной строке). Выведите все числа
# от A до B включительно, в порядке возрастания, если A < B, или в порядке
# убывания в противном случае.
def my_int(a, b):
    if a > b:
        if a == b:
            return str(b)
        return str(a) + ' ' + str(my_int(a - 1, b))
    else:
        if a == b:
            return str(a)
        return str(a) + ' ' + str(my_int(a + 1, b))


# Дано натуральное число N. Вычислите сумму его цифр.
# При решении этой задачи нельзя использовать строки, списки, массивы
# (ну и циклы, разумеется).
def sum_num(n):
    if n // 10 < 1:
        return n % 10
    return sum_num(n // 10) + n % 10


# Дано натуральное число N. Выведите все его цифры по одной, в обратном
# орядке, разделяя их пробелами или новыми строками.
# При решении этой задачи нельзя использовать строки, списки, массивы (ну и
# циклы, разумеется). Разрешена только рекурсия и целочисленная арифметика.
def str_numreverse(n):
    if n // 10 < 1:
        return str(n)
    return str(n % 10) + ' ' + str_numreverse(n // 10)


# Дано натуральное число N. Выведите все его цифры по одной, в обычном
# порядке, разделяя их пробелами или новыми строками.
# При решении этой задачи нельзя использовать строки, списки, массивы (ну и
# циклы, разумеется). Разрешена только рекурсия и целочисленная арифметика.
def str_num(n):
    if n // 10 < 1:
        return str(n)
    return str_num(n // 10) + ' ' + str(n % 10)


# Дано натуральное число N. Выведите слово YES, если число N является точной
# степенью двойки, или слово NO в противном случае.
# Операцией возведения в степень пользоваться нельзя!
def pow_2real(n):
    if n % 2 == 0:
        if n // 2 == 1:
            return 'yes'
        return pow_2real(n // 2)
    return 'no'


# Дано натуральное число n>1. Проверьте, является ли оно простым. Программа
# должна вывести слово YES, если число простое и NO, если число составное.
# Алгоритм должен иметь сложность O(logn).
# Указание. Понятно, что задача сама по себе нерекурсивна, т.к. проверка
# числа n на простоту никак не сводится к проверке на простоту меньших чисел.
# Поэтому нужно сделать еще один параметр рекурсии: делитель числа,
# и именно по этому параметру и делать рекурсию.
def prime_ornot(n, div=2):
    if n < 2:
        return 'no'
    elif n == 2:
        return 'yes'
    elif n % div == 0:
        return 'no'
    elif div < n // 2:
        return prime_ornot(n, div + 1)
    else:
        return 'yes'


# Решето Эратосфена - функция возвращает список из простых чисел до заданного
# числа n
def erat(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2
            while j < n:
                sieve[j] = 0
                j += i
    res = [i for i in sieve if i != 0]
    return res

def binary(num):
    """Функция выводит представление десятичного числа в двоичной системе"""
    s = ''
    while num > 0:
        s = str(num % 2) + s
        num //= 2
    return s

def multinary(num, m):
    """Функция выводит представление десятичного числа(num)
    в системе исчисления(m) 0 < m <= 10"""
    s = ''
    while num > 0:
        s = str(num % m) + s
        num //= m
    return s

# Удаление элемента списка во время его итерирования:

mylist = gen_list(1,8,10)
print(mylist)
for el in mylist[:]:
    mylist.remove(el)
print(mylist)

# Или:
mylist1 = gen_list(1,8,10)
print(mylist1)
for index, el in enumerate(mylist1[:]):
    mylist1.remove(el)
print(mylist1)

# Крестики-нолики где "Х" побеждает с первой попытки.
# Вариант неверный:

row = [''] * 3
board = [row] * 3
print(board)
board[0][0] = 'X'
print(board)

# Вариант верный:

board = [[''] * 3 for i in range(3)]
print(board)
board[0][0] = 'X'
print(board)

# Разница при ссылках на объекты:

a = [1, 2, 3, 4]
b = a
a = a + [6, 7, 8]
print(a, b)
a = [1, 2, 3, 4]
b = a
a += [6, 7, 8]
print(a, b)

# Сохранить только уникальные значения списка:

a = gen_list(1, 4, 10)
print(a)
a = list(set(a))
print(a)

# Как сделать ключём словаря изменяемый объект:

set_x = [1, 2, 3]
lst_x = [4, 5, 6]
dict_x = {frozenset(set_x): lst_x}
print(dict_x)
dict_y = {tuple(lst_x): set_x}
print((dict_y))


# ml = gen_list(4, 85, 10)
# print(ml)
# print(my_sum(ml))
# print(my_len(ml))
# print(my_maxlst(ml))
# my_list=list(range(1,100))
# print([(i,prime_ornot(i)) for i in my_list])
# print(prime_ornot(17))

# Задача: Пользователь вводит количество предприятийб названияб плановую и
# фактическую прибыль каждого предприятия.
# Вычислить процент выполнения плана и вывести данные с предварительной
# фильтрацией.

k = int(input('Введите количество предприятий: '))
enterprises = {}
for i in range(1, k + 1):
    name = input('Введите название предприятия: ')
    enterprises[name] = [float(input('Плановая прибыль: ')),
                         float(input('Фактическая прибыль: '))]
    enterprises[name].append(enterprises[name][1] / enterprises[name][0])
print('Фактическая прибыль больше 10, но план не выполнен (меньше 100%)')
for key, value in enterprises.items():
    if value[1] > 10 and value[2] < 1:
        print(f'Предприятие {key} заработало {value[1]}, что составило'
              f' {value[2] * 100:.2f}%')



