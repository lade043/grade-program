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
            subject = input("Where do you want to add the category? \n")
            category = input("Which category do you want ot add? \n")