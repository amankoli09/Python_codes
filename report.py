# name=input("Enter Student name:")
# roolnum=input("Enter roll number:")
# maths=input("Enter Maths marks:")
# science=input("Enter science marks:")
# english=input("Enrter English mars:")

# total= maths+science+english
# average=total/3

# if average>=45:
#     result="Pass"
# else:
#     result="FAIL"

# print("***** Student Report Card *****")
# print("Name :",name)
# print("Roll No :",roolnum)
# print("Total :",total)
# print("Average :",average)
# print("Result :",result)
# print("********************************")
# Mini Project - Student Report Card

# taking inputs
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

# calculations
total = maths + science + english
average=total/3
average = round(average,2)

# result condition (change 40 if your pass marks are different)
if average >= 45:
    result = "PASS"
else:
    result = "FAIL"

# printing report card
print("\n----- Student Report Card -----")
print("Name   : ", name)
print("Roll No: ", roll_no)
print("Total  : ", total)
print("Average: ", average)
print("Result : ", result)
print("--------------------------------")