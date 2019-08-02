import subject
import user_IO
import serializer
import encryption
import exceptions
import os

subjects = []
filepath = "/data/user.grades"
try:
    password = user_IO.password()
    if os.path.isfile(filepath):
        with open(filepath, 'r') as file:
            string = encryption.decrypt(password, file.read())
            serializer.deserialize(string)

    while True:
        try:
            user_input = user_IO.user_input()
            input_or_output = user_input[0]
            if input_or_output == "input":
                _edit = user_input[1]
                _subject = user_input[2]
                if _edit == "grade":
                    _category = user_input[3]
                    _grade = user_input[4]
                    _grade_name = user_input[5]
                    subject_edit = subject.get_subject(subjects, _subject)
                    if subject_edit:
                        subject_edit.add_grade(_category, subject.Grade(_grade, _grade_name))
                elif _edit == "category":
                    _category = user_input[3]
                    _rating = user_input[4]
                    subject_edit = subject.get_subject(subjects, _subject)
                    if subject_edit:
                        subject_edit.add_grade_category(_category, _rating)
                elif _edit == "subject":
                    _main = user_input[3]
                    _oral = user_input[4]
                    subjects.append(subject.Subject(_subject, _main, _oral))
                else:
                    raise exceptions.WrongCaseException
            elif input_or_output == "output":
                _subject = user_input[1]
                subject_get = subject.get_subject(subjects, _subject)
                user_IO.user_output(subject_get.return_average_subject)
            elif input_or_output == "exit":
                break
            else:
                raise exceptions.WrongCaseException

        except (exceptions.NotANumberException, exceptions.CategoryNotExistingException,
                exceptions.SubjectNotExistingException, exceptions.WrongCaseException) as e:
            user_IO.exception_raised(e)

    with open(filepath, 'w') as file:
        _list = [serializer.serialize(_subject) for _subject in subjects]
        string = encryption.encrypt(password, str(_list))
        file.write(string)

except Exception as e:
    print('ERROR' + str(e))
