# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
# 1
s_winter = ["зима", 12, 1, 2]
s_spring = ["весна", 3, 4, 5]
s_summer = ["лето", 6, 7, 8]
s_autum = ["осень", 9, 10, 11]
s_t = "В этом месяце время года "
while True:
    try:
        mounth = int(input("Введите номер месяца: "))
        if mounth in s_winter:
            print(s_t, s_winter[0])
        elif mounth in s_spring:
            print(s_t, s_spring[0])
        elif mounth in s_summer:
            print(s_t, s_summer[0])
        elif mounth in s_autum:
            print(s_t, s_autum[0])
        else:
            print("Такого месяца нет")
            break
    except:
        print("введено не число")
        break

# 2
# seasson = {12: 'Зима', 1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна',
# 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень'}