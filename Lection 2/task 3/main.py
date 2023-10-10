end_num = int(input("Enter the number: "))
for i in range(1, end_num+1):
    zero_dividers = set()
    for j in range(1, i+1):
        if i%j == 0:
            zero_dividers.add(j)
    print(f"{i} | {zero_dividers}")

prime_numbers = set()
prime_numbers.add(2)
for num in range(3, end_num + 1):
    if (num % 2 != 0 and all(num % i != 0 for i in range(3, int(num**0.5) + 1, 2))):
        prime_numbers.add(num)

print(f"\nPrime numbers:\n {prime_numbers}")