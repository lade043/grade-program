import subject
import user_IO

subjects = []
try:
    while True:
        user_input = user_IO.user_input()
        if user_input[0] == "input":
            if user_input[1] == "grade":
                subject_edit = subject.get_subject(subjects, user_input[2])
                if subject_edit:
                    subject_edit.add_grade(user_input[3], subject.Grade(user_input[4], user_input[5]))
            elif user_input[1] == "category":
                subject_edit = subject.get_subject(subjects, user_input[2])
                if subject_edit:
                    subject_edit.add_grade_category(user_input[3], user_input[4])
            elif user_input[1] == "subject":
                subjects.append(subject.Subject(user_input[2], user_input[3], user_input[4]))
        elif user_input[0] == "output":
            subject_get = subject.get_subject(subjects, user_input[1])
            user_IO.user_output(subject_get.return_average_subject)
    raise SystemError

except Exception as e:
    print('ERROR' + str(e))