# a="xyz"
# b="xyz"
# print(a is not b)

# x=["aman"]
# y=["koli"]
# print(x is not y)

a=["a","b","c","b","b"]
while "b" in a:
    a.remove("b") 
print(a)
