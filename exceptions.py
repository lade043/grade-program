class NotANumberException(Exception):
    pass


class SubjectNotExistingException(Exception):
    pass


class CategoryNotExistingException(Exception):
    pass


class WrongCaseException(Exception):
    pass


def convertible(string):
    try:
        float(string)
        return True
    except ValueError:
        raise NotANumberException