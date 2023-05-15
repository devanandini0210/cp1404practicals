from prac_09.musician import Musician


class Band:
    def __init__(self, name=""):
        self.name = name
        self.musician = Musician

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return str(vars(self))

    def add(self):