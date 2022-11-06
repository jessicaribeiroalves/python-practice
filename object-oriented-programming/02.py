class Student:
    all_students = []

    def __init__(self, name, grade):
        self.name = name
        self._grade = grade
        Student.all_students.append(self)

    def get_grade(self):
        return self._grade

    def set_grade(self, grade):
        if grade <= 0 or grade > 100:
            raise ValueError("New grade not in the accepted range of [0-100].")
        self._grade = grade

    grade = property(get_grade, set_grade)

    @staticmethod
    def calculate_average_grade(students):
        if len(students) == 0:
            return -1
        grades_sum = 0
        for student in students:
            grades_sum += student.grade
        return grades_sum // len(students)

    @classmethod
    def get_average_grade(cls):
        return cls.calculate_average_grade(cls.all_students)

    @classmethod
    def get_best_student(cls):
        if len(cls.all_students) == 0:
            return None
        best_grade = 0
        best_student = None
        for student in cls.all_students:
            if student.grade > best_grade:
                best_grade = student.grade
                best_student = student
        return best_student
