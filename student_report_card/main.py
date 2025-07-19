import os
from student_utils import save_students, load_students, calculate_average, calculate_grade

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_student(students):
    name = input("Enter student name: ")
    subjects = {}
    subject_count = int(input("How many subjects? "))
    for _ in range(subject_count):
        subject = input("Enter subject name: ")
        score = float(input(f"Enter score for {subject}: "))
        subjects[subject] = score

    average = calculate_average(subjects)
    grade = calculate_grade(average)

    student = {
        "name": name,
        "subjects": subjects,
        "average": average,
        "grade": grade
    }

    students.append(student)
    save_students(students)
    print("Student added successfully.\n")

def view_students(students):
    if not students:
        print("No students available.\n")
        return
    for idx, student in enumerate(students, 1):
        print(f"\nStudent {idx}: {student['name']}")
        for subject, score in student['subjects'].items():
            print(f"  {subject}: {score}")
        print(f"Average: {student['average']:.2f}")
        print(f"Grade: {student['grade']}")

def update_student(students):
    name = input("Enter the student name to update: ")
    for student in students:
        if student['name'].lower() == name.lower():
            print(f"Updating record for {student['name']}")
            for subject in student['subjects']:
                score = float(input(f"Enter new score for {subject}: "))
                student['subjects'][subject] = score
            student['average'] = calculate_average(student['subjects'])
            student['grade'] = calculate_grade(student['average'])
            save_students(students)
            print("Record updated.\n")
            return
    print("Student not found.\n")

def main():
    students = load_students()

    while True:
        print("====== Student Report Card App ======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student Scores")
        print("4. Exit")
        choice = input("Enter choice (1-4): ")

        clear_screen()

        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            update_student(students)
        elif choice == '4':
            print("Exiting app. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
