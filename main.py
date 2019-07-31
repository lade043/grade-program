import subject
import user_IO

subjects = []
while True:
    user_input = user_IO.user_input()
    if user_input[0] == "input":
        if user_input[1] == "grade":
            subject_edit = subject.get_subject(subjects, user_input[2])
            if subject_edit:
                subject_edit.add_grade(user_input[3], subject.Grade(user_input[4], user_input[5]))
