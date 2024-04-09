def first_alg(a, b, c):
    return ((a*c) ** 2) + ((b*c) ** 3) + ((c*c) ** 4)


def second_alg(b, z, d):
    if (z != 0):
        if (b/z > d):
            return "y = sin(w * f)"
        else:
            return "y = cos(w * f)"
    else:
        return "Ділення на нуль!"


def factorial(a):
    fact = 1
    for i in range(1, a+1):
        fact *= i
    return fact


def third_alg(a, b):
    if (a > b and a > 0):
        fact1 = factorial(a)
        num = fact1 * b
        fact2 = factorial(a-b)
        return num/fact2
    else:
        return "Непраильно введені дані!"
