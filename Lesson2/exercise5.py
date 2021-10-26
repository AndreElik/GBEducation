#     5. Создать вручную список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
#     A. Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде
# <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки,
# как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
#     B. Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект
# списка после сортировки остался тот же).
#     C. Создать новый список, содержащий те же цены, но отсортированные по убыванию.
#     D. Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию,
# написав минимум кода?
from random import randint


def generator():
    parent_list = []
    for i in range(20):
        parent_list.append(randint(1, 10000) / 100)
    return parent_list


lst = generator()
print(lst)
for idx in lst:
    int_part = str(idx).split('.')[0]
    div_part = str(idx).split('.')[1].ljust(2, '0')
    print('"' + int_part, 'руб', div_part, 'коп"', end=', ')
lst.sort()
print("\n\n")
for i in lst:
    int_part = str(i).split('.')[0]
    div_part = str(i).split('.')[1].ljust(2, '0')
    print('"' + int_part, 'руб', div_part, 'коп"', end=', ')
print("\n\n")
for j in lst[::-1]:
    int_part = str(j).split('.')[0]
    div_part = str(j).split('.')[1].ljust(2, '0')
    print('"' + int_part, 'руб', div_part, 'коп"', end=', ')
print("\n\n")
for j in lst[15:]:
    int_part = str(j).split('.')[0]
    div_part = str(j).split('.')[1].ljust(2, '0')
    print('"' + int_part, 'руб', div_part, 'коп"', end=', ')







