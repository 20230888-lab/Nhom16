from models import Employee, Manager, Developer, Intern
from exceptions.employee_exceptions import EmployeeNotFoundError, DuplicateEmployeeError

class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        for emp in self.employees:
            if emp.emp_id == employee.emp_id:
                # Nếu trùng ID, tự động sinh ID mới (thêm hậu tố _new)
                new_id = f"{employee.emp_id}_new"
                print(f"Lỗi: Trùng mã nhân viên {employee.emp_id}. Tự động đổi sang {new_id}")
                employee.emp_id = new_id
                break
        self.employees.append(employee)

    def remove_employee(self, emp_id):
        emp = self.find_employee_by_id(emp_id)
        self.employees.remove(emp)
        print(f"Đã xóa nhân viên có ID: {emp_id}")

    def find_employee_by_id(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                return emp
        raise EmployeeNotFoundError(emp_id)

    def search_by_name(self, name):
        return [emp for emp in self.employees if name.lower() in emp.name.lower()]

    def search_developer_by_language(self, language):
        return [emp for emp in self.employees if isinstance(emp, Developer) and emp.language.lower() == language.lower()]

    def get_employees_by_type(self, emp_class):
        return [emp for emp in self.employees if isinstance(emp, emp_class)]

    def get_employees_sorted_by_performance(self):
        return sorted(self.employees, key=lambda x: x.performance_score, reverse=True)

    def promote_employee(self, emp_id):
        emp = self.find_employee_by_id(emp_id)
        if isinstance(emp, Intern):
            new_emp = Developer(emp.emp_id, emp.name, emp.age, emp.email, emp.base_salary, "Python")
            self.replace_employee(emp, new_emp)
            print(f"Thăng chức Intern -> Developer cho {emp.name}")
        elif isinstance(emp, Developer):
            new_emp = Manager(emp.emp_id, emp.name, emp.age, emp.email, emp.base_salary, 0)
            self.replace_employee(emp, new_emp)
            print(f"Thăng chức Developer -> Manager cho {emp.name}")
        else:
            print("Manager đã ở cấp bậc cao nhất.")

    def replace_employee(self, old_emp, new_emp):
        index = self.employees.index(old_emp)
        # Giữ lại các thuộc tính quan trọng
        new_emp.projects = old_emp.projects
        new_emp.performance_score = old_emp.performance_score
        self.employees[index] = new_emp

    def get_top_10_most_projects(self):
        return sorted(self.employees, key=lambda x: len(x.projects), reverse=True)[:10]

    def get_top_10_least_projects(self):
        return sorted(self.employees, key=lambda x: len(x.projects))[:10]

    def get_employees_with_one_project(self):
        return [emp for emp in self.employees if len(emp.projects) == 1]

    def layoff_employees(self, emp_ids):
        removed_count = 0
        for eid in emp_ids:
            try:
                emp = self.find_employee_by_id(eid)
                self.employees.remove(emp)
                removed_count += 1
            except EmployeeNotFoundError:
                print(f"Không tìm thấy nhân viên ID: {eid} để xóa.")
        return removed_count
