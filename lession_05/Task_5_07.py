"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""
import json
data = []
averave_profit = 0
firm_count = 0
firm_dict = {}
with open("create_file\\text_5_7.txt", "r", encoding="utf-8") as file:
    with open("create_file\\text_5_7.json", "w") as firm_json:
        for line in file.readlines():
            tmp = line.split()

            try:
                receipts = int(tmp[-2])
                cost = int(tmp[-1])
            except ValueError:
                print("Value error - выручка, издержки")
                continue

            firm_dict[tmp[0]] = receipts - cost

            if receipts > cost:
                firm_count += 1
                averave_profit += receipts - cost
            else:
                continue

        data.append(firm_dict)

        try:
            averave_profit = averave_profit/firm_count
            data.append({"averave_profit": round(averave_profit)})
        except ZeroDivisionError:
            print("все фирмы в убытке")

        json.dump(data, firm_json)
