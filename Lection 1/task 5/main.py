import cmath

coefficients = []

for coef_name in ['a', 'b', 'c']:
    val = float(input(f"Enter coefficient {coef_name}: "))
    coefficients.append(val)

a, b, c = coefficients

D = b**2 - 4*a*c
if D >= 0:
    x1 = (-b + cmath.sqrt(D)) / (2*a)
    x2 = (-b - cmath.sqrt(D)) / (2*a)
else:
    x1 = complex(-b / (2*a), cmath.sqrt(-D) / (2*a))
    x2 = complex(-b / (2*a), -cmath.sqrt(-D) / (2*a))

if x1 == x2:
    print("Root :", x1)
else:
    print("Root 1:", x1)
    print("Root 2:", x2)
