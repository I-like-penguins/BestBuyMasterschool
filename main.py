from products import Product
from store import Store


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    best_buy = Store([bose, mac])
    price = best_buy.order([(bose, 5), (mac, 30), (bose, 10)])
    print(f"Order cost: {price} dollars.")

    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    products = best_buy.get_active_products()
    print(f"Total Quantity:  {best_buy.get_total_quantity()}")
    print(f"Number of active products: {best_buy.get_number_of_active_products()}")
    print(f"Sum: {best_buy.order([(products[0], 1), (products[1], 2)])}")

if __name__ == "__main__":
    main()