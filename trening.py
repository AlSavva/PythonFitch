def gen_list(n, m, l):
    """Функция генерирует список заданной длинны из случайных целых чисел"""
    from random import randint
    lst = []
    for i in range(l):
        lst.append(randint(n, m))
    return lst


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
        return pow_2real(n//2)
    return 'no'


# ml = gen_list(4, 85, 10)
# print(ml)
# print(my_sum(ml))
# print(my_len(ml))
# print(my_maxlst(ml))
# my_list=list(range(2,100,2))
# print([(i,pow_2real(i)) for i in my_list])
print(pow_2real(16))
