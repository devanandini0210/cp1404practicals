class Band:

    def __init__(self, name=""):
        self.name = name
        self.musicians = []

    def __str__(self):
        return f"{self.name} ({self.musicians[0]} {self.musicians[1]})"

    def __repr__(self):
        return str(vars(self))

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        if not self.musicians:
            return f"The band needs musicians!"
        return "\n".join(musician.play() for musician in self.musicians)



