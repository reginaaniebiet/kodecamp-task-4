import json
import os

DATA_FILE = "students.json"

def save_students(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def load_students():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def calculate_average(scores):
    return sum(scores.values()) / len(scores)

def calculate_grade(avg):
    if avg >= 70:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 45:
        return "D"
    elif avg >= 40:
        return "E"
    else:
        return "F"
