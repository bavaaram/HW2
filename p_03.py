#! /usr/bin/python3

def digit_summer(num):
    """
    This function takes you a number and summation it digits, if sum greater than 10, calculate the summation digits again with sum,
    but if sum smaller than 10, the sum is given to output.
    """
    num, summation = str(num), 0
    for i in num:
        summation += int(i)
    if summation > 10:
        num = summation
        return digit_summer(num)
    else:
        return summation

print(digit_summer(1234567))
