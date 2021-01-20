# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
my_list = []
my_list.append(None)
my_list.append(-50)
my_list.append(23.45)
my_list.append("Some text")
my_list.append(["list", None, 4])
my_list.append({"dict": 14, "bool": True, "int": 5, "float" : 3.14 })
my_list.append(("tup", None, 6, 14.7))
my_list.append({"set", None, 7, 7, 7, 7})

print(my_list)
for i in my_list:
    print(type(i))
