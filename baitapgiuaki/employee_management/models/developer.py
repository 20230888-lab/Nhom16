from .employee import Employee

class Developer(Employee):
    def __init__(self, emp_id, name, age, email, base_salary, language):
        super().__init__(emp_id, name, age, email, base_salary)
        self.language = language

    def calculate_salary(self):
        # Lương Developer = Lương CB + (Số dự án * 1000) + (Điểm hiệu suất * 150)
        return self.base_salary + (len(self.projects) * 1000) + (self.performance_score * 150)

    def __str__(self):
        return super().__str__() + f" | Loại: Developer | Ngôn ngữ: {self.language}"
