from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str

    def __getattr__(self, name):
        if name == 'full_name':
            return "{0} {1}".format(self.first_name.capitalize(), self.last_name.capitalize())
        raise AttributeError("No such attribute: {}".format(name))
