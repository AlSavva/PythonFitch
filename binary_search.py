def gen_list(n, m, l):
    """Функция генерирует список заданной длинны l из случайных целых чисел в
    диапазоне от n до m."""
    from random import randint
    return [randint(n, m) for _ in range(l)]


def binary_search(list, item):
    """Функция для осуществления метода бинарного поиска
    в сортированных спискахю Скорость исполнения О(log_n)"""
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


# Алгоритм сортировки выбором. Скорость выполнения О(n**2)

def find_smallest(list):
    """Функция реализует поиск наименьшего значения в произвольном списке.
    Возвращает индекс наименьшего элемента в списке."""
    smallest = list[0]
    smallest_ind = 0
    for i in range(1, len(list)):
        if list[i] < smallest:
            smallest = list[i]
            smallest_ind = i
    return smallest_ind


def chois_sort(list):
    """Функция реализует сортировку выбором произвольного списка, используя
    функцию find_smallest"""
    new_list = []
    for i in range(len(list)):
        smallest = find_smallest(list)
        new_list.append(list.pop(smallest))
    return new_list


def q_sort(list):
    """Функция реализует алгоритм быстрой сортировкию Скорость выполнения
    O(n*log_n)"""
    if len(list) <= 2:
        return list
    else:
        check = list[0]
        right = [i for i in list[1:] if i > check]
        left = [i for i in list[1:] if i <= check]
        return q_sort(left) + [check] + q_sort(right)


def my_decompose(lst):
    """Функция для разкладывания положительных и отрицательных элементов
    массива lst в два разных массива"""
    ls_positive = []
    ls_negative = []
    for i in lst:
        if i > 0:
            ls_positive.append(i)
        elif i < 0:
            ls_negative.append(i)
    return ls_positive, ls_negative
    # Худший вариант:


#     ls_positive = [i for i in lst if i > 0]
#     ls_negative = [i for i in lst if i < 0]
#     т.к. в данном алгоритме требуется два прохода по списку.


def my_insert(num, pos, lst):
    """Функция вставляет элемент num на позицию pos в массив lst(полная анология
    работы функции insert)"""
    lst.append(None)
    i = len(lst) - 1
    while i > pos:
        lst[i], lst[i - 1] = lst[i - 1], lst[i]
        i -= 1
    lst[pos] = num
    return lst


# Аналогичный результат можно получить в результате выполнения следующего
# короткого кода:
# lst_new = lst[:pos] + [num] + lst[pos:]
# однако реализация данного кода требует в 2 раза больше памятиб т.к.
# создается новый массив

def my_matrix(rows, cols):
    """Функция генерирует матрицу размером row x col из произвольных чисел от
    1 до 10"""
    from random import randint
    matrix = [[randint(1, 10) for _ in range(cols)] for _ in range(rows)]
    for line in matrix:
        for item in line:
            print(f'{item:>4}', end='')
        print()
    return matrix


def matrix_sum(matrix):
    """Функция выводит сумму по столбцам и по строкам матрицы."""
    sum_col = [0] * len(matrix[0])
    for rows in matrix:
        sum_row = 0
        for i, item in enumerate(rows):
            sum_row += item
            sum_col[i] += item
            print(f'{item:>4}', end='')
        print(f'    | {sum_row}')
    print('-' * (len(matrix) * 6))
    for s in sum_col:
        print(f'{s:>4}', end='')


def sqmatrix_diag_change(matrix):
    """Функция меняет значения главной и побочной диагонали квадратной
    матрицы"""
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if i == j:
                spam = matrix[i][j]
                matrix[i][j] = matrix[i][size - 1 - j]
                matrix[i][size - 1 - j] = spam
    for line in matrix:
        for item in line:
            print(f'{item:>4}', end='')
        print()
    return matrix


def matrix_diag_change(matrix):
    """Функция меняет значения главной и побочной диагонали квадратной
    матрицы"""
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if i == j:
                spam = matrix[i][j]
                matrix[i][j] = matrix[i][size - 1 - j]
                matrix[i][size - 1 - j] = spam
    for line in matrix:
        for item in line:
            print(f'{item:>4}', end='')
        print()
    return matrix


# my_list = gen_list(-50, 50, 20)
# print(my_list)
# print(my_insert(1000, 13, my_list))
a = my_matrix(5, 5)
print()
matrix_diag_change(a)
