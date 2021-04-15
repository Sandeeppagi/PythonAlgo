def mod(dividend, divisor):
    if divisor == 0:
        return 'Divisor cannot be zero'
    if dividend < divisor:
        return dividend
    else:
        return mod(dividend - divisor, divisor)


dividend = 10
divisor = 4
print(f'Modulus for {dividend}/{divisor} is {mod(dividend, divisor)}')
