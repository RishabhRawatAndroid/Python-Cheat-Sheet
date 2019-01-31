class Car:
    def __init__(self):  # constructor of car class
        _name = None  # private member
        model = None
        year = None

    @property  # getter
    def name(self):
        return self._name

    @name.setter  # setter same like a java
    def name(self, name):
        self._name = name

    @staticmethod  # static method in python
    def showcar():
        return 'Rishabh Car'


if __name__ == "__main__":
    car = Car()
    car.name = 'Toyota'
    print(Car.showcar())
    print(car.name)
