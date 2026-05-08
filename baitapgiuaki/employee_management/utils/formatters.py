def format_currency(amount):
    return f"{amount:,.0f} VND"

def print_header(title):
    print("\n" + "="*60)
    print(f"{title:^60}")
    print("="*60)

def print_employee_table(employees):
    if not employees:
        print("\nChưa có dữ liệu nhân viên.")
        return

    print("\n" + "-"*120)
    print(f"{'ID':<10} | {'Tên':<20} | {'Tuổi':<5} | {'Email':<25} | {'Lương CB':<15} | {'Điểm':<5} | {'Loại':<10}")
    print("-"*120)
    for emp in employees:
        from models import Manager, Developer, Intern
        emp_type = "Unknown"
        if isinstance(emp, Manager): emp_type = "Manager"
        elif isinstance(emp, Developer): emp_type = "Developer"
        elif isinstance(emp, Intern): emp_type = "Intern"
        
        print(f"{emp.emp_id:<10} | {emp.name:<20} | {emp.age:<5} | {emp.email:<25} | {format_currency(emp.base_salary):<15} | {emp.performance_score:<5} | {emp_type:<10}")
    print("-"*120)
