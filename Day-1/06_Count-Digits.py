# Take an integer and count how many digits it has.
def count_digits():
    n = int(input("Enter the the integer: "))

    counted = len(str(abs(n)))
    print(counted)


count_digits()
