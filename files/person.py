from json import JSONEncoder


class Person:

    def __init__(self, FIRST_NAME, LAST_NAME, YEAR_OF_BIRTH, MONTH_OF_BIRTH, DAY_OF_BIRTH, COMPANY, PROJECT, ROLE, ROOM,
                 HOBBY):
        self.FIRST_NAME = FIRST_NAME
        self.LAST_NAME = LAST_NAME
        self.YEAR_OF_BIRTH = YEAR_OF_BIRTH
        self.MONTH_OF_BIRTH = MONTH_OF_BIRTH
        self.DAY_OF_BIRTH = DAY_OF_BIRTH
        self.COMPANY = COMPANY
        self.PROJECT = PROJECT
        self.ROLE = ROLE
        self.ROOM = ROOM
        self.HOBBY = HOBBY

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()


class PersonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return obj.__dict__
        return JSONEncoder.default(self, obj)

