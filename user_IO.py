def user_input():
    print("Hi User, \n do you want to edit your grades?")
    todo = input("Ok, do you want to see them or to edit them? [see/edit]\n")
    if todo == "see":
        print("Which subject do you want to know the information?")
        subject = input()
        return "output", subject
    elif todo == "edit":
        print("Do you want to add a subject, a category or a grade? [subject/category/grade]")
        user_add = input()
        if user_add == "subject":
            subject = input("Which subject do you want to add? \n")
            return "input", "subject", subject
        elif user_add == "category":
            subject = input("To which subject do you want to add the category? \n")
            category = input("Which category do you want to add? \n")
            rating = float(input("Rating? \n"))
            return "input", "category", subject, category, rating
        elif user_add == "grade":
            subject = input("To which subject do you want to add the grade? \n")
            category = input("To which category do you want to add it? \n")
            grade = input("Grade? \n")
            grade_name = input("What's the name of the grade? \n")
            return "input", "grade", subject, category, grade, grade_name
