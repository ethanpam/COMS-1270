# Ethan Pham — Lab 9 — myMath unit tests

import pytest
from myMath import (
    add,
    subtract,
    multiply,
    divide,
    power,
    factorial,
    is_prime,
    sum_of_digits,
    gcd,
    fib,
    lcm,
    square_root,
    abs_diff,
    log,
    mod,
    mean,
    median,
    mode,
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    inverse,
    triangular_number,
)


def test_add_subtract_multiply():
    assert add(1, 2) == 3
    assert add(-4, 4) == 0
    assert subtract(5, 3) == 2
    assert subtract(-2, -5) == 3
    assert multiply(6, 0) == 0
    assert multiply(-3, 4) == -12


def test_divide_and_power():
    assert divide(9, 3) == 3
    assert divide(7, 2) == 3.5
    assert power(2, 5) == 32
    assert power(-3, 3) == -27
    with pytest.raises(ValueError):
        divide(10, 0)


def test_factorial_and_prime():
    assert factorial(0) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)
    assert is_prime(2) is True
    assert is_prime(15) is False
    assert is_prime(1) is False


def test_sum_of_digits_and_gcd():
    assert sum_of_digits(12345) == 15
    assert sum_of_digits(-909) == 18
    assert gcd(54, 24) == 6
    assert gcd(-8, 12) == 4


def test_fib_and_lcm():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(7) == 13
    with pytest.raises(ValueError):
        fib(-3)
    assert lcm(4, 6) == 12
    assert lcm(0, 5) == 0


def test_square_root_and_abs_diff():
    assert square_root(16) == 4
    assert square_root(0) == 0
    with pytest.raises(ValueError):
        square_root(-9)
    assert abs_diff(10, 4) == 6
    assert abs_diff(4, 10) == 6


def test_log_and_mod():
    assert log(100) == 2
    assert log(8, 2) == 3
    with pytest.raises(ValueError):
        log(-10)
    with pytest.raises(ValueError):
        log(10, 1)
    assert mod(10, 3) == 1
    assert mod(-10, 3) == 2


def test_mean_median_mode():
    assert mean([1, 2, 3, 4]) == 2.5
    with pytest.raises(ValueError):
        mean([])
    assert median([3, 1, 2]) == 2
    assert median([1, 2, 3, 4]) == 2.5
    with pytest.raises(ValueError):
        median([])
    assert mode([1, 2, 2, 3]) == 2
    with pytest.raises(ValueError):
        mode([])


def test_temperature_conversions():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100


def test_inverse_and_triangular_number():
    assert inverse(4) == 0.25
    assert inverse(-2) == -0.5
    with pytest.raises(ValueError):
        inverse(0)
    assert triangular_number(0) == 0
    assert triangular_number(5) == 15
    with pytest.raises(ValueError):
        triangular_number(-1)
