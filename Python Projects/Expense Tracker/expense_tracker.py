import csv
import datetime
import matplotlib.pyplot as plt

# --- Step 1: Initialize CSV with header if not exists ---
with open("expense.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Date", "Category", "Amount"])


# --- Step 2: Add Expense Function ---
def add_expense(date=None, category="General", amount=0):
    if date is None:
        date = datetime.date.today()
    with open("expense.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount])
    print("Expense Added!")


# --- Step 3: Show Summary Function ---
def show_summary():
    total = 0
    category_totals = {}
    max_expense = (0, "")

    with open("expense.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header

        for row in reader:
            if not row:  # skip empty rows
                continue
            date, category, amount = row
            amount = int(amount)

            total += amount
            category_totals[category] = category_totals.get(category, 0) + amount

            if amount > max_expense[0]:
                max_expense = (amount, category)

    print("\n--- Expense Summary ---")
    print(f"Total Spent: {total}")
    print("Per Category:")
    for cat, amt in category_totals.items():
        print(f"  {cat}: {amt}")
    print(f" Biggest Expense: {max_expense[1]} = {max_expense[0]}")


# --- Step 4: Show Chart Function ---
def show_chart():
    category_totals = {}

    with open("expense.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            if not row:
                continue
            _, category, amount = row
            amount = int(amount)
            category_totals[category] = category_totals.get(category, 0) + amount

    if not category_totals:
        print("No expenses to show chart!")
        return

    labels = category_totals.keys()
    sizes = category_totals.values()

    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("Expenses by Category")
    plt.show()


# --- Step 5: Menu System ---
def menu():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. Show Summary")
        print("3. Show Chart")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            category = input("Enter category: ")
            amount = int(input("Enter amount: "))
            add_expense(category=category, amount=amount)

        elif choice == "2":
            show_summary()

        elif choice == "3":
            show_chart()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


# --- Run the App ---
menu()
