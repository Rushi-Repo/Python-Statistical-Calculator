def mode(numbers): #complete
    n = len(numbers)
    lst = []
    for i in range(0, n, 1):
        lst.append(numbers.count(numbers[i]))
    m = max(lst)
    for x in numbers:
        if numbers.count(x) == m:
            return x