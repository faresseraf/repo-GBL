"""3. Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров)."""
class Worker:
    'строка с описанием класса Worker'
    def __init__(self, name=None, surname=None, position=None, wage=None, bonus=None):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {"wage": wage, "bonus": self.bonus}


class Position(Worker):
    def get_full_name(self):
        return print(getattr(self, "name"), getattr(self, "surname"))
    def get_total_income(self):
        return print(sum(getattr(self, '_income').values()))


worker1 = Position('Bob', 'Oak', 'cowboy', 5000, 1000)
worker1.get_full_name()
worker1.get_total_income()