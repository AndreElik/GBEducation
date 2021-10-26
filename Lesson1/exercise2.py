
#
# parent_list = list(range(1, 1000, 2))
# num = len(parent_list)
# target_list = list(range(1, 501))
# i = 0
# summa_elements = 0
# while i <= (num-1):
#     target_list[i] = parent_list[i] ** 3
#     element = target_list[i]
#     summa = 0
#     while element > 0:
#         digit = element % 10
#         summa = summa + digit
#         element = element // 10
#     if (summa % 7) != 0:
#         summa_elements = summa_elements + summa
#     i = i + 1
# print(target_list)
# print(summa_elements)

target_list = []
summa_elements = 0
for i in range(1, 1000, 2):
    i = i ** 3 + 17
    target_list.append(i)

    element = i
    summa = 0
    while element != 0:

        digit = element % 10
        summa = summa + digit
        element = element // 10
    if summa % 7 == 0:
        summa_elements = summa_elements + i
print(summa_elements)
