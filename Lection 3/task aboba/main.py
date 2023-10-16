import hashlib
import random

targetHash = "e186022d0931afe9fe0690857e32f85e50165e7fbe0966d49609ef1981f920c6"
code = hashlib.sha256()

string = "aaaa"
let_num = 0
while not code.hexdigest() == targetHash:
    let_code = random.randint(97, 122)
    string = string[:let_num] + chr(let_code) + string[let_num + 1:]
    let_num += 1
    if let_num > 3:
        let_num = 0
    code = hashlib.sha256(string.encode())
        
    print(string + "|" + code.hexdigest())
print(f"Answer is: {string}")