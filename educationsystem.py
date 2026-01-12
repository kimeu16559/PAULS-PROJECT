

class Person:
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name

    def display(self):
        pass  # Polymorphism


class Student(Person):
    def __init__(self, person_id, name, course):
        super().__init__(person_id, name)
        self.course = course

    def display(self):
        print(f"ID: {self.person_id} | Name: {self.name} | Course: {self.course}")


class Course:
    def __init__(self, course_id, name, fee, discount=0):
        self.course_id = course_id
        self.name = name
        self.fee = fee
        self.discount = discount

    def final_fee(self):
        return self.fee - (self.fee * self.discount / 100)


students = []
courses = [
    Course(1, "Python Programming", 15000, 10),
    Course(2, "Data Science", 20000, 5),
    Course(3, "Web Development", 18000, 0),
    Course(4, "Cyber Security", 22000, 15)
]


def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course Name: ")
    students.append(Student(sid, name, course))
    print("Student added successfully.")


def view_students():
    if not students:
        print("No students found.")
    for s in students:
        s.display()


def search_student():
    sid = input("Enter Student ID to search: ")
    for s in students:
        if s.person_id == sid:
            s.display()
            return
    print("Student not found.")


def update_student():
    sid = input("Enter Student ID to update: ")
    for s in students:
        if s.person_id == sid:
            s.name = input("Enter new name: ")
            s.course = input("Enter new course: ")
            print("Student updated successfully.")
            return
    print("Student not found.")


def display_courses():
    print("\nAvailable Courses")
    for c in courses:
        print(f"{c.course_id}. {c.name} - KES {c.fee} (Discount {c.discount}%)")


def payment(amount):
    print("\nPayment Method")
    print("1. Mpesa")
    print("2. Debit/Credit Card")
    choice = input("Choose payment method: ")
    if choice in ["1", "2"]:
        print(f"Payment of KES {amount} successful.")
    else:
        print("Invalid payment method.")


def course_registration():
    display_courses()
    cid = int(input("Select course ID: "))
    for c in courses:
        if c.course_id == cid:
            final_amount = c.final_fee()
            print(f"\nCourse Selected: {c.name}")
            print(f"Discount: {c.discount}%")
            print(f"Total Payable: KES {final_amount}")
            payment(final_amount)
            return
    print("Invalid course selection.")


def menu():
    while True:
        print("\n--- EDUCATION MANAGEMENT SYSTEM ---")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student Record")
        print("5. Register for Course & Pay")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            course_registration()
        elif choice == "6":
            print("Exiting system...")
            break
        else:
            print("Invalid choice.")


menu()