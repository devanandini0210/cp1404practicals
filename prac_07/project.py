import datetime


class Project:

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        date_string = start_date
        self.start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, Start Date : {self.start_date} , Priority : {self.priority}, Cost Estimate = {self.cost_estimate}, Completion Percentage {self.completion_percentage}"

    def __lt__(self, other):
        return self.priority < other.priority
