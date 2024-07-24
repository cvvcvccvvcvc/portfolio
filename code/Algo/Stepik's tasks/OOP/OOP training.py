class Employee:
    
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    @property     # to call method as attribute  buuut u can t set a new value
    def email(self):   # email was atrib, but it seted in init, and when first was changed nothing
        return f"{self.first}.{self.last}@email.com"  # changed
    
    #  @fullname.setter  if i want to set another atrib's by setting fullname
    def fullname(self):
        return f"{self.first} {self.last}"
    # @fullname.deleter works with KW del emp_1.fullname (e.g. first, last = None, None)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}, {self.pay})"
    
    def __str__(self):
        return f'--> {self.fullname()}: {self.email}'

    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())
    
    @classmethod
    def set_raise_amt(cls, new_raise_amt):
        cls.raise_amt = new_raise_amt
    
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
    
    def __repr__(self):
        return super().__repr__(self) + f'developer atributes: ({self.prog_lang})'

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, *emps):
        for emp in emps:
            if emp not in self.employees:
                self.employees.append(emp)
    
    def remove_emp(self, *emps):
        for emp in emps:
            if emp in self.employees:
                self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Ivan', 'Lunegov', 100_000, 'Python')
emp_1 = Employee('Test', 'User', 10_000)
emp_2 = Employee('Test_2', 'User_2', 20_000)
mgr_1 = Manager('Obivavan', 'Lunegov', 100_000, [dev_1])
# isinstance issubclass

print(repr(mgr_1))
print(emp_1 + emp_2)  # = combined salary
print(len(emp_1))