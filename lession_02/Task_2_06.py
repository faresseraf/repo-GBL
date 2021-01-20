# 6. * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

product_list = []
product_count = 1
while True:
    if "0" == input('Для выхода введите "0"'):
        break
    else:
        product_dict = {}
        product_dict['название'] = input('Введите название товара')
        product_dict['цена'] = int(input('Введите цену товара'))
        product_dict['количество'] = int(input('Введите количество товара'))
        product_dict['ед.изм'] = input('Введите ед.изм')
        temp = (product_count, product_dict)
        product_list.append(temp)
        product_count += 1

print(product_list)

# часть 2
product_descrip = ()
for i in range(len(product_list)):
    product_descrip += tuple(list(product_list[i])[1].keys())

product_descrip = set(product_descrip)
# print(product_descrip)
spec_product = list(product_descrip)
# print(spec_product)

spec_pr_end = {}
for i in range(len(spec_product)):
    spec_pr_temp = []

    for j in range(len(product_list)):
        spec_pr_temp.append(list(product_list[j])[1].get(spec_product[i]))

    spec_pr_temp = list(set(spec_pr_temp))
    spec_pr_end.update({spec_product[i]: spec_pr_temp})

print(spec_pr_end)
