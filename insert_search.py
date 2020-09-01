# сортировка введенного списка методом вставки

rating_list = list(map(int,
                       input('Для создания списка введите группу целых чисел,'
                             'разделённых пробелами: ').split()))
for num in range(1, len(rating_list)):
    i = num
    while i > 0 and rating_list[i - 1] > rating_list[i]:
        rating_list[i], rating_list[i - 1] = rating_list[i - 1], rating_list[i]
        i -= 1
print(f'Введённый список отсортирован:\n{rating_list}')
