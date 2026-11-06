import student

print("Welcome to Student Management System")

while True:

    print("\n===== Student Management System =====")

    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        student.add_student()

    elif choice == "2":

        student.display_students()

    elif choice == "3":

        student.search_student()

    elif choice == "4":

        student.delete_student()

    elif choice == "5":

        student.update_student()

    elif choice == "6":

        print("Exiting Program...")
        break

    else:

        print("Invalid choice!")

