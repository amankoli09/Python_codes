# class student:
#     def __init__(self, name,m1,m2,m3):
#         self.name = name
#         self.total_marks = m1 + m2 + m3
#         self.percentage=self.total_marks / 3

#     def showreport(self):
#         print("----- Report Card -----")
#         print("Name:", self.name)
#         print("Marks",self.m1,self.m2,self.m3)
#         print("Total Marks:", self.total_marks)
#         print("Percentage:", self.percentage)

# name=input("Enter Student Name: ")
# m1=int(input("Enter Marks in Subject 1: "))
# m2=int(input("Enter Marks in Subject 2: "))
# m3=int(input("Enter Marks in Subject 3: "))

# s1=student(name,m1,m2,m3)
# s1.showreport()

class student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.total_marks = m1 + m2 + m3
        self.percentage = self.total_marks / 3

    def showreport(self):
        print("----- Report Card -----")
        print("Name:", self.name)
        print("Marks:", self.m1, self.m2, self.m3)
        print("Total Marks:", self.total_marks)
        print("Percentage:", self.percentage)
        

name = input("Enter Student Name: ")
m1 = int(input("Enter Marks in Subject 1: "))
m2 = int(input("Enter Marks in Subject 2: "))
m3 = int(input("Enter Marks in Subject 3: "))

s1 = student(name, m1, m2, m3)
s1.showreport()
