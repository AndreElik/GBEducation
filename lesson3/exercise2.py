def num_translate_adv(s):
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
    if s == s.lower():
        return nums.get(s)
    else:
        s = s.lower()
        return nums[s].capitalize()

    # try:
    #     out = nums[s]
    #     return out
    # except:
    #     raise ValueError('None')


print(num_translate_adv('Two'))