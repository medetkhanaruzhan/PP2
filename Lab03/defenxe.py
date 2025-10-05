class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary 
    def increase_salary(self,percent):
        self.salary += self.salary * (percent / 100)

emp1 = Employee("Aruzhan", 47000)
print("До повышения:", emp1.salary)
emp1.increase_salary(10)
print("После повышения:", emp1.salary)