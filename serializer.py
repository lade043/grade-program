import json
import subject


class TempSubject:
    def __init__(self, string):
        self.__dict__ = json.loads(string)


def serialize(subject):
    string = subject.__dict__
    for category in string["grades"]:
        for counter, grade in enumerate(string["grades"][category][0]):
            string["grades"][category][0][counter] = grade.__dict__
    return str(string)


def deserialize(string):
    temp = TempSubject(string)
    _subject = subject.Subject(temp.name, bool(temp.main_subject), bool(temp.oral_exam))
    for category in temp.grades:
        _subject.add_grade_category(category, temp.grades[category][1])
    return _subject

