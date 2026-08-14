# Take integer input from the user
num = int(input("Enter a number: "))

# Prime numbers must be greater than 1
if num > 1:
    # Loop from 2 to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
