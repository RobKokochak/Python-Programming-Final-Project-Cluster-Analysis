#Rob Kokochak

def recursiveSum(x):
    if x == 1:
        return x
    else:
        result = x + recursiveSum(x-1)
    return result

print(recursiveSum(50))
