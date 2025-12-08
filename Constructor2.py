class Report:
    def __init__(self,m1,m2,m3,name,roll):
        self.name=name
        self.roll=roll
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.percentage=((m1+m2+m3)/300)*100

        print("Student Name:",name)
        print("Student Roll No.:",roll)
        print("Marks in Subject 1:",m1)
        print("Marks in Subject 2:",m2)
        print("Marks in Subject 3:",m3)
        print("Percentage:",self.percentage)
r1=Report(90,85,88,"Aman",101)


#     def total_marks(self):
#             return self.m1 + self.m2 + self.m3
    
#     def average_marks(self):
#             return self.total_marks() // 3
    
# r1=Report(90,85,88)
# print("Total Marks:",r1.total_marks())

# print("Average Marks:",r1.average_marks())
