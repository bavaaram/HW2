#! /usr/bin/python3

def fact(n: int) -> int:
    """
    This function Actually takes you a number and calculate it's Factorail :)
    """
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def roundd(item: (int, float), digit: int) -> (int, float):
    """
    This function is for rounding a flaot number with desired limiting digits. 
    """
    item2 = (item // (10 ** -digit)) * (10 ** -digit)
    if (item - item2) * (10 ** (digit + 1)) > 5:
        item2 += (10 ** -digit)
    return item2


def neper(num: int, poww: (int, float)) -> (int, float):
    """
    This function is used for estimate neper (e^x) function with Maclaurin Series.
    it takes you number of terms and power of the neper (x) to estimate the e^x with 
    3-digits rounding :)
    """
    res = 0
    for i in range(int(num)):
        res += (poww **i) / (fact(i))
    return roundd(res, 3)

print(neper(100, 6))
