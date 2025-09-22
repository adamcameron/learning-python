class Person:
    class FirstName():
        def __get__(self, obj, objtype=None):
            return obj._first_name

        def __set__(self, obj, value: str):
            obj._first_name = value.capitalize()

    class LastName():
        def __get__(self, obj, objtype=None):
            return obj._last_name

        def __set__(self, obj, value: str):
            obj._last_name = value.capitalize()

    first_name = FirstName()
    last_name = LastName()

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)
