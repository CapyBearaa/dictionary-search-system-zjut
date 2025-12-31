class StudentAnalytics:
    def __init__(self, storage):
        self.storage = storage

    def rank_students(self):
        return sorted(self.storage.get_all(), key=lambda s: s.average(), reverse=True)

    def get_grade_distribution(self):
        dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
        for s in self.storage.get_all():
            avg = s.average()
            if avg >= 90: dist["A"] += 1
            elif avg >= 80: dist["B"] += 1
            elif avg >= 70: dist["C"] += 1
            elif avg >= 60: dist["D"] += 1
            else: dist["F"] += 1
        return dist

    def get_subject_difficulty(self):
        students = self.storage.get_all()
        subjects = ["math", "english", "physics", "history", "programming"]
        results = {}
        for sub in subjects:
            avg = sum(s.grades.get(sub, 0) for s in students) / len(students)
            results[sub] = avg
        return sorted(results.items(), key=lambda x: x[1]) # Hardest first
