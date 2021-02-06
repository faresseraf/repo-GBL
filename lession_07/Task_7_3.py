'''3.
Деление.
оздается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.С
В классе необходимо реализовать метод make_order(),
принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****...,
где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.'''
class Cell:
    def __init__(self, counts):
        self._counts = counts

    def __str__(self):
        return str(self._counts)

    def __add__(self, other):
        self._counts += int(str(other))
        return self

    def __sub__(self, other):
        spam = self._counts - int(str(other))
        if spam > 0:
            self._counts = spam
            return self._counts
        else:
            print('исходных клеток мало')

    def __mul__(self, other):
        self._counts *= int(str(other))
        return self._counts

    def __truediv__(self, other):
        self._counts = round(self._counts / int(str(other)))
        return self._counts

    def make_order(self, other):
        cage = 0
        for i in range(self._counts):
            print('*', end='')
            cage += 1
            if (cage % other) == 0:
                print('\\n', end='')


cell1 = Cell(15)
cell2 = Cell(10)
print(cell1 + cell2, '\tcell1 + cell2')
print(cell1 - cell2, '\tcell1 - cell2')
print(cell1 * cell2, 'cell1 * cell2')
print(cell1 / cell2, '\tcell1 / cell2')
cell1.make_order(4)