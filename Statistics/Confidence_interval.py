from Statistics.Mean import mean
from Statistics.StandardDeviation import standard_deviation
from Calculator.Squareroot import root
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Addition import addition
from Calculator.Subtraction import subtraction


def confidence_interval(numbers):
    m = mean(numbers)
    confidence_level = 0.95
    z = (1-confidence_level) / 2
    sd = standard_deviation(numbers)
    n = root(len(numbers))
    return [subtraction(multiplication(division(n, sd), z), m), addition(multiplication(division(n, sd), z), m)]
    #return [m - z*sd / n, m + z*sd / n]