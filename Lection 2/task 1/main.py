elements = set()
while True:
    val = input("Enter unique value or enter nothig to finish: ")
    if (val == ""):
        break
    elements.add(val)

print(f"Unique elements: {elements}")