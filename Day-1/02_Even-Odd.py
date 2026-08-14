# Take an integer and siplay whether it is even or odd

def even_odd():
    n = int(input("Enter the number to be checked:"))

    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")


even_odd()
