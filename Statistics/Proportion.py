from Calculator.Division import division
from Calculator.Addition import addition


def proportion(lst):
    t = 0
    for n in lst:
        if (n % 2) == 0:
            t = addition(t, 1)
        value = division(len(lst), t)
    return value

