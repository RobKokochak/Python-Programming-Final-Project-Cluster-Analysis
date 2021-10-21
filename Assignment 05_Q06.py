#Rob Kokochak

def recursivePow(num,exp):
    if exp == 1:
        return num
    else:
        result = num * recursivePow(num,exp-1)
    return result

print(recursivePow(3,4))
