def factorial(number):
    """Return the factorial of a non-negative integer."""
    if number < 0:
        return None

    result = 1
    for value in range(2, number + 1):
        result *= value
    return result

number = int(input("Enter an integer: "))
result = factorial(number)

if result is None:
    print("Factorial is not defined for negative numbers.")
else:
    print(result)

