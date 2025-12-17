num=[1,2,3,4,5,6,7,8,"koli","aman","koli"]
# del num[0:4] #5,6,7,8
# del num[2:6]
num.remove("koli")
print(num)
while "koli" in num:
    num.reomove("koli")
    print(num)
