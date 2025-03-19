import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def is_completed(self):
        return self.completion_percentage >= 100

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")


def load_projects(filename="projects.txt"):
    projects = []
    with open(filename, 'r') as file:
        next(file)  # Skip the header
        for line in file:
            data = line.strip().split('\t')  # Split by tab
            if len(data) == 5:
                project = Project(*data)  # Unpack the data into the Project constructor
                projects.append(project)
    return projects
