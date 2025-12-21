

class ListStorage:
    def __init__(self):
    
        self.data = []

    
    def add(self, item):
        
        
        for student in self.data:
            if student.id == item.id:
                
                raise ValueError(f"Item with id={item.id} already exists")

    
        self.data.append(item)
        return True

    def search_by_id(self, student_id):
        
        for student in self.data:
            if student.id == student_id:
                return student
        return None


    def search_by_name(self, name):
       
        result = []
        for student in self.data:
            if student.name == name:
                result.append(student)
        return result

    def search_by_group(self, group):
        
        result = []
        for student in self.data:
            if student.group == group:
                result.append(student)
        return result

    def get_all(self):
       
        return list(self.data)

    
