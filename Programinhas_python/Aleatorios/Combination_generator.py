from array import array


def combination_generator(end: int = 0, amount: int = 0, iterable: iter = None):
    combination = array('i', [0] * amount)
    if iterable:
        combination = array('i', iterable)
        amount = len(combination)
        end = max(combination)
    while combination.count(end) != amount:
        if combination[-1] >= end+1:
            for i in range(amount-1, -1, -1):
                if combination[i] >= end+1:
                    combination[i] = 0
                    combination[i - 1] += 1
                else:
                    break
        yield combination
        combination[-1] += 1
