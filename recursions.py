# Реализация функции Аккермана(служит для проверки компилятора на возможность
# оптимизации рекурсии)
# import sys


# sys.setrecursionlimit(3000)

def akk(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return akk(m - 1, 1)
    return akk(m - 1, akk(m, n - 1))


# print(akk(3, 8)) - выдаст ошибку при выполненииб из-за переполнения
# стека вызовов. Для устранения ошибки необходимо изменить размер стека вызовов
# (по умолчанию глубина стека ограничена 1000).Изменение глубины стека стр. 3-6
# С величиной этого параметра не стоит злоупотреблять.


# Реализация алгоритма Евклида(нахождение НОД(gcd)) 3-мя способами:
# Variant#1 - cycle based on subtraction: недостаток - низкая скорость работы на больших числах.

def gcd_cyc(m, n):
    while m != n:
        if m > n:
            m -= n
        else:
            n -= m
    return m


# Variant#2 - recursion: недостаток - при некоторых значениях возможно
# переполнение стека вызовов.

def gcd_rec(m, n):
    if n == 0:
        return m
    return gcd_rec(n, m % n)


# Variant#2 - cycle based on division: наиболее оптимальный алгоритм для данной
# задачи.

def gcd_cycdiv(m, n):
    while n != 0:
        m, n = n, m % n
    return m


print(gcd_cycdiv(542, 24234567892))
