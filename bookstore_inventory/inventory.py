import json
import os
import math

DATA_FILE = "books.json"

class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = math.ceil(price)  # Round up
        self.stock = stock

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "price": self.price,
            "stock": self.stock
        }

def load_books():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def save_books(books):
    with open(DATA_FILE, 'w') as file:
        json.dump(books, file, indent=4)

def add_book(title, author, price, stock):
    books = load_books()
    new_book = Book(title, author, price, stock)
    books.append(new_book.to_dict())
    save_books(books)
    print("Book added successfully!")

def view_books():
    books = load_books()
    if not books:
        print("No books in inventory.")
    else:
        for idx, book in enumerate(books, 1):
            print(f"\nBook {idx}")
            print(f"Title : {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Price : ₦{book['price']}")
            print(f"Stock : {book['stock']}")

def update_stock(title, quantity):
    books = load_books()
    for book in books:
        if book["title"].lower() == title.lower():
            book["stock"] += quantity
            save_books(books)
            print("Stock updated!")
            return
    print("Book not found.")
