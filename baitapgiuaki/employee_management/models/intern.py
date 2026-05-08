from .employee import Employee

class Intern(Employee):
    def __init__(self, emp_id, name, age, email, base_salary, university):
        super().__init__(emp_id, name, age, email, base_salary)
        self.university = university

    def calculate_salary(self):
        # Lương Intern = Lương CB + (Điểm hiệu suất * 100)
        return self.base_salary + (self.performance_score * 100)

    def __str__(self):
        return super().__str__() + f" | Loại: Intern | Trường: {self.university}"
