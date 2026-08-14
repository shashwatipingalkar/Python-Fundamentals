from builtins import int


n = int(input("Enter the number: "))
for num in range(2, n):
    # Check if num has any factors other than 1 and itself
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break  # Not prime, skip to the next number
    else:
        # If the loop completes without finding a factor, it is prime
        print(num, end=" ")
