from random import randrange

translate_dictionary = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'}

number_en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
             'nine', 'ten']


def num_translate_adv(my_digit):
    if my_digit == 'y':
        random_idx = randrange(len(number_en))
        var_num_translate = translate_dictionary.get(number_en[random_idx])
    elif my_digit.istitle():
        my_digit_lower = my_digit.lower()
        var_num_translate = translate_dictionary.get(my_digit_lower).title()
    else:
        var_num_translate = translate_dictionary.get(my_digit)
    return var_num_translate


print(num_translate_adv(input('Введите числительное на английском от '
                              '1 до 10 или нажмите "y" и "Enter" для '
                              'автоматического выбора числа ')))
