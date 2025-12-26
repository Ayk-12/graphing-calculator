import math

def falling_power(x: int | float, n: int) -> int | float:
    if n <= 0:
        return 1
    return x * falling_power(x - 1, n - 1)

def rising_power(x: int | float, n: int) -> int | float:
    return falling_power(x + n - 1, n)

def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def cos(x: int | float) -> int | float:
    return math.cos(x)

def ln(x: float) -> float:
    if (x <= 0):
        return ln(x + 0.01)
    return math.log(x)

