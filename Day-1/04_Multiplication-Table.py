# Take a number n and print the multiplication table from 1–10.

def multiplication_table():
    n = float(input("Enter the number for the multiplication table to be printed:"))

    mult = 0

    for i in range(11):
        mult = i * n
        print(f"{n} X {i} = {mult}")


multiplication_table()
