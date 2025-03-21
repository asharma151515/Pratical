import datetime

# Constants
COMPLETED_PERCENTAGE = 100
FILENAME = 'projects.txt'

def main():
    projects = load_projects(FILENAME)
    print(f"Welcome to Pythonic Project Management\nLoaded {len(projects)} projects from {FILENAME}")

    while True:
        print_menu()
        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Enter filename to load projects: ")
            projects = load_projects(filename)

        elif choice == 's':
            filename = input("Enter filename to save projects: ")
            save_projects(filename, projects)

        elif choice == 'd':
            display_projects(projects)

        elif choice == 'f':
            filter_date = input("Show projects that start after date (dd/mm/yyyy): ")
            filtered_projects = filter_projects_by_date(projects, filter_date)
            display_projects(filtered_projects)

        elif choice == 'a':
            new_project = add_new_project()
            projects.append(new_project)

        elif choice == 'u':
            update_project(projects)

        elif choice == 'q':
            if input("Would you like to save to projects.txt? (yes/no): ").lower() == 'yes':
                save_projects(FILENAME, projects)
            print("Thank you for using custom-built project management software.")
            break

        else:
            print("Invalid option. Please try again.")

def print_menu():
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")

def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        header = file.readline()  # Skip header
        for line in file:
            parts = line.strip().split('\t')
            # Check if the number of parts is 5 (valid data), otherwise set default values
            if len(parts) == 5:
                projects.append(Project(*parts))
            elif len(parts) == 4:
                # If the completion percentage is missing, set it to 0
                parts.append("0")  # Default completion percentage to 0
                projects.append(Project(*parts))
            else:
                print(f"Skipping invalid project data: {line}")
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion\n")  # Write header
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")

def display_projects(projects):
    incomplete = [p for p in projects if p.completion_percentage < COMPLETED_PERCENTAGE]
    complete = [p for p in projects if p.completion_percentage == COMPLETED_PERCENTAGE]

    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")

    print("Completed projects:")
    for project in complete:
        print(f"  {project}")

def filter_projects_by_date(projects, filter_date):
    date = datetime.datetime.strptime(filter_date, "%d/%m/%Y").date()
    return [project for project in projects if project.start_date > date]

def add_new_project():
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion_percentage = input("Percent complete: ")
    return Project(name, start_date, priority, cost_estimate, completion_percentage)

def update_project(projects):
    display_projects(projects)
    while True:
        try:
            choice = int(input("Project choice: "))
            if 0 <= choice < len(projects):
                project = projects[choice]
                print(f"{project}")
                new_percentage = input("New Percentage (leave blank to keep existing): ")
                new_priority = input("New Priority (leave blank to keep existing): ")

                if new_percentage:
                    project.completion_percentage = int(new_percentage)
                if new_priority:
                    project.priority = int(new_priority)
                break  # Exit loop after valid input
            else:
                print("Invalid choice. Please enter a number between 0 and", len(projects)-1)
        except ValueError:
            print("Invalid input. Please enter a valid project number.")


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def is_completed(self):
        return self.completion_percentage == COMPLETED_PERCENTAGE

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")

if __name__ == "__main__":
    main()
