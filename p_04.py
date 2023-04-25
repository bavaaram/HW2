#! /usr/bin/python3

def fact(n: int) -> int:
    """
    This function Actually takes you a number and calculate it's Factorial :)
    """
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def round_func(item: (int, float), digit: int) -> (int, float):
    """
    This function is for rounding a float number with desired limiting digits. 
    """
    item2 = (item // (10 ** -digit)) * (10 ** -digit)
    if (item - item2) * (10 ** (digit + 1)) > 5:
        item2 += (10 ** -digit)
    return item2


def neper_func(num: int, poww: (int, float)) -> (int, float):
    """
    This function is used for estimate neper (e^x) function with Maclaurin Series.
    it takes you number of terms and power of the neper (x) to estimate the e^x with 
    3-digits rounding :)
    """
    res = 0
    for i in range(int(num)):
        res += (poww **i) / (fact(i))
    return round_func(res, 3)

print(neper_func(100, 6))
