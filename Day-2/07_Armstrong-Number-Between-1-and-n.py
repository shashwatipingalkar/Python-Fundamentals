def print_armstrong_numbers(n):
    n =  int(input("Enter the number:"))
    for i in range(1, n + 1):
        s = str(i)
        power = len(s)
        total = sum(int(digit) ** power for digit in s)
        if total == i:
            print(i)

print_armstrong_numbers()
