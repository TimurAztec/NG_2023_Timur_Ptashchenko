select = float(input("Convert Fahrenheit to Celsius - enter '1', convert Celsius to Fahrenheit enter - '2': "))
val = float(input("Enter temperature: "))
if select == 1:
    print(f"Temperature in Celsius is: {round((val - 32) * 5/9, 1)}")
elif select == 2:
    print(f"Temperature in Fahrenheit is: {round((val * 9/5) + 32, 1)}")