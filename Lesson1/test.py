
summa_elements = 0
i, j = 27, 27
summa = 0
while j != 0:

    digit = j % 10
    summa = summa + digit
    j = j // 10
if summa % 7 == 0:
    summa_elements = summa_elements + i
print(summa_elements)


