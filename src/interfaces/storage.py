class SearchSystem:
    def __init__(self, storage):
        self.storage = storage

    def add_student(self, item):
        self.storage.add(item)

    def find_by_id(self, student_id):
        return self.storage.search_by_id(student_id)

    def find_by_name(self, name):
        return self.storage.search_by_name(name)

    def find_by_group(self, group):
        return self.storage.search_by_group(group)

    def get_all(self):
        return self.storage.get_all()

