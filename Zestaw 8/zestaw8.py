# Dominik Juszczyk
# Python 3.8
# Jezyk Python grupa nr 2
# Zestaw 8


import random
from math import sqrt


# Zadanie 1
def solve1(a, b, c):
    # ax * by + c = 0
    if a == 0 and b == 0:
        print("Wrong equation")
    else:
        if a != 0:
            print("zero of a function = ", -(c / a))
        if b != 0:
            print("y-intercept = ", -(c / b))


# Zadanie 3
def calc_pi(n):
    if n <= 0:
        raise ValueError("Wrong argument")
    hits = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        x = pow(x, 2)
        y = pow(y, 2)
        distance = sqrt(x + y)
        if distance < 1:
            hits += 1
    return 4 * (hits / n)


# Zadanie 4
def heron(a, b, c):
    p = (a + b + c) / 2
    s = p * (p - a) * (p - b) * (p - c)
    if s <= 0:
        raise ValueError("This triangle cannot exist")
    return sqrt(s)


# Zadanie 6
RESULTS = {}
def P(i, j):
    if i < 0 or j < 0:
        raise ValueError("Wrong arguments")
    if i == 0 and j == 0:
        return 0.5
    if j == 0:
        return 0.0
    if i == 0:
        return 1.0

    global RESULTS
    if i not in RESULTS:
        RESULTS[i] = {j: 0.5 * (P(i - 1, j) + P(i, j - 1))}
    elif j not in RESULTS[i]:
        RESULTS[i][j] = 0.5 * (P(i - 1, j) + P(i, j - 1))

    return RESULTS[i][j]
