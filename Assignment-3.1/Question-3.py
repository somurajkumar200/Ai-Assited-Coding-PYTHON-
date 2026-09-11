def is_armstrong(number):
    """Return True if number is an Armstrong number."""
    if number < 0:
        return False

    digits = str(number)
    power = len(digits)
    return sum(int(digit) ** power for digit in digits) == number

number = int(input("Enter an integer: "))

if is_armstrong(number):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

