    #     2.
    #     Дан список:
    # ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
    # Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до
    # и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
    # ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"',
    # 'градусов']
    # Сформировать из обработанного списка строку:
    # в "05" часов "17" минут температура воздуха была "+05" градусов
    # Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие
    # для чисел со знаком?
    # Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
    # Главное: дополнить числа до двух разрядов нулём!
    #     3. *(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place). Эта задача намного
    #     серьёзнее, чем может сначала показаться.



parent_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
indx = 0
while indx < (len(parent_list)-1)
    

# idx = 0
# target_list = parent_list.copy()
# print(target_list)
# num = len(parent_list)
# while idx < num:
#     if target_list[idx].isdigit():
#         variable = int(target_list[idx])
#         variable = "{:02n}".format(variable)
#         target_list.insert(idx, '"')
#         target_list.insert(idx+1, variable)
#         target_list.insert(idx+2, '"')
#         num = num + 2
#         idx = idx + 2
#
#     else:
#         symbol_element = target_list[idx]
#         for i in range(len(target_list[idx])):
#             if symbol_element[i-1].isdigit():
#                 variable1 = int(symbol_element[i-1])
#                 variable1 = "{:02n}".format(variable1)
#                 #symbol_element[i-1] = variable1
#
#     idx = idx + 1
# print(target_list)