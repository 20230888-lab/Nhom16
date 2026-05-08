from exceptions.employee_exceptions import InvalidAgeError, InvalidSalaryError

def validate_age(age):
    if not (18 <= age <= 65):
        raise InvalidAgeError(f"Tuổi {age} không hợp lệ (phải từ 18-65).")
    return True

def validate_salary(salary):
    if salary <= 0:
        raise InvalidSalaryError(f"Lương {salary} phải lớn hơn 0.")
    return True

def validate_email(email):
    if "@" not in email:
        raise ValueError("Email không đúng định dạng (thiếu @).")
    return True

def validate_score(score):
    if not (0 <= score <= 10):
        raise ValueError("Điểm hiệu suất phải trong khoảng 0-10.")
    return True
