"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""
file = open('create_file\\text_5_2.txt', 'r')


s_lines = file.readlines()
f_name = file.name.split('\\')[-1]
print(f'В файле {f_name} содержиться {len(s_lines)} строк')
# print(f"В файле {file.name.split('\\')[-1]} содержиться {len(s_lines)} строк") # ????????


for i, line in enumerate(s_lines):
    textl = len(line.split())
    print(f'{textl} слов в {i+1} строке')


file.close()
