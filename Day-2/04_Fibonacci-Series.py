def fibonacci():
    n = int(input("Enter the number: "))
    if n < 1:
        print("Please enter a positive number")
        return
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b


fibonacci()
