from datetime import datetime as str_date


class Subject:
    def __init__(self, name, main_subject, oral_exam):
        self.name = name
        self.grades = {}
        self.main_subject = main_subject
        self.oral_exam = oral_exam

    def add_grade_category(self, name, rating):
        self.grades[name] = ([], rating)

    def add_grade(self, category, grade):
        self.grades[category][0].append(grade)

    def return_grades(self, category):
        return self.grades[category][0]

    def return_grade_categories(self):
        return [i for i in self.grades]


class Grade:
    def __init__(self, grade, name, date=str(str_date.now())):
        self.grade = grade
        self.name = name
        self.date = date


def get_subject(liste, name):
    for subject in liste:
        if subject.name == name:
            return subject
    return None
