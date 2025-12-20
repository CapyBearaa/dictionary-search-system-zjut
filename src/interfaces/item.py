# src/interfaces/item.py

from typing import Dict


class Item:
    """
    Represents a student with grades.
    """

    def __init__(self, student_id: str, name: str, group: str, grades: dict):
        self.student_id = student_id
        self.name = name
        self.group = group
        self.grades = grades  # dict: subject -> score

    def average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

    def __repr__(self):
        return (
            f"Item("
            f"ID={self.student_id}, "
            f"Name='{self.name}', "
            f"Group='{self.group}', "
            f"Avg={self.average():.2f}"
            f")"
        )


    def average(self) -> float:
        """
        Calculates average grade.
        """
        return sum(self.grades.values()) / len(self.grades)

    def __repr__(self) -> str:
        grades_str = ", ".join(
            f"{k.capitalize()}: {v}" for k, v in self.grades.items()
        )

        return (
            f"\n📘 Student Info\n"
            f"-------------------------\n"
            f"ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Group: {self.group}\n"
            f"Average: {self.average():.2f}\n"
            f"Grades: {grades_str}\n"
        )
