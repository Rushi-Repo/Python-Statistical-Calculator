from Statistics.Proportion import proportion
from Statistics.Variance import variance
from Calculator.Subtraction import subtraction
from Calculator.Multiplication import multiplication
from Calculator.Division import division


def variance_of_population_proportion(numbers):
    n = len(numbers)
    prop = proportion(numbers)
    prop_2 = subtraction(prop, 1)
    x = multiplication(prop, prop_2)
    variance_of_pp = division(x, n)
    return variance_of_pp