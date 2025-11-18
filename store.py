import products as pd

class Store:
    def __init__(self, products = []):
        """Initalize the store with products or an empty list of product-objects"""
        if products is None or len(products) == 0:
            self.__products = []
            return
        for product in products:
            if not isinstance(product, pd.Product):
                raise TypeError("All products must be of type Product")
        self.__products = products

    def add_product(self, product):
        """Add a product-object to the store, raise an error if the product is not of type Product"""
        if not isinstance(product, pd.Product):
            raise TypeError("Product must be of type Product")
        self.__products.append(product)

    def remove_product(self, product):
        """Remove a product-object from the store, raise an error if the product is not of type Product"""
        if not isinstance(product, pd.Product):
            raise TypeError("Product must be of type Product")
        self.__products.remove(product)

    def get_products(self):
        """Return a list of every product-object, active or not"""
        return self.__products

    def get_active_products(self) -> list[pd.Product]:
        """Return a list of every product-object that is active"""
        active_products = []
        for product in self.__products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def get_total_quantity(self) -> int:
        """Return the total quantity of all products"""
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_number_of_active_products(self) -> int:
        """Return the number of active products"""
        return len(self.get_active_products())

    def order(self, shopping_list) -> float:
        """Return the total price of the shopping list, raise an error if the shopping list is not a list of Product-objects
        shopping_list consists of Tuples of (Product-object, quantity)"""
        total_price = 0.0
        for product, quantity in shopping_list:
           if not isinstance(product, pd.Product):
               raise TypeError("All products must be of type Product")
           if not isinstance(quantity, int):
               raise TypeError("Quantity must be of type int")
           if not product.is_active():
               raise ValueError("Product is not active")
           if quantity <= 0:
               raise ValueError("Quantity cannot be less or equal to zero")
           total_price += product.buy(quantity)
        return total_price