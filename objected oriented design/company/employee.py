class Employee:
    
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'

        Employee.num_of_emps += 1

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def pay_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Eric', 'Smith', 60000)
emp_2 = Employee('Emily', 'Williams', 60000)
print(Employee.num_of_emps)
