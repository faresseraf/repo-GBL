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
    num_user = num_user % (10**(count_digit-1))
    count_digit -= 1

print(f'самая большая цифра в введеном числе {num_user_str} равна {max_digit}')