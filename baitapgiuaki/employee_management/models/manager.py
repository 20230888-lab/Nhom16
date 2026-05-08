from .employee import Employee

class Manager(Employee):
    def __init__(self, emp_id, name, age, email, base_salary, team_size):
        super().__init__(emp_id, name, age, email, base_salary)
        self.team_size = team_size

    def calculate_salary(self):
        # Lương Manager = Lương CB + (Số nhân viên quản lý * 500) + (Điểm hiệu suất * 200)
        return self.base_salary + (self.team_size * 500) + (self.performance_score * 200)

    def __str__(self):
        return super().__str__() + f" | Loại: Manager | Team size: {self.team_size}"
