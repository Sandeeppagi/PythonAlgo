def printOneToN(n):
    if n == 1:
        print(n)
        return
    printOneToN(n - 1)
    if n < 8:
        print(n)


def printNtoOne(n):
    if n == 1:
        print(n)
        return
    print(n)
    printNtoOne(n - 1)


printOneToN(9)
print('-'*15)
printNtoOne(9)
