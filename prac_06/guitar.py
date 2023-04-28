class Guitar:

    def __init__(self, name="", year="", cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{name}({year}) : {cost}".format(name=self.name, year=self.year, cost=self.cost)

    def get_age(self):
        year = int(self.year)
        return 2023 - year

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False

