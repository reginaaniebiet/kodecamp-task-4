import os
from inventory import add_book, view_books, update_stock

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    while True:
        print("\n===== Bookstore Inventory System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book Stock")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        clear_screen()

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            price = float(input("Enter price: ₦"))
            stock = int(input("Enter stock quantity: "))
            add_book(title, author, price, stock)
        elif choice == "2":
            view_books()
        elif choice == "3":
            title = input("Enter book title to update stock: ")
            quantity = int(input("Enter quantity to add/remove (use negative for reduce): "))
            update_stock(title, quantity)
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-4.")

if __name__ == "__main__":
    main()
