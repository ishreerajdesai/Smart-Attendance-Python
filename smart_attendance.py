
students = []
attendance_records = []

while True:
    print("\n===== SMART ATTENDANCE SYSTEM =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Students")
    print("4. View Attendance Report")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")

        found = False

        for student in students:
            if student["id"] == student_id:
                found = True

        if found:
            print("Student ID already exists!")
        else:
            students.append({
                "id": student_id,
                "name": name
            })
            print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students registered!")
        else:
            date = input("Enter Date (DD-MM-YYYY): ")
            status = {}

            for student in students:
                print("\nStudent:", student["name"])
                attendance = input("Present or Absent (P/A): ").upper()

                while attendance not in ["P", "A"]:
                    attendance = input("Enter P or A: ").upper()

                status[student["id"]] = attendance

            attendance_records.append({
                "date": date,
                "status": status
            })
            print("Attendance marked successfully!")

    elif choice == "3":
        print("\n===== STUDENT LIST =====")

        for student in students:
            print("ID:", student["id"],
                  "| Name:", student["name"])

    elif choice == "4":
        print("\n===== ATTENDANCE REPORT =====")

        for student in students:
            present = 0
            total = 0

            for record in attendance_records:
                if student["id"] in record["status"]:
                    total += 1

                    if record["status"][student["id"]] == "P":
                        present += 1

            percentage = (present / total * 100) if total > 0 else 0

            print("\nName:", student["name"])
            print("Present:", present)
            print("Total Classes:", total)
            print("Attendance:", round(percentage, 2), "%")

    elif choice == "5":
        print("Thank you for using Smart Attendance System!")
        break

    else:
        print("Invalid choice! Try again.")
