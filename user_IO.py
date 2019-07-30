def userinput():
    print("Hi User, \n do you want to edit your grades?")
    todo = input("Ok, do you want to see them or to edit them? [see/edit]\n")
    if todo == "see":
        print("Which subject do you want to know the information?")
        subject = input()
        return "output", subject
    elif todo == "edit":
        print("Do you want to add a subject, a category or a grade? [subject/category/grade]")
        useradd = input()
        if useradd == "subject":
            subject = input("Which subject do you want to add? \n")
            return "input", subject
        elif todo == "category":
            subject = input("To which subject do you want to add the category? \n")
            category = input("Which category do you want to add? \n")
            rating = float(input("Rating? \n"))
            return "input", subject, category, rating
        elif todo == "grade":
            subject = input("To which subject do you want to add the grade? \n")
            category = input("To which category do you want to add it? \n")
            grade = input("Grade? \n")
            gradename = input("What's the name of the grade? \n")
            return "input", subject, category, grade, gradename

