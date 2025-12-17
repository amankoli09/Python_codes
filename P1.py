list=["tiger","lion","deer"]
print(list)
list.append("fox")
print(list)
list.extend(["Giraff","rihno","Horse"])
print(list)

a=["Sneha"]    # this is the concept of the concatition
b=a+["koli"]
print(b)

a=10
b=10.3
c="80 lakh average LPA"
d=[1,2,3,4]
e={"one","two","three"}
f={"name": "Aman", "age": 19}
g=True
h=[10,20,30,40]
i=h
j=[34,35,36,37]
print(id(h))
print(id(i))
print(id(j))
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

x=[1,2,3] # reference of a is different than reference of b
y=[1,2,3]
print(id(x))
print(id(y))
print(x is y)
print(x==y)
print(x is not y)
