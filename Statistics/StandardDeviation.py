from Calculator.Addition import addition
from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Calculator.Square import square
from Calculator.Squareroot import root

from Statistics.Mean import mean


def standard_deviation(numbers):  # complete
    n = len(numbers)
    c = 0
    t = 0
    for i in range(0, n, 1):
        c = subtraction(mean(numbers), numbers[i])
        t = addition(square(c), t)
    x = division((n - 1), t)
    return root(x)


