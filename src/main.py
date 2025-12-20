# src/main.py

from interfaces.item import Item
from storages.dict_storage import DictStorage
from utils import get_sheet


def load_students_from_sheet(storage: DictStorage):
    sheet = get_sheet("Students", "Sheet1")
    rows = sheet.get_all_records()

    for row in rows:
        grades = {
            "math": row["math"],
            "english": row["english"],
            "physics": row["physics"],
            "history": row["history"],
            "programming": row["programming"]
        }

        student = Item(
            student_id=str(row["student_id"]),
            name=row["name"],
            group=row["group"],
            grades=grades
        )

        storage.add(student)


def main():
    print("=== Student Search System ===")

    storage = DictStorage()
    load_students_from_sheet(storage)

    while True:
        print("\n==============================")
        print("🎓 Student Search System")
        print("==============================")
        print("1️⃣  Search student by ID")
        print("2️⃣  Search student by name")
        print("3️⃣  Show students by group")
        print("4️⃣  Show all students")
        print("0️⃣  Exit")

        choice = input("Your choice: ").strip()

        if choice == "1":
            student_id = input("Enter student ID: ")
            student = storage.search_by_id(student_id)

            if student:
                print(student)
                print("Grades:", student.grades)
            else:
                print("Student not found")

        elif choice == "2":
            name = input("Enter name: ")
            results = storage.search_by_name(name)

            if results:
                for s in results:
                    print(s)
            else:
                print("No students found")

        elif choice == "3":
            group = input("Enter group: ")
            results = storage.search_by_group(group)

            if results:
                for s in results:
                    print(s)
            else:
                print("No students in this group")

        elif choice == "4":
            for s in storage.get_all():
                print(s)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
