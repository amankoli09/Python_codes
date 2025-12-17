class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name
        self.attendance = 0

        # calling method inside constructor
        self.mark_attendance()

    def mark_attendance(self):
        self.attendance += 1
        print(f"{self.name} marked present. Total = {self.attendance}")
    
    def display_info(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Attendance:", self.attendance)

name=input("Enter Employee Name: ")
emp_id=int(input("Enter Employee ID: "))

emp=Employee(emp_id,name)
emp.display_info()
