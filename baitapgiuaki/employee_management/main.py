import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

from models import Manager, Developer, Intern
from services.company import Company
from services.payroll import PayrollService
from utils.validators import validate_age, validate_salary, validate_email, validate_score
from utils.formatters import print_header, print_employee_table, format_currency
from exceptions.employee_exceptions import EmployeeException, EmployeeNotFoundError

def input_employee_info():
    while True:
        try:
            emp_id = input("Nhập ID nhân viên: ")
            name = input("Nhập tên nhân viên: ")
            age = int(input("Nhập tuổi: "))
            validate_age(age)
            email = input("Nhập email: ")
            validate_email(email)
            base_salary = float(input("Nhập lương cơ bản: "))
            validate_salary(base_salary)
            return emp_id, name, age, email, base_salary
        except ValueError as e:
            print(f"Lỗi nhập liệu: {e}. Vui lòng nhập lại.")
        except EmployeeException as e:
            print(f"Lỗi: {e}. Vui lòng nhập lại.")

def main():
    company = Company("ABC")
    payroll = PayrollService()

    while True:
        print_header("HỆ THỐNG QUẢN LÝ NHÂN VIÊN CÔNG TY ABC")
        print("1. Thêm nhân viên mới")
        print("2. Hiển thị danh sách nhân viên")
        print("3. Tìm kiếm nhân viên")
        print("4. Quản lý lương")
        print("5. Quản lý dự án")
        print("6. Đánh giá hiệu suất")
        print("7. Quản lý nhân sự")
        print("8. Thống kê báo cáo")
        print("9. Thoát")
        print("="*60)
        
        choice = input("Chọn chức năng (1-9): ")

        try:
            if choice == '1':
                print("\na. Thêm Manager")
                print("b. Thêm Developer")
                print("c. Thêm Intern")
                sub_choice = input("Chọn loại nhân viên: ")
                emp_id, name, age, email, base_salary = input_employee_info()
                
                if sub_choice == 'a':
                    team_size = int(input("Nhập team size: "))
                    company.add_employee(Manager(emp_id, name, age, email, base_salary, team_size))
                elif sub_choice == 'b':
                    lang = input("Nhập ngôn ngữ lập trình: ")
                    company.add_employee(Developer(emp_id, name, age, email, base_salary, lang))
                elif sub_choice == 'c':
                    uni = input("Nhập trường đại học: ")
                    company.add_employee(Intern(emp_id, name, age, email, base_salary, uni))
                else:
                    print("Lựa chọn không hợp lệ.")

            elif choice == '2':
                print("\na. Tất cả nhân viên")
                print("b. Theo loại (Manager/Developer/Intern)")
                print("c. Theo hiệu suất (từ cao đến thấp)")
                sub_choice = input("Chọn kiểu hiển thị: ")
                
                if sub_choice == 'a':
                    print_employee_table(company.employees)
                elif sub_choice == 'b':
                    print("1. Manager, 2. Developer, 3. Intern")
                    type_choice = input("Chọn loại: ")
                    if type_choice == '1': print_employee_table(company.get_employees_by_type(Manager))
                    elif type_choice == '2': print_employee_table(company.get_employees_by_type(Developer))
                    elif type_choice == '3': print_employee_table(company.get_employees_by_type(Intern))
                elif sub_choice == 'c':
                    print_employee_table(company.get_employees_sorted_by_performance())

            elif choice == '3':
                print("\na. Theo ID")
                print("b. Theo tên")
                print("c. Theo ngôn ngữ lập trình (cho Developer)")
                sub_choice = input("Chọn kiểu tìm kiếm: ")
                
                if sub_choice == 'a':
                    eid = input("Nhập ID: ")
                    try:
                        emp = company.find_employee_by_id(eid)
                        print_employee_table([emp])
                    except EmployeeNotFoundError as e:
                        print(e)
                elif sub_choice == 'b':
                    name = input("Nhập tên: ")
                    print_employee_table(company.search_by_name(name))
                elif sub_choice == 'c':
                    lang = input("Nhập ngôn ngữ: ")
                    print_employee_table(company.search_developer_by_language(lang))

            elif choice == '4':
                print("\na. Tính lương cho từng nhân viên")
                print("b. Tính tổng lương công ty")
                print("c. Top 3 nhân viên lương cao nhất")
                sub_choice = input("Chọn chức năng: ")
                
                if sub_choice == 'a':
                    eid = input("Nhập ID: ")
                    emp = company.find_employee_by_id(eid)
                    print(f"Lương của {emp.name}: {format_currency(emp.calculate_salary())}")
                elif sub_choice == 'b':
                    total = payroll.calculate_total_company_salary(company.employees)
                    print(f"Tổng lương công ty: {format_currency(total)}")
                elif sub_choice == 'c':
                    print_employee_table(payroll.get_top_3_highest_salaries(company.employees))

            elif choice == '5':
                print("\na. Phân công nhân viên vào dự án")
                print("b. Xóa nhân viên khỏi dự án")
                print("c. Hiển thị dự án của 1 nhân viên")
                print("d. Top 10 nhân viên tham gia nhiều dự án nhất")
                print("e. Top 10 nhân viên tham gia ít dự án nhất")
                print("f. Danh sách nhân viên tham gia đúng 1 dự án")
                sub_choice = input("Chọn chức năng: ")
                
                if sub_choice in ['a', 'b', 'c']:
                    eid = input("Nhập ID nhân viên: ")
                    emp = company.find_employee_by_id(eid)
                    
                    if sub_choice == 'a':
                        pname = input("Nhập tên dự án: ")
                        emp.add_project(pname)
                        print(f"Đã thêm dự án {pname} cho {emp.name}")
                    elif sub_choice == 'b':
                        pname = input("Nhập tên dự án cần xóa: ")
                        emp.remove_project(pname)
                        print(f"Đã xóa dự án {pname} khỏi {emp.name}")
                    elif sub_choice == 'c':
                        print(f"Dự án của {emp.name}: {', '.join(emp.projects) if emp.projects else 'Chưa có'}")
                elif sub_choice == 'd':
                    print_employee_table(company.get_top_10_most_projects())
                elif sub_choice == 'e':
                    print_employee_table(company.get_top_10_least_projects())
                elif sub_choice == 'f':
                    print_employee_table(company.get_employees_with_one_project())
                else:
                    print("Lựa chọn không hợp lệ.")

            elif choice == '6':
                print("\na. Cập nhật điểm hiệu suất cho nhân viên")
                print("b. Hiển thị nhân viên xuất sắc (điểm > 8)")
                print("c. Hiển thị nhân viên cần cải thiện (điểm < 5)")
                sub_choice = input("Chọn chức năng: ")
                
                if sub_choice == 'a':
                    eid = input("Nhập ID: ")
                    emp = company.find_employee_by_id(eid)
                    score = float(input("Nhập điểm mới (0-10): "))
                    validate_score(score)
                    emp.update_performance(score)
                    print(f"Đã cập nhật điểm cho {emp.name}")
                elif sub_choice == 'b':
                    excellent = [e for e in company.employees if e.performance_score > 8]
                    print_employee_table(excellent)
                elif sub_choice == 'c':
                    needs_imp = [e for e in company.employees if e.performance_score < 5]
                    print_employee_table(needs_imp)

            elif choice == '7':
                print("\na. Xóa nhân viên (nghỉ việc)")
                print("b. Tăng lương cơ bản cho nhân viên")
                print("c. Thăng chức (Intern -> Developer, Developer -> Manager)")
                print("d. Cắt giảm nhân sự (nghỉ việc hàng loạt)")
                sub_choice = input("Chọn chức năng: ")
                
                if sub_choice == 'd':
                    ids_str = input("Nhập danh sách ID nhân viên (cách nhau bởi dấu phẩy): ")
                    emp_ids = [eid.strip() for eid in ids_str.split(',') if eid.strip()]
                    count = company.layoff_employees(emp_ids)
                    print(f"Đã cắt giảm thành công {count} nhân viên.")
                else:
                    eid = input("Nhập ID: ")
                    if sub_choice == 'a':
                        company.remove_employee(eid)
                    elif sub_choice == 'b':
                        emp = company.find_employee_by_id(eid)
                        amount = float(input("Nhập số tiền tăng: "))
                        emp.base_salary += amount
                        print(f"Đã tăng lương cho {emp.name}. Lương mới: {format_currency(emp.base_salary)}")
                    elif sub_choice == 'c':
                        company.promote_employee(eid)
                    else:
                        print("Lựa chọn không hợp lệ.")

            elif choice == '8':
                print("\na. Số lượng nhân viên theo loại")
                print("b. Tổng lương theo phòng ban/loại")
                print("c. Số dự án trung bình trên mỗi nhân viên")
                sub_choice = input("Chọn chức năng: ")
                
                if sub_choice == 'a':
                    counts = payroll.count_by_type(company.employees)
                    for k, v in counts.items(): print(f"{k}: {v}")
                elif sub_choice == 'b':
                    salaries = payroll.total_salary_by_type(company.employees)
                    for k, v in salaries.items(): print(f"{k}: {format_currency(v)}")
                elif sub_choice == 'c':
                    avg = payroll.average_projects_per_employee(company.employees)
                    print(f"Số dự án trung bình: {avg:.2f}")

            elif choice == '9':
                print("Cảm ơn bạn đã sử dụng hệ thống!")
                sys.exit()
            else:
                print("Lựa chọn không hợp lệ, vui lòng chọn lại (1-9).")

        except EmployeeNotFoundError as e:
            print(f"Lỗi: {e}")
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")

if __name__ == "__main__":
    main()
