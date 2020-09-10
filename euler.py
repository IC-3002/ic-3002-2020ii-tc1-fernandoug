import math

def e_cuadratica(n):
    res = 0
    for i in range(n):
    	res += 1 / math.factorial(i)
    return res


def e_lineal(n):
    factorial, res = 1, 0
    for i in range(n):
    	factorial *= n
    	res += 1 / factorial
    return res
