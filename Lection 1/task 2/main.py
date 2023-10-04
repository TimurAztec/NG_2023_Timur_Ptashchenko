tries_count: int = 0

def is_int_convertable(val: str):
    try: 
        int(val)
    except ValueError:
        return False
    else:
        return True

def sum_up(val1: str, val2: str):
    if (not is_int_convertable(val1)) or (not is_int_convertable(val2)):
        global tries_count
        tries_count += 1
        print("Please enter corrent numbers!") if tries_count <= 5 else print("Ты шо дебил? Ты в школе числа не учил? Числа вводи нормально!")
        if tries_count > 5: tries_count = 0
        return
    print(f"Numbers sum is: {int(val1) + int(val2)}")

while True:
    print("Enter 2 numbers to sum up:")
    sum_up(input("Enter first number: "), input("Enter second number: "))