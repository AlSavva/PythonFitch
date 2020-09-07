def gen_list(n: int, m: int, l: int):
    """Функция генерирует список заданной длинны из случайных целых чисел
    n-нижняя граница для ГСЧ, m-верхняя граница, l-длинна списка"""
    from random import randint

    lst = []
    for i in range(l):
        lst.append(randint(n, m))
    return lst


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


my_list = gen_list(10, 15, 5)
a=chois_sort(my_list[:])
print(a)
b=q_sort(my_list)
print(b)
