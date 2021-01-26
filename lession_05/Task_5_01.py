"""
1. Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

import sys

file = open('create_file\\text_5_1.txt', 'a+')

while True:
    text = input("введите текст ")
    if text != '':
        file.writelines(text + '\n')
    else:
        break

file.close()

if file.closed == True:
    sys.exit("the end")
