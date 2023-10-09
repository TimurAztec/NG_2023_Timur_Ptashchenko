import math

action = input("Enter math action you wanna perform ( + , - , *, / , sqrt, ^ ): ")
if (action == "sqrt"):
    num1 = int(input("Enter number: "))
else:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
match action:
    case "+":
        print(f"Answer {num1 + num2}")
    case "-":
        print(f"Answer {num1 - num2}")
    case "*":
        print(f"Answer {num1 * num2}")
    case "/":
        print(f"Answer {num1 / num2}")
    case "sqrt":
        print(f"Answer {math.sqrt(num1)}")
    case "^":
        print(f"Answer {num1**num2}")