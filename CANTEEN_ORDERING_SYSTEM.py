def display_welcome_message():
    print("Welcome to the Canteen Management System!")

def display_canteen_menu():
    print("\n--- MAIN MENU ---")
    print("1. Add Item")
    print("2. Show Current Order")
    print("3. Show Summary Order")
    print("4. Display All Submitted Orders")
    print("5. Remove Item from Order")
    print("6. Clear Order")
    print("7. Submit Order")
    print("0. Exit")

def show_menu(menu):
    print("\n--- CANTEEN MENU ---")
    for key, item in menu.items():
        print(f"{key}. {item['name']} - ₱{item['price']}")

def add_multiple_items(menu, order):
    show_menu(menu)
    print("\nEnter your order in the format item_number:quantity separated by commas.")
    print("Example: 1:2,3:1 (means 2 Burgers, 1 Pizza)")
    user_input = input("Your order: ").strip()
    if not user_input:
        print("No input received.")
        return
    
    entries = user_input.split(',')
    for entry in entries:
        try:
            item_num, qty = entry.split(':')
            if item_num in menu:
                qty = int(qty)
                if qty > 0:
                    order[item_num] = order.get(item_num, 0) + qty
                else:
                    print(f"Quantity for item {item_num} must be positive. Skipped.")
            else:
                print(f"Item number {item_num} is not in the menu. Skipped.")
        except ValueError:
            print(f"Invalid format '{entry}', please use item_number:quantity. Skipped.")

    print("Items added and order updated.")

def show_current_order(order, menu):
    if not order:
        print("\nNo current order.")
        return
    print("\n--- CURRENT ORDER ---")
    total = 0
    for item_num, qty in order.items():
        price = menu[item_num]['price'] * qty
        total += price
        print(f"{item_num}. {menu[item_num]['name']} x {qty} = ₱{price}")
    print(f"Total Price: ₱{total}")

def show_summary_order(order, menu):
    if not order:
        print("\nNo current order to summarize.")
        return
    print("\n--- ORDER SUMMARY ---")
    total = 0
    for item_num, qty in order.items():
        price = menu[item_num]['price'] * qty
        total += price
        print(f"{menu[item_num]['name']}: {qty} pcs - ₱{price}")
    print(f"Total Price: ₱{total}")

def display_current_orders(all_orders, menu):
    if not all_orders:
        print("\nNo orders currently placed.")
        return
    print("\n--- ALL SUBMITTED ORDERS ---")
    for idx, order in enumerate(all_orders, start=1):
        print(f"\nOrder {idx}:")
        total = 0
        for item_num, qty in order.items():
            price = menu[item_num]['price'] * qty
            total += price
            print(f"  {menu[item_num]['name']} x {qty} = ₱{price}")
        print(f"  Total: ₱{total}")

def remove_item_from_order(order, menu):
    if not order:
        print("\nNo current order to remove items from.")
        return
    show_current_order(order, menu)
    try:
        item_num = input("Enter the item number to remove (or 'cancel' to abort): ").strip()
        if item_num.lower() == 'cancel':
            print("Remove item cancelled.")
            return
        if item_num in order:
            del order[item_num]
            print(f"Item '{menu[item_num]['name']}' removed from order.")
        else:
            print("Invalid item number.")
    except Exception as e:
        print("Error:", e)

def clear_order(order):
    if not order:
        print("\nNo current order to clear.")
        return
    confirmation = input("Are you sure you want to clear the order? (Y/N): ")
    if confirmation.lower() == 'y':
        order.clear()
        print("Order cleared.")
    else:
        print("Clear order aborted.")

def submit_order(order, all_orders):
    if not order:
        print("\nNo current order to submit.")
        return
    confirmation = input("Confirm order submission? (Y/N): ")
    if confirmation.lower() == 'y':
        all_orders.append(order.copy())
        print("Order submitted.")
        order.clear()
    else:
        print("Order submission cancelled.")

def main():
    menu = {
        "1": {"name": "Burger", "price": 50},
        "2": {"name": "Soda", "price": 20},
        "3": {"name": "Pizza", "price": 100},
        "4": {"name": "Fries", "price": 30}
    }

    display_welcome_message()
    order = {}
    all_orders = []

    while True:
        display_canteen_menu()
        option = input("Enter an option: ").strip()

        if option == '0':
            print("Exiting system...")
            break

        elif option == '1':
            add_multiple_items(menu, order)

        elif option == '2':
            show_current_order(order, menu)

        elif option == '3':
            show_summary_order(order, menu)

        elif option == '4':
            display_current_orders(all_orders, menu)

        elif option == '5':
            remove_item_from_order(order, menu)

        elif option == '6':
            clear_order(order)

        elif option == '7':
            submit_order(order, all_orders)

        else:
            print("Invalid input option. Please try again.")

if __name__ == "__main__":
    main()
    