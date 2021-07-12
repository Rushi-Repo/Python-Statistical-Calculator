import random


def getSample(data, ss):
    random_values = random.choices(data, k=ss - 1)
    return random_values