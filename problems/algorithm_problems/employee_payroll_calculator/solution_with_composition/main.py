from problems.algorithm_problems.employee_payroll_calculator.solution_with_composition.hr import calculate_payroll, LTDPolicy
from problems.algorithm_problems.employee_payroll_calculator.solution_with_composition.productivity import track
from problems.algorithm_problems.employee_payroll_calculator.solution_with_composition.employees import employee_database


if __name__ == '__main__':
    employees = employee_database.employees

    sales_employee = employees[2]
    ltd_policy = LTDPolicy()
    sales_employee.apply_payroll_policy(ltd_policy)

    track(employees, 40)
    calculate_payroll(employees)
