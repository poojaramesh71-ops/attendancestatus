def check_attendance(login_time):
    if login_time < 9.30:
        return "Present"
    elif 9.30 <= login_time <= 10.00:
        return "Late"
    else:
        return "Absent"


login_time = float(input("Enter login time (in 24-hour format, e.g., 9.45): "))

status = check_attendance(login_time)
print("Attendance Status:", status)