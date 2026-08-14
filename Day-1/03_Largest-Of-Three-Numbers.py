# Take 3 numbers and print the largest without using max().

def largest():

    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))
    c = int(input("Enter the third number:"))

    if a > b and a > c:
        print(f"{a} is largest")
    elif b > a and b > c:
        print(f"{b} is largest")
    elif c > b and c > a:
        print(f"{c} is largest")
    elif a == b > c:
        print(f"{a} is largest")
    elif b == c > a:
        print(f"{b} is largest")
    elif a == c > b:
        print(f"{a} is largest")


largest()
