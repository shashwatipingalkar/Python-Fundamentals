def palindrom():
    user_input = input("Enter the integer to be reversed: ").strip()

    # Check for a negative sign
    if user_input.startswith('-'):
        reversed_str = '-' + user_input[1:][::-1]
    else:
        reversed_str = user_input[::-1]

    if reversed_str == user_input:
        print(f"{user_input} is palindrom")
    else:
        print(f"{user_input} is not palindrom")


palindrom()
