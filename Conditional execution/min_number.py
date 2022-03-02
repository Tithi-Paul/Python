import numbers
from unittest import result


number1 = float(input("Enter a number: "))
number2 = float(input("Enter another number: "))
number3 = float(input("Enter a number again: "))
if number1 < number2:
    min = number1
    if number3 < min:
        result = number3
    else:
        result = min
else:
    min = number2
    if number3 < min:
        result = number3
    else:
        result = min
print(result)