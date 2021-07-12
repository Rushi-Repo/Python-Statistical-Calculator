from Statistics.Mean import mean
from Statistics.sample import getSample

import random
import statistics


def samp_mean(numbers):
    ss = random.randint(1, len(numbers))
    new_values = getSample(numbers, ss)
    n = round(mean(new_values), 2)
    actual_mean = round(statistics.mean(new_values), 2)  # to compare calculated result
    return n, actual_mean
