# Zestaw 11
# Zadanie 1

import random
from math import sqrt


def a(n):
    result = list(range(n))
    random.shuffle(result)
    return result


def b(n):
    result = sorted(range(n), key=lambda element: element + random.randint(-2, 2), reverse=False)
    return result


def c(n):
    result = sorted(range(n), key=lambda element: element + random.randint(-2, 2), reverse=True)
    return result


def d(n):
    result = list(random.gauss(0, 1) for i in range(n))
    return result


def e(n):
    k = int(sqrt(n))
    result = list(random.randint(0, k) for i in range(n))
    return result
