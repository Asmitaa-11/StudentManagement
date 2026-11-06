students = []


# Function to add a student
def add_student():

    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Course: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)

    print("Student added successfully!")


# Function to display student details
def display_students():

    if not students:
        print("No students found.")

    else:
        for student in students:

            print("\nStudent Details")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])


# Function to search for a student
def search_student():

    student_id = input("Enter Student ID to search: ")

    for student in students:

        if student["id"] == student_id:

            print("Student Found!")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])

            return

    print("Student not found.")

