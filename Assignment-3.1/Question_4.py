import math
def classify_number(number: int) -> str:
    """Return the classification of number."""
    if number < 2:
        return "Neither"

    # Only test possible divisors through the square root.
    for divisor in range(2, math.isqrt(number) + 1):
        if number % divisor == 0:
            return "Composite"

    return "Prime"

try:
    value = int(input("Enter an integer: "))
    print(f"{value} is {classify_number(value)}.")
except ValueError:
    print("Invalid input. Please enter a whole integer.")
