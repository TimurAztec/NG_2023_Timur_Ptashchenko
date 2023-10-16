import json

file_name = input("Enter file name: ")
key_name = input("Enter key you wanna get: ")

def find_key(data, key):
    results = []
    if isinstance(data, dict):
        if key in data:
            results.append(data[key])
        for value in data.items():
            results += find_key(value, key)
    elif isinstance(data, list):
        for item in data:
            results += find_key(item, key)
    return results


with open(file_name, "r") as file:
    file_data = json.load(file)
    keys = find_key(file_data, key_name)
    print(keys)
