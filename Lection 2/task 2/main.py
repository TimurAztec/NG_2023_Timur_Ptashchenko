elements = []
while True:
    val = input("Enter unique value or enter nothig to finish: ")
    if (val == ""):
        break
    elements.append(val)

count = 0
for item in elements:
    try:
        float(item)
    except ValueError:
        continue
    else:
        count += 1

print(f"Number of numbers in list: {count} | {elements}")