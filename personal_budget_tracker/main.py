import os
from budget_utils import add_transaction, get_total_per_category, load_transactions

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def add_new_transaction():
    category = input("Enter category (e.g., food, rent, transport): ").capitalize()
    try:
        amount = float(input("Enter amount: ₦"))
        add_transaction(category, amount)
        print("Transaction added successfully!\n")
    except ValueError:
        print("Invalid amount. Try again.\n")

def view_all_transactions():
    transactions = load_transactions()
    if not transactions:
        print("No transactions recorded yet.\n")
        return
    print("\nAll Transactions:")
    for t in transactions:
        print(f"{t['date']} - {t['category']} - ₦{t['amount']}")

def view_summary():
    totals = get_total_per_category()
    if not totals:
        print("No data to summarize.\n")
        return
    print("\nTotal Spent by Category:")
    for cat, amt in totals.items():
        print(f"{cat}: ₦{amt:.2f}")

def main():
    while True:
        print("\n===== Personal Budget Tracker =====")
        print("1. Add Transaction")
        print("2. View All Transactions")
        print("3. View Category Summary")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        clear_screen()

        if choice == "1":
            add_new_transaction()
        elif choice == "2":
            view_all_transactions()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
