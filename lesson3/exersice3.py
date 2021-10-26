# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"],
#     "П": ["Петр"]
# }

def thesaurus(*args):
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






















thesaurus("Иван", "Мария", "Петр", "Илья")