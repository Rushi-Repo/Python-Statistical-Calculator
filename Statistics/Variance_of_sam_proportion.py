from Statistics.Proportion import proportion
from Statistics.sample import getSample
from Statistics.Proportion import proportion
from Calculator.Multiplication import multiplication
from Calculator.Subtraction import subtraction
from Calculator.Division import division
import random


def variance_samp_prop(numbers):
    ran = random.randint(1, len(numbers))
    values = getSample(numbers, ran)
    p = proportion(values)
    m = multiplication(p, subtraction(p, 1))
    x = subtraction(len(values), 1)
    h = division(x, m)
    return h
