percent = int(input('Введите количество процентов от 0 до 20 '))

if percent > 4 and percent < 21 or percent == 0:
    print(f'Вы ввели {percent} процентов')
elif percent == 1:
    print(f'Вы ввели {percent} процент')
elif percent > 1 and percent < 5:
    print(f'Вы ввели {percent} процента')
else:
    print(f'Вы ввели число не входящиее в диапазон от 0 до 20')

for percent in range(0, 21):
    if percent > 4 and percent < 21 or percent == 0:
        print(f'В этой программе можно ввести {percent} процентов')
    elif percent == 1:
        print(f'В этой программе можно ввести {percent} процент')
    elif percent > 1 and percent < 5:
        print(f'В этой программе можно ввести {percent} процента')
