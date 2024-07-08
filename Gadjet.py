class Gadjet:
    def __init__(self, brand, color, gb, year):
        super().__init__(brand, year, gb, color)
        self.__brand = brand
        self.__color = color
        self.__gb = gb
        self.__year = year

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def get_gb(self):
        return self.__gb

    def set_gb(self, gb):
        self.__gb = gb

    def get_info(self):
        print(f"height: {self.get_brand()}\n"
              f"width: {self.get_color()}\n"
              f"square: {self.get_gb()}\n"
              f"floor: {self.get_year()}")



class Laptop(Gadjet):
    def __init__(self, brand, color, gb, year):
        super().__init__(brand, year, gb, color)
        self.__brand = brand
        self.__color = color
        self.__gb = gb
        self.__year = year

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def get_gb(self):
        return self.__gb

    def set_gb(self, gb):
        self.__gb = gb

    def get_info(self):
        print(f"height: {self.get_brand()}\n"
              f"width: {self.get_color()}\n"
              f"square: {self.get_gb()}\n"
              f"floor: {self.get_year()}")

class Mapcase(Gadjet):
    def __init__(self, brand, color, gb, year):
        super().__init__(brand, year, gb, color)
        self.__brand = brand
        self.__color = color
        self.__gb = gb
        self.__year = year

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def get_gb(self):
        return self.__gb

    def set_gb(self, gb):
        self.__gb = gb

    def get_info(self):
        print(f"height: {self.get_brand()}\n"
              f"width: {self.get_color()}\n"
              f"square: {self.get_gb()}\n"
              f"floor: {self.get_year()}")