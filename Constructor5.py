class Employee:
    def __init__(self,emp_id,name):
        self.emp_id=emp_id
        self.name=name
        self.attendance=0

    def mark_attendance(self):
        self.attendance += 1
        print(f"{self.name}. marked present:. Total = {self.attendance}")
    
    def display_info(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Attendance:", self.attendance)

emp1=Employee(101,"Aman")
emp1.mark_attendance()
emp1.display_info()
print("\n")
emp2=Employee(102,"Ravi")
emp2.mark_attendance()
emp2.display_info()

# self represents the current instance of the class
# It is used to access instance variables and methods
# It is automatically passed to methods, that's why you must write it in method definitions
# You don’t write self while calling the method → Python fills it automatically

# class Employee:
#     def __init__(self, emp_id, name):
#         self.emp_id = emp_id
#         self.name = name
#         self.attendance = 0

#         # calling method inside constructor
#         self.mark_attendance()

#     def mark_attendance(self):
#         self.attendance += 1
#         print(f"{self.name} marked present. Total = {self.attendance}")
    
#     def display_info(self):
#         print("Employee ID:", self.emp_id)
#         print("Name:", self.name)
#         print("Attendance:", self.attendance)
