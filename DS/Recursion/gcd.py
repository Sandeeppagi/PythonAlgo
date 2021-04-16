def gcd(testVariable1, testVariable2):
    if testVariable1 == testVariable2:
        return testVariable1

    if testVariable1 > testVariable2:
        return gcd(testVariable1 - testVariable2, testVariable2)

    if testVariable1 < testVariable2:
        return gcd(testVariable1, testVariable2 - testVariable1)


testVariable1 = 42
testVariable2 = 56
print(f"GCD of {testVariable1}, {testVariable2} is {gcd(testVariable1, testVariable2)}")
