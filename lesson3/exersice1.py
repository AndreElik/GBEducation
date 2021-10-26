def num_translate(s: object):
    nums = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    return nums.get(s)

    # try:
    #     out = nums[s]
    #     return out
    # except:
    #     raise ValueError('None')


print(num_translate('two'))
