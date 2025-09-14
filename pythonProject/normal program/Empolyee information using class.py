class Employee:
    company="IBM"
    def __init__(self,name,salary):
        self.n=name
        self.s=salary
    def Show(self):
        print("Name:",self.n)
        print("SalarY:",self.s)
        print("Company:",Employee.company)
emp=Employee("Varad",25)
emp.Show()