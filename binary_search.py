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


my_list = list(map(int, input().split()))
print(chois_sort(my_list))
