"""4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""
class Car:
    def __init__(self, speed=0, color='rainbow', name='Auto', is_polise=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_polise

    def go(self):
        print(f"{self.name} GO !")
    def stop(self):
        print(f"{self.name} Stop 1 2.")
    def turn(self, direction='d'):
        if direction == "d":
            print(f"{self.name} direct")
        elif direction == "l":
            print(f"{self.name} left turn")
        elif direction == "r":
            print(f"{self.name} right turn")
        else:
            print(f"{self.name}course not changed")
    def show_speed(self):
        print(f'{self.name}: current car speed = {self.speed} km/h')


class Towncar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name}: slow down to 60')
        else:
            print(f'{self.name}: current car speed = {self.speed} km/h')


class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name}: slow down to 40')
        else:
            print(f'{self.name}: current car speed = {self.speed} km/h')

class PoliceCar(Car):
    pass

towncar1 = Towncar(speed=20, color='orange', name='towncar1')
sportcar1 = SportCar(speed=75, color='green', name='sportcar1')
workcar1 = WorkCar(speed=30, color='brown', name='workcar1')
policecar1 = PoliceCar(is_polise=True, speed=55, color='black', name='policecar1')

print(towncar1.speed, sportcar1.speed, workcar1.speed, policecar1.speed, sep='\t\t')
print(towncar1.color, sportcar1.color, workcar1.color, policecar1.color, sep='\t')
print(towncar1.name, sportcar1.name, workcar1.name, policecar1.name)
print(towncar1.is_police, sportcar1.is_police, workcar1.is_police, policecar1.is_police, sep='\t')

towncar1.go()
towncar1.show_speed()
towncar1.speed += 100
towncar1.show_speed()
towncar1.turn('l')
towncar1.turn('r')
towncar1.turn('d')
towncar1.stop()

sportcar1.stop()
workcar1.show_speed()
workcar1.turn('l')
policecar1.show_speed()
policecar1.turn('d')
policecar1.stop()