end_num = int(input("Enter the number: "))
for iterational_num in range(1, end_num+1):
    zero_dividers = set()
    for divider_num in range(1, iterational_num+1):
        if iterational_num%divider_num == 0:
            zero_dividers.add(divider_num)
    print(f"{iterational_num} | {zero_dividers}")

prime_numbers = set()
prime_numbers.add(2)
for num in range(3, end_num + 1):
    if (num % 2 != 0 and all(num % prime_num != 0 for prime_num in range(3, int(num**0.5) + 1, 2))):
        prime_numbers.add(num)

print(f"\nPrime numbers:\n {prime_numbers}")