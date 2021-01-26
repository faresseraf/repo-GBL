"""5. Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""
import random
num_count = 0
while True:
    try:
        num_count = int(input("Введите сумму скольки чисел подсчитаем: "))
        break
    except:
        print("Введите целое число")
        continue

num_list = [random.randint(0, 99) for x in range(num_count)]

with open('create_file\\text_5_5.txt', 'w+') as file:
    file.write("Числа:" + '\n' + ' '.join(str(e) for e in num_list) + '\n' + "Их сумма = " + str(sum(num_list)))
    file.seek(0)
    print(file.read())

