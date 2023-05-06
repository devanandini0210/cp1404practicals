import datetime
from project import Project


def main():
    filename = "projects.txt"
    projects = []

    menu = '''- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
    '''
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            in_file = open(filename, 'r')
            in_file.readline()

            for line in in_file:
                parts = line.strip().split('\t')
                project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
                projects.append(project)
            in_file.close()
            load_project(projects)

        elif choice == "S":
            save_project(projects, filename)

        elif choice == "D":
            display_project(projects)

        elif choice == "F":
            filter_project(projects)

        elif choice == "A":
            print("Let's add a new project")
            name = input("Name: ")
            start_date = input("Start Date: ")
            priority = input("Priority: ")
            cost_estimate = input("Cost Estimate: ")
            completion_percentage = input("Percent complete: ")
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)

        elif choice == "U":
            update_project(projects)

        print(menu)
        choice = input(">>> ").upper()


def load_project(projects):
    for project in projects:
        print(project)


def save_project(projects, filename):
    f = open(filename, "w")
    f.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
    for project in projects:
        f.write(
            f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")
    f.close()


def display_project(projects):
    projects.sort()
    print("Incomplete Projects: ")
    for project in projects:
        if project.completion_percentage != "100":
            print("\t" + str(project))
    print("Complete Projects: ")
    for project in projects:
        if project.completion_percentage == "100":
            print("\t" + str(project))


def filter_project(projects):
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    sorted_by_date = []
    for project in projects:
        if project.start_date >= date:
            sorted_by_date.append(project)

    sorted_by_date = sorted(sorted_by_date, key=date_key)
    for project in sorted_by_date:
        print(project)


def date_key(obj):
    return obj.start_date


def update_project(projects):
    for i, project in enumerate(projects):
        print(str(i) + "\t" + str(project))

    project_choice = int(input("Project Choice: "))
    percentage = input("New Percentage: ")
    priority = input("New Priority: ")

    projects[project_choice].completion_percentage = percentage
    projects[project_choice].priority = priority


main()
