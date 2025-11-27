# A module containing a variety of mathematical operators

def add(a, b):
    """
    Adds two numbers.
    """
    return a + b

def subtract(a, b):
    """
    Subtracts the second number from the first.
    """
    return a - b

def multiply(a, b):
    """
    Multiplies two numbers.
    """
    return a * b

def divide(a, b):
    """
    Divides the first number by the second.
    Raises an exception if division by zero is attempted.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b 

def power(base, exponent):
    """
    Raises base to the power of exponent.
    """
    return base ** exponent

def factorial(n):
    """
    Returns the factorial of the given number.
    """
    if n < 0:
        raise ValueError("Input cannot be negative")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def is_prime(n):
    """
    Returns True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def sum_of_digits(n):
    """
    Returns the sum of digits of a number.
    """
    n = abs(n)
    return sum(int(digit) for digit in str(n))

def gcd(a, b):
    """
    Returns the greatest common divisor of a and b.
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)

def fib(n):
    """
    Returns the nth Fibonacci number.
    """
    if n < 0:
        raise ValueError("Input cannot be negative")
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

def lcm(a, b):
    """
    Returns the least common multiple of a and b.
    """
    return abs(a * b) // gcd(a, b)

def square_root(n):
    """
    Returns the square root of a number in the set of real numbers.
    """
    if n < 0:
        raise ValueError("Cannot take square root of a negative number")
    return n ** 0.5

def abs_diff(a, b):
    """
    Returns the absolute difference between two numbers.
    """
    return abs(a - b)

def log(a, base=10):
    """
    Returns the logarithm of a number to a specified base.
    """
    import math
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive values")
    if base <= 0 or base == 1:
        raise ValueError("Invalid base for logarithm")
    return math.log(a, base) 

def mod(a, b):
    """
    Returns the modulus (remainder) of a divided by b.
    """
    return a % b

def mean(numbers):
    """
    Returns the mean of a list of numbers.
    """
    if len(numbers) == 0:
        raise ValueError("numbers must not be empty")
    return sum(numbers) / len(numbers)

def median(numbers):
    """
    Returns the median of a list of numbers.
    """
    if len(numbers) == 0:
        raise ValueError("numbers must not be empty")
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    return sorted_numbers[n//2]

def mode(numbers):
    """
    Returns the mode of a list of numbers (most frequent value).
    """
    if len(numbers) == 0:
        raise ValueError("numbers must not be empty")
    from collections import Counter
    counts = Counter(numbers)
    return counts.most_common(1)[0][0]

def celsius_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit.
    """
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius.
    """
    return (fahrenheit - 32) * 5/9

def inverse(a):
    """
    Returns the multiplicative inverse of a number.
    """
    if a == 0:
        raise ValueError("Cannot invert zero")
    return 1 / a

def triangular_number(n):
    """
    Returns the nth triangular number (sum of the first n positive integers).
    """
    if n < 0:
        raise ValueError("Input cannot be negative")
    return n * (n + 1) // 2
