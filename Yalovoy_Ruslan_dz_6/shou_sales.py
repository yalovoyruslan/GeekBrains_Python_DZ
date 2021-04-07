import sys


def show_function(sales):
    with open('bakery.csv', 'r', encoding='utf-8') as show_f:
        _i = show_f.readlines()
        _i = _i[int(sales):]
        for i in _i:
            print(i.strip())


if __name__ == '__main__':
    a = sys.argv
    if len(a) == 1:
        arg = 1
    else:
        arg = a[1]
    show_function(arg)
