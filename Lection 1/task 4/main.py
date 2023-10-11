import math

action = input("Enter math action you wanna perform ( + , - , *, / , sqrt, ^ ): ")
if (action == "sqrt"):
    num1 = int(input("Enter number: "))
else:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

answer = None
match action:
    case "+":
        answer = num1 + num2
    case "-":
        answer = num1 - num2
    case "*":
        answer = num1 * num2
    case "/":
        answer = num1 / num2
    case "sqrt":
        answer = math.sqrt(num1)
    case "^":
        answer = num1**num2

if answer:
    print(f"Answer: {answer}")
else:
    print("Wrong action or numbers!")