# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(x, y, z):
    if x + y > y + z:
        return x + y
    elif x + z >= y + z:
        return x + z
    else:
        return y + z

print(my_func(1, 1, 1) == 2)
print(my_func(0, 1, 2) == 3)
print(my_func(1, 1, 2) == 3)
print(my_func(1, 2, 2) == 4)
print(my_func(2, 1, 2) == 4)
print(my_func(9, 2, 1) == 11)
print(my_func(2, 9, 1) == 11)