

def thesaurus_adv(*args):
    names = {}

    for element in args:
        key = element[0]
        names.update({key: []})
    print(names)
    for i in names.keys():
        meaning = []
        for element in args:
            if i == element[0]:
                meaning.append(element)
        names.update({i: meaning})
    print(names)


thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

