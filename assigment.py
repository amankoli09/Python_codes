x = 10
print(f"Initial value of x = {x}")
a = int(input("Enter number for x += : "))
x += a
print(f"After x += {a} → {x}")
b = int(input("Enter number for x -= : "))
x -= b
print(f"After x -= {b} → {x}")
c = int(input("Enter number for x *= : "))
x *= c
print(f"After x *= {c} → {x}")
d = int(input("Enter number for x /= : "))
x /= d
print(f"After x /= {d} → {x}")
e = int(input("Enter number for x %= : "))
x %= e
print(f"After x %= {e} → {x}")
f = int(input("Enter number for x **= : "))
x **= f
print(f"After x **= {f} → {x}")
g = int(input("Enter number for x //= : "))
x //= g
print(f"After x //= {g} → {x}")