"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""
file = open('create_file\\text_5_3.txt', 'r')
s_file = file.readlines()
average, employee_count = 0, 0
print("Список сотрудников с окладом меньше 20 тыс.: ")
for i, empl_sal in enumerate(s_file):
    emp_list = empl_sal.split('\t')
    try:
        sur_sal = int(emp_list[-1])
        average += sur_sal
        employee_count += 1
    except:
        continue

    if sur_sal < 20:
        print(emp_list[0])

print(f'средняя величина дохода сотрудников = {average / employee_count:.1f} тыс.')

file.close()