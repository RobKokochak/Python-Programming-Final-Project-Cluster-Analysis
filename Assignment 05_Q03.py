#Rob Kokochak

def recursivePrint(n):
    if n == 1:
        print(n)
    else:
        recursivePrint(n - 1)
        print(n)

recursivePrint(10)
