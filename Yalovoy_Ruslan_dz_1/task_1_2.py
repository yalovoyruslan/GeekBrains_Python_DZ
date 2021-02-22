lists_cube = [i**3 for i in range(1, 1001, 2)]
print(lists_cube)

final_amount = 0
final_amount_17 = 0

for number_list in lists_cube:
    sum_last_digit = 0
    sum_last_digit_17 = 0
    var_number_list = number_list
    var_number_list_17 = number_list + 17
    while var_number_list > 0 and var_number_list_17 > 0:
        sum_last_digit += var_number_list % 10
        var_number_list = var_number_list // 10
        sum_last_digit_17 += var_number_list_17 % 10
        var_number_list_17 = var_number_list_17 // 10
    if sum_last_digit % 7 == 0:
        final_amount += number_list
    elif sum_last_digit_17 % 7 == 0:
        final_amount_17 += number_list + 17

print(f'Сумма всех чесел, сумма цифр которых кратна 7: {final_amount}' )
print(f'Сумма всех чесел списка, увеличенных на 17 и, сумма цифр которых кратна 7: {final_amount_17}' )
