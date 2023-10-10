vowels = ["A", "E", "I", "O", "U"]
string = input("Please enter your prompt in English: \n")
for i, let in enumerate(string):
    if not let.upper() in vowels:
        string = string[:i] + " " + string[i + 1:]

print(string)