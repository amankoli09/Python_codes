print("Enter the value of A")
inputA = input()
print("Enter the value of B")
inputB = input()
print("Enter the operator")
inputOperator = input()

if inputOperator == "+":
    print("The result is ",int(inputA) + int(inputB))
elif inputOperator == "-":
    print("The result is ",int(inputA) - int(inputB))
elif inputOperator == "*":
    print("The result is ",int(inputA) * int(inputB))
elif inputOperator == "/":
    print("The result is ",int(inputA) / int(inputB))
else:
    print("Invalid operator")