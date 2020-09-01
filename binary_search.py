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
