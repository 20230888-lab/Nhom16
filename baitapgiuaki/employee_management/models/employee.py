from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, emp_id, name, age, email, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.email = email
        self.base_salary = base_salary
        self.projects = []
        self.performance_score = 0.0

    @abstractmethod
    def calculate_salary(self):
        pass

    def add_project(self, project_name):
        if len(self.projects) >= 5:
            from exceptions.employee_exceptions import ProjectAllocationError
            raise ProjectAllocationError("Nhân viên đã có 5 dự án, không thể thêm mới.")
        self.projects.append(project_name)

    def remove_project(self, project_name):
        if project_name in self.projects:
            self.projects.remove(project_name)

    def update_performance(self, score):
        if not (0 <= score <= 10):
            raise ValueError("Điểm hiệu suất phải nằm trong khoảng 0-10")
        self.performance_score = score

    def __str__(self):
        return f"ID: {self.emp_id} | Tên: {self.name} | Tuổi: {self.age} | Lương CB: {self.base_salary} | Điểm: {self.performance_score}"
