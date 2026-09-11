def is_perfect_number(number):
    """Return True when number equals the sum of its proper divisors."""
    divisor_sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            divisor_sum += divisor
    return divisor_sum == number

try:
    number = int(input("Enter a positive integer: "))
    if number <= 0:
        print("Invalid input. Please enter a positive integer.")
    elif is_perfect_number(number):
        print("Perfect Number")
    else:
        print("Not a Perfect Number")
except ValueError:
    print("Invalid input. Please enter a positive integer.")
