class data:
    def __init__(self,name,age,salary,hra,da):
        self.name=name
        self.age=age
        self.salary=salary
        self.hra=hra
        self.da=da
        self.gross_salary=salary+hra+da
        self.anual_salary=self.gross_salary*12

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Salary:",self.salary)
        print("HRA:",self.hra)
        print("DA:",self.da)
        print("Gross Salary:",self.gross_salary)
        print("Anual Salary:",self.anual_salary)

print("----- Employee Details -----")
name=input("Enter Employee Name: ")
age=int(input("Enter Employee Age: "))
salary=float(input("Enter Employee Salary: "))
hra=float(input("Enter HRA: "))
da=float(input("Enter DA: "))

emp=data(name,age,salary,hra,da)
emp.display()