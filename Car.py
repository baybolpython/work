class Car:

    def __init__(self, brand, color, max_speed, year):
        super().__init__(brand, color, max_speed, year)
        self.__brand = brand
        self.__color = color
        self.__max_speed = max_speed
        self.__year = year

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color
    def get_max_speed(self):
        return self.__max_speed

    def set_max_speed(self, max_speed):
        self.__max_speed = max_speed

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year


    def get_info(self):
        print(f"height: {self.get_brand()}\n"
              f"width: {self.get_color()}\n"
              f"square: {self.get_max_speed()}\n"
              f"floor: {self.get_year()}")
