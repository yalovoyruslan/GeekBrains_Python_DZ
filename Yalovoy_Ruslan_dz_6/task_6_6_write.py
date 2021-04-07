

def add_function(sales):
    with open('bakery.csv', 'a', encoding='utf-8') as add_f:
        sales = sales.replace(',', '.')
        sales = float(sales)
        # print(type(sales))
        if type(sales) == float:
            sales = str(sales)
            print(sales)
            add_f.writelines(sales + '\n')
        else:
            print('Введенные данные не являются числом')


if __name__ == '__main__':
    add_function(sales='3,2')
