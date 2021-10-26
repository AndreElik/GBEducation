

for num in range(1, 101):
    if num % 10 == 1:
        word_percent = ' процент'
    elif num % 10 > 4 or num % 10 == 0:
        word_percent = ' процентов'
    else:
        word_percent = ' процента'
    if num >= 10:
        if num < 20:
            word_percent = ' процентов'
    print(num, word_percent)
