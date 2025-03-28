class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())

    def __eq__(self, value):
        return self.get_sum() == value.get_sum()

    def __ne__(self, value):
        return self.get_sum() != value.get_sum()

    def __gt__(self, value):
        return self.get_sum() > value.get_sum()

    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()

    def __lt__(self, value):
        return self.get_sum() < value.get_sum()

    def __le__(self, value):
        return self.get_sum() <= value.get_sum()


students = [
    Student("홍길동", 87, 95, 75, 83),
    Student("이영희", 95, 90, 85, 78),
    Student("박철수", 75, 90, 80, 95),
]

student_a = Student("홍길동", 87, 95, 75, 83)
student_b = Student("이영희", 95, 90, 85, 78)

print("홍길동 총점: ", student_a.get_sum())
print("이영희 총점: ", student_b.get_sum())

print("student_a == student_b: ", student_a == student_b)
print("student_a != student_b: ", student_a != student_b)
print("student_a > student_b: ", student_a > student_b)
print("student_a >= student_b: ", student_a >= student_b)
print("student_a < student_b: ", student_a < student_b)
print("student_a <= student_b: ", student_a <= student_b)

