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

