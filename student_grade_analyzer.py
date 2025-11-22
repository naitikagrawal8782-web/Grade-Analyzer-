# Student Grade Analyzer Project
students = []
def add_student():
    name = input("Enter student name: ")
    m1 = float(input("Enter marks for Subject 1: "))
    m2 = float(input("Enter marks for Subject 2: "))
    m3 = float(input("Enter marks for Subject 3: "))

    avg = (m1 + m2 + m3) / 3

    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    else:
        grade = "D"

    students.append({
        "name": name,
        "marks": [m1, m2, m3],
        "average": avg,
        "grade": grade
    })

    print("Student added successfully!\n")

def view_all():
    if len(students) == 0:
        print("No student records available.\n")
        return

    print("\n--- Student Records ---")
    for s in students:
        print(f"Name: {s['name']} | Avg: {s['average']} | Grade: {s['grade']}")
    print()

def top_student():
    if len(students) == 0:
        print("No students to analyze.\n")
        return

    top = max(students, key=lambda x: x["average"])
    print("\n--- Top Student ---")
    print(f"Name: {top['name']}")
    print(f"Average: {top['average']}")
    print(f"Grade: {top['grade']}\n")

def menu():
    while True:
        print("===== Student Grade Analyzer =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Show Top Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all()
        elif choice == "3":
            top_student()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.\n")

menu()
