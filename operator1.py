a=int(input("Enter the value of A : "))
b=int(input("Enter the value of B : "))
print("Enter the operator")
operator=input()
if operator=="+":
    sum=a+b
    print("The sum is ",sum)
elif operator=="-":
    diff=a-b
    print("The difference is ",diff)
elif operator=="*":
    prod=a*b
    print("The product is ",prod)
elif operator=="/":
    quot=a/b
    print("The quotient is ",quot)
elif operator=="//":
    floorquot=(a//b)
    print("The floor quotient is ",floorquot)   
elif operator=="**":
    exp=a**b
    print("The exponent is ",exp)        
else:
    print("Invalid operator")
