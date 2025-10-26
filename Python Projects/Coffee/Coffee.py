# Coffee class represents a coffee item with a name and price
class Coffee:
    def __init__(self, name, price):
        self.name = name      # Coffee name (e.g., "Latte")
        self.price = price    # Coffee price (e.g., 3.5)


# Order class manages the customer's order
class Order:
    def __init__(self):
        self.items = []  # List to store ordered coffee items

    def add_item(self, coffee):
        """Add a coffee item to the order."""
        self.items.append(coffee)
        print(f"Added {coffee.name} to your order.")

    def total(self):
        """Calculate the total price of the order."""
        return sum(item.price for item in self.items)

    def show_order(self):
        """Display all items in the order with the total."""
        if not self.items:
            print("No items in order.")
            return

        print("\nYour Order:")
        # Display each item with its name and price
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ${item.price:.2f}")

        # Show total cost of the order
        print(f"Total: ${self.total():.2f}\n")

    def checkout(self):
        """Finalize the order after confirmation from the user."""
        if not self.items:
            print("Your cart is empty.")
            return

        # Show current order before checkout
        self.show_order()

        # Ask user for confirmation
        confirm = input("Proceed to checkout? Yes/No: ").strip().lower()
        if confirm == "yes":
            print("Order confirmed! Thank you.")
            self.items.clear()  # Clear cart after checkout
        else:
            print("Checkout cancelled.")


# Main function controls the menu and ordering process
def main():
    # Define menu with Coffee objects
    menu = [
        Coffee("Espresso", 2.5),
        Coffee("Latte", 3.5),
        Coffee("Cappuccino", 3.0),
        Coffee("Americano", 2.0)
    ]

    order = Order()  # Create a new order

    while True:
        # Display menu options
        print("\n--- Coffee Menu ---")
        for i, coffee in enumerate(menu, 1):
            print(f"{i}. {coffee.name} - ${coffee.price:.2f}")

        # Additional options
        print("5. View Order")
        print("6. Checkout")
        print("7. Exit")

        # Take user input
        choice = input("Choose an option: ")

        # Process user choice
        if choice in ["1", "2", "3", "4"]:
            order.add_item(menu[int(choice) - 1])  # Add selected coffee
        elif choice == "5":
            order.show_order()  # View current order
        elif choice == "6":
            order.checkout()  # Go to checkout
        elif choice == "7":
            print("Thank you for visiting, goodbye!")
            break  # Exit the loop
        else:
            print("Invalid choice. Try again.")


# Run the program
if __name__ == "__main__":
    main()
