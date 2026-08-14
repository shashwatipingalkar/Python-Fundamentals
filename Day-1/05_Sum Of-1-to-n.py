# Take n and calculate the sum 1 + 2 + ... + n using a loop.

def sum():

    n = int(input("Enter the number: "))
    add = 0
    for i in range(n+1):
        add += i
    print(add)


sum()
