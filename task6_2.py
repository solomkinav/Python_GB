# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self, thickness):
        """Возвращает массу асфальта в тоннах, при массе 1кв. м толщиной 1см - 25 кг"""
        return self._length * self._width * 25 * thickness / 1000


# проверка работы
rd1 = Road(5000, 20)
rd2 = Road(500, 20)
rd3 = Road(100, 20)
print(rd1.weight(5))
print(rd2.weight(5))
print(rd3.weight(5))