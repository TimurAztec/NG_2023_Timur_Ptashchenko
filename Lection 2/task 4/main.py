vowels = ["A", "E", "I", "O", "U"]
string = input("Please enter your prompt in English: \n")
for letter_index, letter in enumerate(string):
    if not letter.upper() in vowels:
        string = string[:letter_index] + " " + string[letter_index + 1:]

print(string)