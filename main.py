import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    d = datetime.datetime.today()
    print(f'Рассчет зарплаты от:{d}')
    get_employees()
    calculate_salary()
