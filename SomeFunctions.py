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
    

"""
FALLING POWERS FUNCTIONS FOR MY GRAPHING CALCULATOR:

[["g0", "falling_power(x,0)", -10.0, 10.0, 100.0, [99, 124, 97]], ["g1", "falling_power(x,1)", -10.0, 10.0, 100.0, [224, 121, 169]], ["g2", "falling_power(x,2)", -10.0, 10.0, 100.0, [59, 226, 222]], ["g3", "falling_power(x,3)", -10.0, 10.0, 100.0, [193, 191, 23]], ["g4", "falling_power(x,4)", -10.0, 10.0, 100.0, [229, 178, 215]], ["g5", "falling_power(x,5)", -10.0, 10.0, 100.0, [80, 99, 237]], ["g6", "falling_power(x,6)", -10.0, 10.0, 100.0, [17, 187, 111]], ["gx", "falling_power(x,x)", 0.0, 5.0, 250.0, [126, 192, 139]]]


RISING POWERS FUNCTIONS FOR MY GRAPHING CALCULATOR:

["h0", "rising_power(x,0)", -10.0, 10.0, 50.0, [111, 195, 196]], ["h1", "rising_power(x,1)", -10.0, 10.0, 100.0, [25, 232, 225]], ["h2", "rising_power(x,2)", -10.0, 10.0, 100.0, [157, 215, 29]], ["h3", "rising_power(x,3)", -10.0, 10.0, 100.0, [204, 56, 43]], ["h5", "rising_power(x,5)", -10.0, 10.0, 100.0, [231, 17, 203]]]

"""