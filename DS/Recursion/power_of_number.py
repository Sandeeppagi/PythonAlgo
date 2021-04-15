def power_of_number(base, power):
    if power == 0:
        return 1
    else:
        return base * power_of_number(base, power - 1)

base = 2
power = 3
print(f"Value of {base} to power the of {power} is {power_of_number(base, power)}")
