import sys

def is_int_convertable(val: str):
    try: 
        int(val)
    except ValueError:
        return False
    else:
        return True

if __name__ == "__main__":
    correct: bool = False
    for index, arg in enumerate(sys.argv[1:]):
        if arg.startswith('-'):
            val: str = sys.argv[index+2]
            if arg == "-ftc" and is_int_convertable(val):
                print(f"Temperature in Celsius is: {round((int(val) - 32) * 5/9, 1)}")
                correct = True
                break
            if arg == "-ctf" and is_int_convertable(val):
                print(f"Temperature in Fahrenheit is: {round((int(val) * 5/9) + 32, 1)}")
                correct = True
                break
            if arg == "-help":
                print("-ftc [value] to convert Fahrenheit to Celsius")
                print("-ctf [value] to convert Celsius to Fahrenheit")
                correct = True
                break
    if not correct:
        print("Please add -help flag to get info")