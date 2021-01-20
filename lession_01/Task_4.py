#4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
num_user_str = input('Введите целое положительное число. ')
count_digit = len(num_user_str)
num_user = int(num_user_str)
max_digit = 0
while num_user > 0:
    temp_num = num_user//(10**(count_digit-1))
    if max_digit < temp_num:
        max_digit = temp_num
        if max_digit == 9: # самая больщая цифра это 9
            break
    num_user = num_user % (10**(count_digit-1))
    count_digit -= 1

print(f'самая большая цифра в введеном числе {num_user_str} равна {max_digit}')

#temp_num = num_user//10 тогда всё проше выглядит, а проверка идёт с конца числа
#и потом в 14 строке =>   num_user = num_user % 10  обрезка последней цифры