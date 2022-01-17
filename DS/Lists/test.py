listone = [20, 40]
listtwo = [20, 40]

print(listone == listtwo)
print(listone is listtwo)

print('-' * 15)

# for x in range(0.5, 5.5, 0.5):
#     print(x)

var = 'James Bond'
print(var[2::-1])
print('-' * 15)


def calculate(num1, num2=4):
    res = num1 * num2
    print(res)


calculate(5, 6)
print('-' * 15)

var = "James" * 2 * 3
print(var)
print('-' * 15)

# var1 = 1
# var2 = 2
# var3 = "3"
#
# print(var + var2 + var3)

x = 36 / 4 * (3 + 2) * 4 + 2
print(x)
print('-' * 15)

for i in range(10, 15, 1):
    print(i, end=', ')
print()
print('-' * 15)

value1 = 5 ** 2
value2 = 5 ** 3
print(value1)
print(value2)
print('-' * 15)

str = "pynative"
print(str[1:3])
print('-' * 15)

p, q, r = 10, 20, 30
print(p, q, r)
print('-' * 15)

sal = 8000


def printSal():
    sal = 12000
    print("Salary:", sal)


printSal()
print("Salary:", sal)
print('-' * 15)

for i in range(1, 3):
    print(i)
else:
    print('bhla bhla')
print('-' * 15)

a, b = 1, 0
a = a ^ b
b = a ^ b
a = a ^ b
print(a)


# str = "my name"
# for i in str:
#     print(i, end=", ")
#
# x = (i for i in range(3))
# for i in x:
#     print(i)
# for i in x:
#     print(i)


def twoNumberSum(array, targetSum):
    for firstNum in array:
        if targetSum - firstNum in array and targetSum - firstNum != firstNum:
            return [firstNum, targetSum - firstNum]
    return []


array = [3, 3]
targetSum = 6

print(twoNumberSum(array, targetSum))


def stockExchange(stockPrices):
    buy = stockPrices[0]
    sell = stockPrices[0]
    for price in stockPrices:
        if price < buy:
            buy = price
            sell = price
        if sell < price:
            sell = price
    return sell - buy


print('Stock', stockExchange([7, 1, 5, 3, 6, 4]))
print('Stock', stockExchange([7, 6, 4, 3, 1]))
