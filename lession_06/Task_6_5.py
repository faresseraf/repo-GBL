"""5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра."""
class Stationery:
    def __init__(self, s_title=None):
        self.title = s_title
        self.draw()
    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationery):
    def draw(self):
        print('ручка')
class Pencil(Stationery):
    def draw(self):
        print('карандаш')
class Handle(Stationery):
    def draw(self):
        print('маркер')


pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()