file_name = input("Enter file name: ")
char_dict = {}
with open(file_name, "r") as file:
    content = file.read()
    for char in content:
        char_dict[char] = char_dict.get(char, 0) + 1
print(char_dict)
    