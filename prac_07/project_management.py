import datetime

# Constants
COMPLETED_PERCENTAGE = 100
FILENAME = 'projects.txt'

def main():
    projects = load_projects(FILENAME)

    print("\nAll Projects:")
    display_projects(projects)

    filter_date = input("\nEnter a date to filter projects (dd/mm/yyyy): ")
    filtered_projects = filter_projects_by_date(projects, filter_date)
    print("\nFiltered Projects:")
    display_projects(filtered_projects)

    new_project = add_new_project()
    projects.append(new_project)

    save_projects('FILENAME', projects)
    print("\nProjects saved to file.")


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def is_completed(self):
        return self.completion_percentage >= COMPLETED_PERCENTAGE

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")


def load_projects(filename=FILENAME):
    projects = []
    with open(filename, 'r') as file:
        next(file)  # Skip the header
        for line in file:
            data = line.strip().split('\t')  # Split by tab
            if len(data) == 5:
                project = Project(*data)  # Unpack the data into the Project constructor
                projects.append(project)
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost\tEstimate Completion\n")
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    for project in projects:
        print(project)



def filter_projects_by_date(projects, date):
    filtered_projects = [project for project in projects if project.start_date > datetime.datetime.strptime(date, '%d/%m/%Y').date()]
    return filtered_projects


def add_new_project():
    name = input("Enter the name of the project: ")
    start_date = input("Enter the start date of the project (dd/mm/yyyy): ")
    priority = int(input("Enter the priority of the project: "))
    cost = float(input("Enter the cost of the project: "))
    estimate_completion = int(input("Enter the estimate completion percentage of the project: "))
    return Project(name, start_date, priority, cost, estimate_completion)


if __name__ == "__main__":
    main()
