import json
import os
from datetime import datetime

DATA_FILE = "transactions.json"

class Transaction:
    def __init__(self, date, category, amount):
        self.date = date
        self.category = category
        self.amount = amount

    def to_dict(self):
        return {
            "date": self.date,
            "category": self.category,
            "amount": self.amount
        }

def load_transactions():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def save_transactions(transactions):
    with open(DATA_FILE, 'w') as file:
        json.dump(transactions, file, indent=4)

def add_transaction(category, amount):
    transactions = load_transactions()
    date = datetime.now().strftime("%Y-%m-%d")
    new = Transaction(date, category, amount)
    transactions.append(new.to_dict())
    save_transactions(transactions)

def get_total_per_category():
    transactions = load_transactions()
    totals = {}
    for trans in transactions:
        category = trans["category"]
        amount = trans["amount"]
        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount
    return totals
