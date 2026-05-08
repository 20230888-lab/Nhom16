from models import Manager, Developer, Intern

class PayrollService:
    @staticmethod
    def calculate_total_company_salary(employees):
        return sum(emp.calculate_salary() for emp in employees)

    @staticmethod
    def get_top_3_highest_salaries(employees):
        return sorted(employees, key=lambda x: x.calculate_salary(), reverse=True)[:3]

    @staticmethod
    def count_by_type(employees):
        stats = {"Manager": 0, "Developer": 0, "Intern": 0}
        for emp in employees:
            if isinstance(emp, Manager): stats["Manager"] += 1
            elif isinstance(emp, Developer): stats["Developer"] += 1
            elif isinstance(emp, Intern): stats["Intern"] += 1
        return stats

    @staticmethod
    def total_salary_by_type(employees):
        stats = {"Manager": 0, "Developer": 0, "Intern": 0}
        for emp in employees:
            salary = emp.calculate_salary()
            if isinstance(emp, Manager): stats["Manager"] += salary
            elif isinstance(emp, Developer): stats["Developer"] += salary
            elif isinstance(emp, Intern): stats["Intern"] += salary
        return stats

    @staticmethod
    def average_projects_per_employee(employees):
        if not employees:
            return 0
        total_projects = sum(len(emp.projects) for emp in employees)
        return total_projects / len(employees)
