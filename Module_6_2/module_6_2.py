class Vehicle:
    owner = str()
    __model = str()
    __engine_power = int()
    __color = str()
    __COLOR_VARIANTS = ('GREEN', 'RED', 'WHITE', 'BLACK', 'BLUE')
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self, __model):
        return print(f'Модель: {self.__model}')

    def get_horsepower(self, engine_power):
        return print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self, color):
        return print(f'Цвет: {self.__color}')

    def print_info(self):
        self.get_model(self.__model)
        self.get_horsepower(self.__engine_power)
        self.get_color(self.__color)
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    pass


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()