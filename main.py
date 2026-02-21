import products
import store


def start(best_buy_store):
    while True:
        print("\n1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        print("-" * 25)

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            active_prods = best_buy_store.get_all_products()
            if not active_prods:
                print("No active products in store.")
            else:
                for i, prod in enumerate(active_prods, 1):
                    print(f"{i}. {prod.name} - Price: ${prod.price}, Quantity: {prod.get_quantity()}")

        elif choice == "2":
            total = best_buy_store.get_total_quantity()
            print(f"Total items in store: {total}")

        elif choice == "3":
            print("Make an order (select product index and quantity):")
            active_prods = best_buy_store.get_all_products()
            if not active_prods:
                print("No active products available.")
                continue

            shopping_list = []
            while True:
                for i, prod in enumerate(active_prods, 1):
                    print(f"{i}. {prod.name} - Price: ${prod.price}, Quantity: {prod.get_quantity()}")

                try:
                    idx_str = input("Which product # do you want? ").strip()
                    # if idx_str.lower() == 'done':
                    #     break
                    idx = int(idx_str) - 1
                    if 0 <= idx < len(active_prods):
                        qty = int(input("What amount do you want?"))
                        shopping_list.append((active_prods[idx], qty))
                    else:
                        print("Invalid index.")
                except ValueError:
                    print("Please enter a valid number.")

            if shopping_list:
                try:
                    total_price = best_buy_store.order(shopping_list)
                    print(f"Order total: ${total_price:.2f}")
                except Exception as e:
                    print(f"Order failed: {e}")

        elif choice == "4":
            print("Thanks for shopping!")
            break

        else:
            print("Invalid choice. Please enter 1-4.")


if __name__ == "__main__":
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = store.Store(product_list)

    start(best_buy)