from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

staff = ['mike', 'david', 'steve']
dt = datetime.now()
dt_str = dt.strftime("Дата: %d/%m/%Y Время: %H:%M:%S")
if __name__ == '__main__':
    print(dt_str)
    calculate_salary(15, 36)
    get_employees(staff)