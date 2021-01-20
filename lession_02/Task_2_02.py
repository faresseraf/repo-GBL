# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
try:
    count_elements_list = int(input("Введите кол-во элементов в списке: "))
except:
    print("введено не число")

my_list =[]
for i in range(count_elements_list):
    my_list.append(input("Введите элемент списка: "))

print(my_list, ' list')

j = 0
while j < count_elements_list:
    if (j + 2) > count_elements_list:
        break
    else:
        my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
        j += 2

print(my_list, ' change list')