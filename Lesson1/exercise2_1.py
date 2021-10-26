parent_list = list(range(1, 1000, 2))
num = len(parent_list)
target_list = list(range(1, 501))
i = 0
summa_elements = 0
while i <= (num-1):
    target_list[i] = parent_list[i] ** 3 * 100 + 17
    element = target_list[i]
    summa = 0
    while element > 0:
        digit = element % 10
        summa = summa + digit
        element = element // 10
    if (summa % 7) != 0:
        summa_elements = summa_elements + summa
        print(summa, target_list[i])
        print(summa_elements)
    i = i + 1
print(summa_elements)
print(target_list)
