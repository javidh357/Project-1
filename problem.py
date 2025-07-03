class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        try:
            self.salary = float(salary)
        except ValueError:
            raise ValueError("Salary must be a number")

    def yearly_salary(self):
        return self.salary * 12

    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Dept: {self.department}, Monthly Salary: {self.salary}, Yearly Salary: {self.yearly_salary()}")


class Manager(Employee):
    def __init__(self, emp_id, name, department, salary, team_size):
        super().__init__(emp_id, name, department, salary)
        self.team_size = int(team_size)

    def bonus(self):
        return 0.10 * self.yearly_salary() if self.team_size > 5 else 0

    def display(self):
        super().display()
        print(f"Team Size: {self.team_size}, Bonus: {self.bonus()}")


employees = {}

def load_employees():
    try:
        with open("employees.txt", "r") as file:
            for line in file:
                data = line.strip().split('|')
                if data[0] == "Employee":
                    emp = Employee(data[1], data[2], data[3], data[4])
                elif data[0] == "Manager":
                    emp = Manager(data[1], data[2], data[3], data[4], data[5])
                employees[data[1]] = emp
    except FileNotFoundError:
        pass


def save_employees():
    with open("employees.txt", "w") as file:
        for emp in employees.values():
            if isinstance(emp, Manager):
                file.write(f"Manager|{emp.emp_id}|{emp.name}|{emp.department}|{emp.salary}|{emp.team_size}\n")
            else:
                file.write(f"Employee|{emp.emp_id}|{emp.name}|{emp.department}|{emp.salary}\n")


def add_employee():
    try:
        emp_id = input("Enter Employee ID: ")
        if emp_id in employees:
            print("Employee already exists.")
            return
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))
        is_manager = input("Is this a Manager? (yes/no): ").lower()

        if is_manager == "yes":
            team_size = int(input("Enter Team Size: "))
            emp = Manager(emp_id, name, department, salary, team_size)
        else:
            emp = Employee(emp_id, name, department, salary)

        employees[emp_id] = emp
        print("Employee added successfully.")
    except ValueError as e:
        print(f"Error: {e}")


def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    try:
        emp = employees[emp_id]
        emp.display()
    except KeyError:
        print("Employee not found.")


def display_summary():
    if not employees:
        print("No employees to display.")
        return

    print("\n--- Employee Summary (Sorted by Salary Descending) ---")
    for emp in sorted(employees.values(), key=lambda e: e.salary, reverse=True):
        emp.display()
        print("-" * 40)


def main():
    load_employees()
    while True:
        print("Menu:")
        print("1. Add Employee/Manager")
        print("2. Search by Employee ID")
        print("3. Display All Employees")
        print("4. Exit")

        choice = input("Choose an option one : ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            search_employee()
        elif choice == '3':
            display_summary()
        elif choice == '4':
            save_employees()
            print("Data saved. Exiting.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
