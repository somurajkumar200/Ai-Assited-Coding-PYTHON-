def check_palindrome(number):
    """Return whether an integer reads the same forwards and backwards."""
    if str(number) == str(number)[::-1]:
        return "Palindrome Number"
    return "Not a Palindrome Number"

number = int(input("Enter an integer: "))
print(check_palindrome(number))
