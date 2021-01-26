"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

file = open('create_file\\text_5_4.txt', 'r')
file_str = file.readlines()

for i in file_str:
    temp = i.split()
    if temp[0] == "One":
        temp[0] = "Один"
    elif temp[0] == "Two":
        temp[0] = "Два"
    elif temp[0] == "Three":
        temp[0] = "Три"
    elif temp[0] == "Four":
        temp[0] = "Четыре"
    else:
        continue
    with open('create_file\\text_5_4_change.txt', 'a') as changed:
        changed.write(' '.join(temp) + '\n')


file.close()



