time = int(input('Введите количество секунд '))

day = time // 86400
haur = time % 86400 // 3600
minute = time % 3600 // 60
sek = time % 60

if day == 0 and haur == 0 and minute == 0:
    print(f'Это {sek} секунд')
elif day == 0 and haur == 0:
    print(f'Это {minute} минут, {sek} секунд')
elif day == 0:
    print(f'Это {haur} часов, {minute} минут, {sek} секунд')
else:
    print(f'Это {day} дней, {haur} часов, {minute} минут, {sek} секунд')



