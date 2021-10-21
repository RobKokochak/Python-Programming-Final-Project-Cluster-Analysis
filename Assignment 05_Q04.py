#Rob Kokochak

def recursiveMult(x,y):
    if x == 1:
        return y
    else:
        result = y + recursiveMult(x-1,y)   
    return result

print(recursiveMult(3,5))
