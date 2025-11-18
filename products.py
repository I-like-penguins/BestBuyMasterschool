class Product:
    def __init__(self, name, price, quantity):
        if name == "":
            raise ValueError("Name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__active = True


    def get_quantity(self) -> int:
        return self.__quantity
    def set_quantity(self, quantity):
        self.__quantity = quantity
    def is_active(self) -> bool:
        return self.__active
    def activate(self):
        self.__active = True
    def deactivate(self):
        self.__active = False

    def __str__(self):
        return f"{self.__name}, Price: {self.__price}, Quantity: {self.__quantity}"

    def show(self):
        print(self)