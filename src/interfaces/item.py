class Item:
    """
    Class representing a student.
    """
    def __init__(self, student_id: str, name: str, group: str):
        self.student_id = student_id
        self.name = name
        self.group = group

    def __repr__(self):
        return f"Item(ID='{self.student_id}', Name='{self.name}', Group='{self.group}')"

    def __eq__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return self.student_id == other.student_id
