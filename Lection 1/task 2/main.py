def is_int_convertable(val: str):
    try: 
        int(val)
    except ValueError:
        return False
    else:
        return True

def sum_up(val1: str, val2: str):
    if (not is_int_convertable(val1)) or (not is_int_convertable(val2)):
        print("Please enter corrent numbers!")
        return
    print(f"Numbers sum is: {int(val1) + int(val2)}")

if __name__ == "__main__":
    while True:
        print("Enter 2 numbers to sum up:")
        sum_up(input("Enter first number: "), input("Enter second number: "))