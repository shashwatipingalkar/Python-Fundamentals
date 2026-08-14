# Take integer n and print whether it is positive, negative or zero

def integer():
    n = int(input("Enter the number to be checked: "))

    if n > 0:
        print(f"{n} is positive")
    elif n < 0:
        print(f"{n} is negative")
    else:
        print(f"{n} is zero")


integer()
