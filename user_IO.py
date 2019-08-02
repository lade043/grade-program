import exceptions


def user_input():
    todo = input("Ok, do you want to see them or to edit them [see/edit/exit]?\n")
    if todo == "see":
        print("Which subject do you want to know the information?")
        subject = input()
        return "output", subject
    elif todo == "edit":
        print("Do you want to add a subject, a category or a grade [subject/category/grade]?")
        user_add = input()
        if user_add == "subject":
            subject = input("Which subject do you want to add? \n")
            main_subject = input("Is this subject a main subject [y/n]? \n")
            if main_subject == 'y':
                main_subject = True
            elif main_subject == 'n':
                main_subject = False
            else:
                raise exceptions.WrongCaseException
            oral_exam = input("Will there be an oral exam in this subject [y/n]? \n")
            if oral_exam == 'y':
                oral_exam = True
            elif oral_exam == 'n':
                oral_exam = False
            else:
                raise exceptions.WrongCaseException
            return "input", "subject", subject, main_subject, oral_exam
        elif user_add == "category":
            subject = input("To which subject do you want to add the category? \n")
            category = input("Which category do you want to add? \n")
            rating = float(input("Rating? \n"))
            if exceptions.convertible(rating):
                return "input", "category", subject, category, rating
        elif user_add == "grade":
            subject = input("To which subject do you want to add the grade? \n")
            category = input("To which category do you want to add it? \n")
            grade = input("Grade? \n")
            grade_name = input("What's the name of the grade? \n")
            if exceptions.convertible(grade):
                return "input", "grade", subject, category, grade, grade_name
    elif todo == "exit":
        return "exit"


def user_output(subject, categories, average, average_subject):
    print("\n\n In the subject {} are the following categories:".format(subject))
    for counter, category in enumerate(categories):
        print("The average in {} is {} with these grades:".format(category, average[counter]))
        string = ""
        for grade in categories[category][0]:
            string += str(grade.grade) + ", "
        print(string + "\n")
        print("The average of {} is {}.".format(subject, average_subject))


def exception_raised(exception):
    print("Dear user you've raised an exception. The cause of the exception is:")
    if exception is exceptions.SubjectNotExistingException:
        print("The subject you tried to access is not created")
    elif exceptions is exceptions.CategoryNotExistingException:
        print("The category you tried to add something is non-existent in this subject")
    elif exception is exceptions.NotANumberException:
        print("The number you gave the program is not a number")
    elif exception is exceptions.WrongCaseException:
        print("This was not one of the available choices")