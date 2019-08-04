import json
import subject


class TempSubjectSerialize:
    def __init__(self, _subject):
        self.name = _subject.name
        self.main_subject = str(_subject.main_subject)
        self.oral_exam = str(_subject.oral_exam)
        self.grades = {}
        for category in _subject.grades:
            self.grades[category] = {}
            for counter, grade in enumerate(_subject.grades[category][0]):
                self.grades[category][str(counter)] = {
                    "grade": str(grade.grade),
                    "name": str(grade.name),
                    "date": str(grade.date)
                }
            self.grades[category]["rating"] = _subject.grades[category][1]

    def get_string(self):
        string = self.__dict__
        string = str(string)
        string = string.replace("'", '"')
        return string


class TempSubjectDeserialize:
    def __init__(self, string):
        self.__dict__ = json.loads(string)


def serialize(_subject):
    ser = TempSubjectSerialize(_subject)
    string = ser.get_string()
    return str(string)


def deserialize(string):
    temp = TempSubjectDeserialize(string)
    _subject = subject.Subject(temp.name, bool(temp.main_subject), bool(temp.oral_exam))
    for category in temp.grades:
        _subject.add_grade_category(category, temp.grades[category]['rating'])
        for grade in temp.grades[category]:
            if grade != "rating":
                _subject.add_grade(category, subject.Grade(float(temp.grades[category][grade]["grade"]),  # the grade
                                                           temp.grades[category][grade]["name"],  # the name of grade
                                                           temp.grades[category][grade]["date"]))  # the date of grade
    return _subject
