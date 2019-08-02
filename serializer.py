def serialize(subject):
    string = subject.__dict__
    for category in string["grades"]:
        for counter, grade in enumerate(string["grades"][category][0]):
            string["grades"][category][0][counter] = grade.__dict__
    return str(string)
