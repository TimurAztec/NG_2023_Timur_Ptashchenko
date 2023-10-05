import math

action = input("Enter math action you wanna perform ( + , - , *, / , sqrt, ^ ): ")
match action:
    case "+":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"Answer {num1 + num2}")
    case "-":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"Answer {num1 - num2}")
    case "*":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"Answer {num1 * num2}")
    case "/":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"Answer {num1 / num2}")
    case "sqrt":
        num = int(input("Enter number: "))
        print(f"Answer {math.sqrt(num)}")
    case "^":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"Answer {num1**num2}")