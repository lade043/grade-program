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

    def return_grades(self, category):  # Return all grades in one category
        return self.grades[category][0]

    def return_grade_categories(self):  # Return all categories
        return [i for i in self.grades]

    def return_average_of_category(self, category):  # Return average of one categorie
        return sum(self.grades[category][0]) / len(self.grades[category][0])

    def return_average_of_subject(self):
        rating_sum = 0
        grade_sum = 0
        for i in self.grades:
            rating_sum += self.grades[i][1]
            grade_sum += self.return_average_of_category(i)
        return grade_sum / rating_sum


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
