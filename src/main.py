from storages.bst_storage import BSTStorage
from analytics import StudentAnalytics
from utils import get_sheet
from interfaces.item import Item

def load_data(storage):
    sheet = get_sheet("Students", "Sheet1")
    for row in sheet.get_all_records():
        grades = {k: row[k] for k in ["math", "english", "physics", "history", "programming"]}
        storage.add(Item(str(row["student_id"]), row["name"], row["group"], grades))

def main():
    storage = BSTStorage()
    load_data(storage)
    engine = StudentAnalytics(storage)

    while True:
        print("\n--- 🎓 ADMIN DASHBOARD ---")
        print("1. Search | 2. Delete | 3. Ranking | 4. Distribution | 5. Difficulty | 0. Exit")
        
        try:
            choice = input("Select Option: ")
            if choice == "1":
                sid = input("Enter ID: ")
                print(storage.search_by_id(sid) or "Not found")
            
            elif choice == "2":
                sid = input("ID to Delete: ")
                storage.delete(sid)
                print("Record processed.")

            elif choice == "3":
                for i, s in enumerate(engine.rank_students()[:5], 1):
                    print(f"{i}. {s.name} - {s.average():.1f}")

            elif choice == "4":
                for k, v in engine.get_grade_distribution().items():
                    print(f"Grade {k}: {'◼' * v} ({v})")

            elif choice == "5":
                for sub, score in engine.get_subject_difficulty():
                    print(f"{sub.capitalize()}: {score:.1f} avg")

            elif choice == "0": break
        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()

