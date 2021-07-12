from Calculator.Addition import addition
from Calculator.Division import division

"""
def median(numbers):  # complete
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        x = division(2, addition(division(2, addition(n, 2)), division(2, n)))
        return x
    else:
        x = int(division(2, addition(n, 1)))
        return numbers[x - 1]
"""


def median(numbers):
    n = len(numbers)
    numbers.sort()
    if n % 2 == 0:
        first_median = numbers[int(division(2, n))]
        second_median = numbers[len(numbers) // 2 - 1]
        med = division(2, addition(first_median, second_median))
    else:
        med = numbers[division(2, n)]
    return med
