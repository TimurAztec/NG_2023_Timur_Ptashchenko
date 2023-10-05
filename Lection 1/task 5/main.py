import cmath

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

D = b**2 - 4*a*c
if D >= 0:
    x1 = (-b + cmath.sqrt(D)) / (2*a)
    x2 = (-b - cmath.sqrt(D)) / (2*a)
else:
    i = -b / (2*a)
    j = cmath.sqrt(-D) / (2*a)
    x1 = complex(i, j)
    x2 = complex(i, -j)

print("Root 1:", x1)
print("Root 2:", x2)
