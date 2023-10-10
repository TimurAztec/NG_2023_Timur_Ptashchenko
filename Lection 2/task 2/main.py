def is_float_convertable(val):
    try:
        float(val)
    except ValueError:
        return False
    else:
        return True

elements = []
while True:
    val = input("Enter unique value or enter nothig to finish: ")
    if (val == ""):
        break
    elements.append(val)

count = 0
for item in elements:
    if is_float_convertable(item):
        count += 1

print(f"Number of numbers in list: {count} | {elements}")