class ListStorage:
    def __init__(self):
        self.data = []

    def add(self, item):
        for s in self.data:
            if s.student_id == item.student_id:
                raise ValueError("Duplicate ID")
        self.data.append(item)

    def delete(self, student_id):
        self.data = [s for s in self.data if s.student_id != student_id]

    # --- NEW: MANUAL QUICKSORT ---
    def sort_manually(self):
        self.data = self._quicksort(self.data)

    def _quicksort(self, arr):
        if len(arr) <= 1: return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x.average() > pivot.average()]
        mid = [x for x in arr if x.average() == pivot.average()]
        right = [x for x in arr if x.average() < pivot.average()]
        return self._quicksort(left) + mid + self._quicksort(right)

    def search_by_id(self, student_id):
        for s in self.data:
            if s.student_id == student_id: return s
        return None

    def get_all(self):
        return list(self.data)

