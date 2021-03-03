from random import randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(x):
    lst = []
    for i in range(0, x):
        lst.append(f'{nouns[randrange(len(nouns))]} '
                   f'{adverbs[randrange(len(adverbs))]} '
                   f'{adjectives[randrange(len(adjectives))]}')
    return lst


n = input(f'Введите количество шуток:')
print(get_jokes(int(n)))
