# MEE 1/18/22

print('Input the net sales for')

try:
    previous = float(input('- Prior period:'))
    current = float(input('- Current period:'))

    change = (current - previous) * 100 / previous

    if change > 0:
        result = f'Sales increase {abs(change)}%'
    else:
        result = f'Sales decrease {abs(change)}%'

    print(result)

except ValueError:
    print("Bad input! Please input numerical values for both prior and current")

except ZeroDivisionError:
    print("Please input another value that is not zero.")

finally:
    print("Thank you, have a great day.")