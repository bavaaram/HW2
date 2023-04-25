#! /usr/bin/python3

def digit_summer(num):
    """
    This function takes you a number and summ it digits, if sum greater than 10, calculate the summation digits again with sum,
    but if sum smaller than 10, the sum is given to output.
    """
    num, summ = str(num), 0
    for i in num:
        summ += int(i)
    if summ > 10:
        num = summ
        return digit_summer(num)
    else:
        return summ

print(digit_summer(123456))
