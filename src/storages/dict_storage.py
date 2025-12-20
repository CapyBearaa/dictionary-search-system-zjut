# src/storages/dict_storage.py
from typing import Any, Dict, List, Optional


class DictStorage:
    """
    Storage implementation using a Python dictionary (Hash Table).
    Provides O(1) average time complexity for adding and searching by ID.
    """
    
    def __init__(self):
        # Internal structure: {student_id: Item object}
        self.data: Dict[str, Item] = {}

    def add(self, item: Item) -> bool:
        """
        Adds a student to the storage using student_id as the key.
        Average Complexity: O(1)
        """
        self.data[item.student_id] = item
        return True

    def search_by_id(self, student_id: str) -> Optional[Item]:
        """
        Finds a student by their ID.
        Average Complexity: O(1)
        """
        return self.data.get(student_id)

    def search_by_name(self, name: str) -> List[Item]:
        """
        Finds students by name. Requires a linear scan of all items.
        Complexity: O(N)
        """
        results = []
        # Iterate through all student objects in the dictionary values
        for item in self.data.values():
            if item.name == name:
                results.append(item)
        return results

    def search_by_group(self, group: str) -> List[Item]:
        """
        Finds students by group. Requires a linear scan of all items.
        Complexity: O(N)
        """
        results = []
        # Iterate through all student objects in the dictionary values
        for item in self.data.values():
            if item.group == group:
                results.append(item)
        return results

    def get_all(self) -> List[Item]:
        """
        Returns a list of all students currently in storage.
        Complexity: O(N) (due to list creation)
        """
        return list(self.data.values())
