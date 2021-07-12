from Calculator.Addition import addition
from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Calculator.Square import square
from Calculator.Squareroot import root
from Statistics.sample import getSample
from Statistics.Mean import mean
import random
from Statistics.StandardDeviation import standard_deviation
import statistics


def samp_st_dev(numbers):
    ss = random.randint(1, len(numbers))
    new_values = getSample(numbers, ss)
    c = 0
    t = 0
    n = len(new_values)
    for i in range(0, n, 1):
        c = subtraction(new_values[i], mean(new_values))
        t = addition(square(c), t)
    x = division(subtraction(1, n), t)
    actual_sd = statistics.stdev(new_values)  # Calculated using stat library to compare
    return root(x), actual_sd
