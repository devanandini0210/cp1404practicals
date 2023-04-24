class ProgrammingLanguage:

    def __init__(self, language="", typing_style="", reflect=False, years=""):
        self.name = language
        self.typing = typing_style
        self.reflection = reflect
        self.year = years

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First Appeared in {self.year}"

    def is_dynamic(self):
        if self.typing.upper() == "DYNAMIC":
            return True
        else:
            return False
