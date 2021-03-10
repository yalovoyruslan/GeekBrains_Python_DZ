import requests
from datetime import date


def currency_rates(code):
    code = code.upper()
    foreign_currency = requests.get(
        'http://www.cbr.ru/scripts/XML_daily.asp').text.split('><')
    lst = []

    currency_day = int(foreign_currency[1][14:16])
    currency_month = int(foreign_currency[1][17:19])
    currency_year = int(foreign_currency[1][20:24])
    currency_date = date(currency_year, currency_month, currency_day)

    for i in foreign_currency:
        if i[:8] == 'CharCode':
            _i_ = i[9:12]
            lst.append(_i_)
        elif i[:7] == 'Nominal':
            _i_ = i[8:-9]
            lst.append(_i_)
        elif i[:5] == 'Value':
            _i_ = i[6:-7]
            _i_ = _i_.replace(',', '.')
            lst.append(_i_)
    for i in lst:
        if code == i:
            j = lst.index(code)
            return round(float(lst[j + 2]) / float(lst[j + 1]), 2), \
                   currency_date
        elif i == lst[-1]:
            return None, currency_date


if __name__ == '__main__':
    print(*currency_rates("USD"))
    print(*currency_rates("eur"))
    print(*currency_rates("www"))