def reverse_integer():
    user_input = input("Enter the integer to be reversed: ").strip()
    
    # Check for a negative sign
    if user_input.startswith('-'):
        reversed_str = '-' + user_input[1:][::-1]
    else:
        reversed_str = user_input[::-1]
        
    print(f"Reversed String: {reversed_str}")

reverse_integer()
