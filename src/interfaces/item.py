class Item:
    def __init__(self, student_id: str, name: str, group: str):
        self.student_id = student_id
        self.name = name
        self.group = group

    def __repr__(self):
        return f"Item({self.student_id}, {self.name}, {self.group})"
