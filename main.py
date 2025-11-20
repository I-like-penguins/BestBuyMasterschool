import store
from products import Product
from store import Store

def start(store_obj: Store):
    is_not_quit = True
    while is_not_quit:
        print("Welcome to the Best Buy Store")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an Order")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("View Products:")
            i = 1
            for product in store_obj.get_active_products():
                print(f"{i}. {product}")
                i += 1
            print(f"")
        if choice == "2":
            print("View Total Amount")
            print(f"Total of {store_obj.get_total_quantity()} items in store.")
            print(f"")
        if choice == "3":
            print("Make an Order")
            i = 1
            for product in store_obj.get_active_products():
                print(f"{i}. {product}")
                i += 1
            print(f"When you want to finish order, enter empty text.")
            shopping_list = []
            while True:
                product_number = input("Which product # do you want? ")
                if product_number == "":
                    break
                if not product_number.isdigit():
                    print("Invalid product number!")
                    continue
                if int(product_number) > len(store_obj.get_active_products()):
                    print("Invalid product number!")
                    continue
                try:
                    quantity = int(input("What amount do you want? "))
                except ValueError:
                    print("Invalid quantity!")
                    continue
                try:
                    tmp_product = store_obj.get_active_products()[int(product_number)-1]
                    if tmp_product.get_quantity() > quantity:
                        shopping_list.append((tmp_product, quantity))
                        print(f"Product added to list!")
                    else:
                        print(f"Product is out of stock!")
                except IndexError:
                    print("Invalid product number!")
            print(f"Order made! Total payment: {store_obj.order(shopping_list)}")
            print(f"")
        if choice == "4":
            is_not_quit = False
            print("Thank you for shopping with us!")
    return

def main():
    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = Store(product_list)
    start(best_buy)

if __name__ == "__main__":
    main()