from Statistics.ZScore import zscore
from Statistics.Mean import mean
from Statistics.StandardDeviation import standard_deviation
from Calculator.Subtraction import subtraction
from Calculator.Division import division
from Calculator.Multiplication import multiplication
from Calculator.Addition import addition


def population_correlation_coefficient(numbers, numbers1):
    m = zscore(numbers)
    n = zscore(numbers1)
    value = list(map(lambda a, b: a * b, m, n))
    p = division(len(value), sum(value))
    return p

"""
    x = mean(numbers)
    y = mean(numbers1)
    m = []
    n = []
    t = 0

    for i in numbers:
        zn = division(standard_deviation(numbers), subtraction(x, i))
        m.append(zn)

    for i in numbers1:
        zm = division(standard_deviation(numbers1), subtraction(y, i))
        n.append(zm)

    for i in range(len(numbers)):
        jk = multiplication(m[i], n[i])
        t = addition(t, jk)

    res = division(subtraction(1, len(numbers), t))

    return res
"""